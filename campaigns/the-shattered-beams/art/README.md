# The Shattered Beams — Artwork

This directory holds the image prompts for The Shattered Beams and the approved images they produced. It is a [dndig](https://github.com/mickume/dndig) project: `dndig.yaml` marks it as the project root, and every prompt file below is generated with dndig.

## Contents

| Folder | Kind | Prompts | Used in |
|--------|------|---------|---------|
| `characters/` | NPC portraits | 7 | `npcs.md`, chapters |
| `locations/` | Establishing shots | 5 | `locations.md`, chapters |
| `scenes/` | Encounters and read-aloud moments | 30 | chapters |

- `styles/campaign.md` — the campaign's visual style, applied to every prompt (set in `dndig.yaml`).
- `<folder>/<title>.md` — a prompt file. Its approved image (the **pick**) is `<folder>/images/<title>.png`, and that is the path the campaign documents link to.
- `<folder>/<title>/` — dndig's workspace for that prompt: every candidate take in `takes/`, `pick.json`, and an optional turnaround `sheet.png`. Takes are git-ignored.

Scenes list the characters in them under `cast:` and the places under `references:`. dndig sends those picks along as reference images, so a portrait approved once keeps the same face in every scene. That is why characters are approved before scenes.

The images in `characters/images/`, `locations/images/` and `scenes/images/` were made with dndig 1.x and imported as picks. They have no `pick.json`, so `dndig status` shows them as "no pick" — but they are used as references all the same. To replace one, move the old image out of `images/` first, then generate and pick as below (and update its `.jpg` link in the campaign text to `.png`).

## Setup

```bash
git clone https://github.com/mickume/dndig.git
cd dndig && make install          # Go 1.26+; installs ~/go/bin/dndig
export GEMINI_API_KEY=...         # https://aistudio.google.com/apikey
```

Run every command below from this directory:

```bash
cd campaigns/the-shattered-beams/art
dndig status                      # every prompt, its pick, and what it still needs
```

## Generate Everything

### Option A — Curated (recommended)

Approve each character and place before scenes reuse it.

```bash
# 1. Characters: 3 takes each; inspect characters/<title>/takes/ and pick the best
dndig generate characters/
dndig pick characters/sera-mourne.md --take N        # repeat for every character
dndig sheet characters/sera-mourne.md                # optional: turnaround for recurring NPCs

# 2. Places
dndig generate locations/
dndig pick locations/eld-pylon.md --take N    # repeat for every prompt

# 3. Scenes — their casts and references are now picked
dndig generate scenes/ --dry-run                     # optional: inspect what will be sent
dndig generate scenes/
dndig pick scenes/the-parlay.md --take N          # repeat, or pass --auto-pick above
```

### Option B — Unattended

One pass; the first take of every prompt becomes its pick:

```bash
dndig generate characters/ locations/ scenes/ --auto-pick
```

dndig orders the run so every character and place is generated (and picked) before the scenes that use it. Review the results afterwards and replace any weak pick with Option A's commands.

## Fix or Replace an Image

```bash
dndig refine characters/sera-mourne.md "make the ink stains on her hands darker"   # edits the pick
dndig pick characters/sera-mourne.md --take N                                # approve the new take
dndig generate characters/sera-mourne.md --takes 3                           # or start over
```

After a character or location changes, regenerate the scenes that use it:

```bash
grep -l "sera-mourne" scenes/*.md      # scenes with it in cast: or references:
dndig generate scenes/the-parlay.md
dndig pick scenes/the-parlay.md --take N
```

`dndig generate` always adds new takes, even when a prompt already has a pick, so pass single files to fill in or redo specific images rather than whole folders.

## Tidy Up

```bash
dndig prune characters/ locations/ scenes/          # unpicked takes → discards/
dndig prune characters/ locations/ scenes/ --delete # or delete them
```

## Troubleshooting

| Message | Fix |
|---------|-----|
| `<title> has no approved image yet` | A cast member or reference has no pick: `dndig pick <its file> --take N`, then re-run the remaining prompts |
| `title "x" is used by both …` | Titles must be unique across all of `art/`; rename one prompt (file and `title:`) |
| `unknown field` | Only dndig's frontmatter fields are allowed; see the lorewright dndig reference |
| `no prompt files found` | Remove that folder from the command |
| `… exists but …/pick.json does not say which take it is` | An image sits at the pick path without a `pick.json` (e.g. imported art); move it away and pick again |
