# dndig — Campaign Art with Continuity

[`dndig`](https://github.com/mickume/dndig) generates campaign illustrations with Google's Gemini image models. Its point is **continuity**: a character portrait you approve once becomes the reference image for every later scene that character appears in.

dndig works on a **project**: a directory with a `dndig.yaml` file at its root. In a lorewright campaign, that project is the campaign's `art/` directory. Every prompt file under it is indexed by its `title`, and the approved image of one prompt (its **pick**) can be fed into other prompts as a labelled reference.

---

## Install

dndig is a single Go binary (Go 1.26+):

```bash
git clone https://github.com/mickume/dndig.git
cd dndig
make install                 # builds ./cmd/dndig into ~/go/bin/dndig
export GEMINI_API_KEY=...    # also accepted: GOOGLE_API_KEY
```

`go install github.com/mickume/dndig/cmd/dndig@latest` does **not** work (the AgentKit dependency is consumed through a `replace` directive).

---

## Campaign Art Layout

Lorewright writes every campaign's `art/` directory as a dndig project:

```
campaigns/[campaign-name]/art/
├── dndig.yaml                   # marks art/ as the dndig project root
├── .gitignore                   # keeps candidate takes out of git
├── README.md                    # how to generate this campaign's images
├── styles/
│   └── campaign.md              # the campaign's style directive
├── refs/                        # optional: your own reference images
├── characters/                  # kind: character — NPC portraits
│   ├── captain-harrow.md        # prompt file (title: captain-harrow)
│   ├── images/
│   │   └── captain-harrow.jpg   # the pick — linked from npcs.md
│   └── captain-harrow/          # dndig workspace (created by dndig)
│       ├── takes/001.jpg …      # every candidate, with JSON sidecars
│       ├── pick.json            # which take was picked
│       └── sheet.png            # optional turnaround sheet
├── locations/                   # kind: location — establishing shots of places
│   ├── harbor-district.md
│   └── images/harbor-district.jpg
├── items/                       # kind: item — artifacts, handouts (optional)
├── maps/                        # kind: other — region and battle maps (optional)
└── scenes/                      # kind: scene — encounters and read-aloud moments
    ├── ambush-at-the-docks.md   # cast: [captain-harrow]
    └── images/ambush-at-the-docks.jpg
```

**Why `art/` and not the campaign root is the project:** dndig indexes every Markdown file under its root and requires unique titles across them. Keeping the project in `art/` keeps chapters, `npcs.md` and other campaign documents out of that index.

**Rules that make the layout work:**

1. **File name = title.** `characters/captain-harrow.md` has `title: captain-harrow`. dndig names the pick after the file (`images/captain-harrow.jpg`) and resolves `cast:` and `references:` by title; keeping both identical makes every path predictable.
2. **Titles are unique across all of `art/`.** Letters, digits, `-` and `_` only. Use lowercase kebab-case.
3. **No numeric prefixes.** dndig orders a run by dependency (a scene's `cast:` and title `references:` are generated first), so `01_` prefixes are unnecessary — and they would leak into the image file names.
4. **One folder per kind.** Only create the folders the campaign needs; `characters/`, `locations/` and `scenes/` are the usual minimum.
5. **Never run `dndig init` inside a campaign.** It scaffolds sample prompts (`kaelen`, `ambush`). Lorewright writes `dndig.yaml`, `.gitignore`, `styles/campaign.md` and `README.md` itself.

### `art/dndig.yaml`

```yaml
# dndig project configuration for this campaign's art. Every key is optional.
# model: gemini-3-pro-image          # image model when a prompt names none
style: campaign                      # styles/campaign.md, applied to every prompt
workers: 2                           # concurrent requests
```

### `art/.gitignore`

```
**/takes/
**/discards/
```

### `art/README.md`

Write it from [templates/art-README.md](../templates/art-README.md), filling in the campaign name and the folders that actually exist.

---

## Style Directive

`art/styles/campaign.md` is sent with every prompt, as the system instruction **and** as the opening paragraph of the prompt. It holds the campaign's look; individual prompts should not repeat it.

```markdown
---
name: campaign
---
Dark fantasy illustration, painterly and atmospheric. Muted earth tones with
selective accents of crimson and gold. Dramatic chiaroscuro lighting.
Reminiscent of classic fantasy book cover art. Realistic proportions;
architecture weathered and ancient. No anime or cartoon styles. Do not add
text, captions, borders or any decoration to the picture.
```

Cover medium, brushwork, palette, lighting, composition, mood and what to avoid. Optional frontmatter `references:` lists style example images (relative to the style file) that are sent as "style reference only".

A DM with example art can derive a style instead of writing one:

```bash
dndig style derive styles/campaign.md refs/examples/*.jpg --hint "grim northern campaign" --force
```

---

## Prompt Files

Markdown with a frontmatter block. The body is the image description.

```markdown
---
title: ambush-at-the-docks
kind: scene
aspect_ratio: "16:9"
resolution: 2K
takes: 2
cast: [captain-harrow, sister-vael]
references: [harbor-district]
---
Captain Harrow stands at the edge of the pier, cutlass drawn, as Sister Vael
pulls a drowned lantern from the black water behind her...
```

### Frontmatter Fields

| Field | Default | Description |
|-------|---------|-------------|
| `title` | file stem | Unique name within `art/`; what `cast:` and `references:` use. Keep it equal to the file stem |
| `kind` | `other` | `character`, `scene`, `location`, `item` or `other`; changes how references are described to the model |
| `style` | `dndig.yaml` `style:` | Style name (`styles/<name>.md`) or path. Omit to use the campaign style |
| `aspect_ratio` | `1:1` | See table below (quote it: `"16:9"`) |
| `resolution` | `1K` | `1K`, `2K`, `4K` (`512` only on `gemini-3.1-flash-image`) |
| `takes` | `1` | Candidates per run, 1–8 |
| `temperature` | model default | 0–2; sent only when set |
| `seed` | — | Recorded; best-effort only |
| `model` | `gemini-3-pro-image` | Per-prompt model override |
| `cast` | — | Titles of character prompts whose picks become labelled references (max 5; fidelity drops above 3) |
| `references` | — | Other prompts' titles (resolve to their picks) or image files relative to the prompt file: `[harbor-district, ../refs/bridge.jpg, {path: ../refs/sword.png, as: "Harrow's cutlass"}]` |
| `search` | `false` | Google Search grounding |

Any other field is an error. The dndig 1.x fields `instructions:` and `batch:` are still accepted as aliases of `style:` and `takes:`, but new prompts use the current names. A request carries at most 14 images in total (cast + references + style references).

### Aspect Ratios

| Value | Use |
|-------|-----|
| `2:3`, `3:4`, `4:5` | Portraits, character art |
| `9:16` | Full-body characters, towers, tall maps |
| `1:1` | Tokens, items, battle maps |
| `4:3`, `5:4`, `3:2` | Classic scene and location composition |
| `16:9` | Establishing shots, encounters, landscapes |
| `21:9` | Panoramic vistas, banners |
| `1:4`, `4:1`, `1:8`, `8:1` | Extreme strips (banners, scrolls) |

### Recommended Settings by Content

| Content | Folder | `kind` | `aspect_ratio` | `resolution` | `takes` |
|---------|--------|--------|----------------|--------------|---------|
| NPC portrait | `characters/` | `character` | `2:3` or `3:4` | `2K` | `3` |
| Full-body character | `characters/` | `character` | `9:16` | `2K` | `3` |
| Location establishing shot | `locations/` | `location` | `16:9` or `4:3` | `2K` | `2` |
| Scene / encounter | `scenes/` | `scene` | `16:9` | `2K` | `1`–`2` |
| Panoramic vista | `scenes/` or `locations/` | `scene` / `location` | `21:9` | `2K` | `1` |
| Item / artifact / handout | `items/` | `item` | `1:1` | `1K` | `2` |
| Battle or region map | `maps/` | `other` | `1:1` or `4:3` | `2K`–`4K` | `2` |

### Writing the Prompt Body

- **Characters are character bibles.** Build, age, hair, scars, outfit, signature props, expression, framing. This pick is what every later scene copies, so be specific.
- **Scenes name their cast, they don't redescribe them.** With `cast: [captain-harrow]`, dndig sends Harrow's pick first and tells the model to keep face, hair, build, clothing and props exactly as shown. Describe what Harrow is *doing*, not what she looks like — a competing facial description fights the reference.
- **Reuse places with `references:`.** A scene set in the harbour lists `references: [harbor-district]` so the architecture stays consistent.
- **Build on the read-aloud text.** Then add what prose leaves out: composition, camera angle, light direction, focal point.
- **Leave the art style to `styles/campaign.md`.** Don't end each prompt with "dark fantasy, painterly…".

---

## Commands

Run every command from the campaign's `art/` directory (dndig finds the project root by walking up to `dndig.yaml`, so paths from elsewhere work too).

| Command | Does |
|---------|------|
| `dndig status` | Every prompt with its kind, take count, pick, and missing casts |
| `dndig generate <prompt.md\|dir>... [--takes N] [--dry-run] [--auto-pick]` | Generate candidate takes. A directory means every prompt file directly inside it (not recursive) |
| `dndig pick <prompt.md> --take N` | Approve a take: moves it to `images/<title>.jpg` beside the prompt |
| `dndig refine <prompt.md> "instruction" [--take N]` | Edit a take in conversation (default: the pick, else the latest take) |
| `dndig sheet <prompt.md>` | Front/side/back turnaround of a character's pick; travels with the pick into scenes |
| `dndig prune <prompt.md\|dir>... [--delete]` | Move unpicked takes to `discards/` (or delete them) |
| `dndig style derive <out.md> <image>...` | Derive a style directive from example images |
| `dndig style show campaign` | Print the resolved style |

Flags shared by `generate`, `refine` and `sheet`: `--model ID` and `--dry-run` (prints the full request — model, style, every reference image and the assembled prompt — without spending anything). Global flags: `-v/--verbose`, `--debug`, `--api-key KEY`.

**Things to know:**

- `generate` always makes **new** takes; it never skips a prompt that already has a pick. To fill in only new prompts, pass their files, not the whole folder.
- A directory argument with no prompt files is an error, so only pass folders that exist and contain prompts.
- A prompt whose `cast:` or title `references:` have no pick cannot be assembled — not even with `--dry-run` — and the run stops there. Pick the dependencies first, or use `--auto-pick`, which picks the first take of any prompt that has none so one run can feed its own scenes. `dndig status` lists what each prompt still `needs:`.
- `pick` moves an image; picking again moves the previous pick back into `takes/`. It refuses to overwrite an image at the pick path that no `pick.json` accounts for.

### Models

| Model | Sizes | Use |
|-------|-------|-----|
| `gemini-3-pro-image` (default) | 1K 2K 4K | Final art |
| `gemini-3.1-flash-image` | 512 1K 2K 4K | Fast drafts: `--model gemini-3.1-flash-image` |
| `gemini-3.1-flash-lite-image` | 1K | Cheapest; at most 3 reference images |

---

## Linking Images into Campaign Content

The pick of `art/<folder>/<title>.md` is `art/<folder>/images/<title>.jpg`. Link it with that path from the campaign root:

```markdown
![Captain Harrow](art/characters/images/captain-harrow.jpg)
![The Harbor District](art/locations/images/harbor-district.jpg)
![Ambush at the Docks](art/scenes/images/ambush-at-the-docks.jpg)
```

The path is known before any image exists, so lorewright writes the links when it writes the prompts. Gemini returns PNG; if a pick has another extension (images imported from elsewhere, or older dndig output), the link uses that extension.

See [formatting-conventions.md](formatting-conventions.md#image-integration) for where each image goes.

---

## Generating All Images for a Campaign

The full procedure is in each campaign's `art/README.md` ([template](../templates/art-README.md)). In short:

```bash
cd campaigns/[campaign-name]/art
dndig status                                          # every prompt parses; what each scene needs
dndig generate characters/ --dry-run                  # inspect requests (scenes dry-run once casts are picked)

# Curated: approve every character before it is reused
dndig generate characters/
dndig pick characters/captain-harrow.md --take 2      # one per character
dndig generate locations/ items/ maps/
dndig pick locations/harbor-district.md --take 1      # one per location/item/map
dndig generate scenes/ --auto-pick                    # or pick each scene by hand

# Unattended: one pass, first take of everything is picked
dndig generate characters/ locations/ items/ maps/ scenes/ --auto-pick

dndig prune characters/ locations/ items/ maps/ scenes/   # tidy up unpicked takes
```

### When a Description Changes

If an NPC's or location's appearance changes in the campaign text:

1. Update its prompt file.
2. `dndig generate characters/<title>.md`, then `dndig pick characters/<title>.md --take N` (or `dndig refine` for a small change).
3. Regenerate the scenes that list it in `cast:` or `references:` (`grep -l "<title>" scenes/*.md`) and pick again.

The image links in the campaign text do not change.
