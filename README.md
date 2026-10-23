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

Lorewright writes each campaign's `art/` directory as a [dndig](https://github.com/mickume/dndig) project: a style directive, one prompt file per NPC, location and scene, and an `art/README.md` with the commands to generate every image. dndig keeps characters consistent across scenes by sending each approved portrait along as a reference image.

Requires Go 1.26+ and a [Google Gemini API key](https://aistudio.google.com/apikey):

```bash
git clone https://github.com/mickume/dndig.git
cd dndig && make install          # installs ~/go/bin/dndig
export GEMINI_API_KEY=...
```

Then generate a campaign's art from its `art/` directory:

```bash
cd campaigns/my-campaign/art
dndig status                                              # what there is to generate
dndig generate characters/ locations/ scenes/ --auto-pick # everything, in dependency order
```

See the campaign's `art/README.md` for the curated workflow (choosing the best take of each portrait before scenes reuse it), and the [dndig repo](https://github.com/mickume/dndig) for full documentation.
