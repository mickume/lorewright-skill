# [Campaign Name] — Artwork

This directory holds the image prompts for [Campaign Name] and the approved images they produced. It is a [dndig](https://github.com/mickume/dndig) project: `dndig.yaml` marks it as the project root, and every prompt file below is generated with dndig.

## Contents

| Folder | Kind | Prompts | Used in |
|--------|------|---------|---------|
| `characters/` | NPC portraits | [N] | `npcs.md`, chapters |
| `locations/` | Establishing shots | [N] | `locations.md`, chapters |
| `scenes/` | Encounters and read-aloud moments | [N] | chapters |
| `items/` | Artifacts and handouts | [N] | chapters, `npcs.md` |
| `maps/` | Region and battle maps | [N] | `locations.md`, chapters |

<!-- Remove the rows for folders this campaign does not have. -->

- `styles/campaign.md` — the campaign's visual style, applied to every prompt (set in `dndig.yaml`).
- `<folder>/<title>.md` — a prompt file. Its approved image (the **pick**) is `<folder>/images/<title>.png`, and that is the path the campaign documents link to.
- `<folder>/<title>/` — dndig's workspace for that prompt: every candidate take in `takes/`, `pick.json`, and an optional turnaround `sheet.png`. Takes are git-ignored.

Scenes list the characters in them under `cast:` and the places under `references:`. dndig sends those picks along as reference images, so a portrait approved once keeps the same face in every scene. That is why characters are approved before scenes.

## Setup

```bash
git clone https://github.com/mickume/dndig.git
cd dndig && make install          # Go 1.26+; installs ~/go/bin/dndig
export GEMINI_API_KEY=...         # https://aistudio.google.com/apikey
```

Run every command below from this directory:

```bash
cd campaigns/[campaign-name]/art
dndig status                      # every prompt, its pick, and what it still needs
```

## Generate Everything

### Option A — Curated (recommended)

Approve each character and place before scenes reuse it.

```bash
# 1. Characters: 3 takes each; inspect characters/<title>/takes/ and pick the best
dndig generate characters/
dndig pick characters/[npc-title].md --take N        # repeat for every character
dndig sheet characters/[npc-title].md                # optional: turnaround for recurring NPCs

# 2. Places, items and maps
dndig generate locations/ items/ maps/
dndig pick locations/[location-title].md --take N    # repeat for every prompt

# 3. Scenes — their casts and references are now picked
dndig generate scenes/ --dry-run                     # optional: inspect what will be sent
dndig generate scenes/
dndig pick scenes/[scene-title].md --take N          # repeat, or pass --auto-pick above
```

### Option B — Unattended

One pass; the first take of every prompt becomes its pick:

```bash
dndig generate characters/ locations/ items/ maps/ scenes/ --auto-pick
```

dndig orders the run so every character and place is generated (and picked) before the scenes that use it. Review the results afterwards and replace any weak pick with Option A's commands.

<!-- Pass only folders that exist and contain prompts: dndig refuses an empty one. -->

## Fix or Replace an Image

```bash
dndig refine characters/[npc-title].md "make the scar longer, hair darker"   # edits the pick
dndig pick characters/[npc-title].md --take N                                # approve the new take
dndig generate characters/[npc-title].md --takes 3                           # or start over
```

After a character or location changes, regenerate the scenes that use it:

```bash
grep -l "[npc-title]" scenes/*.md      # scenes with it in cast: or references:
dndig generate scenes/[scene-title].md
dndig pick scenes/[scene-title].md --take N
```

`dndig generate` always adds new takes, even when a prompt already has a pick, so pass single files to fill in or redo specific images rather than whole folders.

## Tidy Up

```bash
dndig prune characters/ locations/ items/ maps/ scenes/          # unpicked takes → discards/
dndig prune characters/ locations/ items/ maps/ scenes/ --delete # or delete them
```

## Troubleshooting

| Message | Fix |
|---------|-----|
| `<title> has no approved image yet` | A cast member or reference has no pick: `dndig pick <its file> --take N`, then re-run the remaining prompts |
| `title "x" is used by both …` | Titles must be unique across all of `art/`; rename one prompt (file and `title:`) |
| `unknown field` | Only dndig's frontmatter fields are allowed; see the lorewright dndig reference |
| `no prompt files found` | Remove that folder from the command |
| `… exists but …/pick.json does not say which take it is` | An image sits at the pick path without a `pick.json` (e.g. imported art); move it away and pick again |
