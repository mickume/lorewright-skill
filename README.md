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

## Art generation with dndig

Lorewright creates image prompts for campaign artwork (NPC portraits, scenes, maps). To generate the actual images, install [dndig](https://github.com/mickume/dndig):

```bash
pipx install dndig
```

Then point it at a campaign's art directory:

```bash
dndig campaigns/my-campaign/art/
```

See the [dndig repo](https://github.com/mickume/dndig) for full documentation.
