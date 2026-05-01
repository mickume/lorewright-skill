# lorewright

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill for creating D&D campaigns, adventures, NPCs, encounters, and storylines tailored for tabletop play.

## Install

```bash
git clone https://github.com/mickume/lorewright-skill.git
cd lorewright-skill
make install
```

This symlinks the skill into `~/.claude/skills/` so it's available globally in Claude Code.

To remove it:

```bash
make uninstall
```

## Usage

In any Claude Code session, invoke the skill:

```
/lorewright
```

Then describe what you want to create — a full campaign, a one-shot adventure, a set of NPCs, encounter tables, etc. The skill guides the workflow with templates, checklists, and structured output.

## Static site generation with lorepages

Lorepages turns a campaign directory into a static HTML website you can host on GitHub Pages, Netlify, or open directly from the filesystem.

Requires Python 3.10+ and `uv`.

### Install

Install globally from this repo:

```bash
uv tool install git+https://github.com/mickume/lorewright-skill.git
```

Or install from a local clone:

```bash
cd lorewright-skill
uv tool install .
```

### Build a site

```bash
lorepages build campaigns/my-campaign/
```

This generates a complete static site at `campaigns/my-campaign/_site/`.

### Options

```
lorepages build <campaign-dir> [options]

  -o, --output-dir DIR    Output directory (default: <campaign-dir>/_site/)
  --mode {dm,player}      dm = full content (default), player = spoiler-free
  --theme THEME           Theme name or path to custom theme dir (default: parchment)
  --base-url URL          Base URL prefix for hosted deployments (default: relative)
  -v, --verbose           Show per-page build progress
```

### DM vs player builds

The default `dm` mode includes everything. The `player` mode strips all DM-only content (chapters, secrets, stat blocks, DM notes) and uses the player briefing as the landing page:

```bash
lorepages build campaigns/my-campaign/ --mode player -o campaigns/my-campaign/_site-player/
```

### Deploy to GitHub Pages

Set `--base-url` to your repo name when deploying to GitHub Pages under a subpath:

```bash
lorepages build campaigns/my-campaign/ --base-url /my-repo-name/
```

Push the output directory contents to your `gh-pages` branch or configure GitHub Pages to serve from it.

### Custom themes

The default `parchment` theme uses CSS custom properties for all colors, fonts, and spacing. To create a custom theme, make a directory containing a `theme.css` file and pass it:

```bash
lorepages build campaigns/my-campaign/ --theme /path/to/my-theme/
```

The theme directory can also include `fonts/` and `img/` subdirectories for self-hosted assets.

## Art generation with dndig

Lorewright creates image prompts for campaign artwork (NPC portraits, scenes, maps). To generate the actual images, install [dndig](https://github.com/mickume/dndig):

Requires Python 3.10+, `uv` and a [Google Gemini API key](https://aistudio.google.com/apikey).

Install directly from the repository:

```bash
uv tool install git+https://github.com/mickume/dndig.git
```

Then point it at a campaign's art directory:

```bash
dndig campaigns/my-campaign/art/
```

See the [dndig repo](https://github.com/mickume/dndig) for full documentation.
