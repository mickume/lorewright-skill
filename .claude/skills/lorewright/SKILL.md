---
name: lorewright
description: A comprehensive DnD campaign and adventure creation skill for game masters and creative content creators. Helps design complete campaigns, adventures, NPCs, encounters, maps, and storylines tailored for tabletop play. Use this when designing D&D content, creating campaign worlds, developing adventure hooks, designing encounters, or building narrative structures for player tables.
---

# lorewright - DnD Campaign & Adventure Creator

lorewright is a specialized skill designed to assist Dungeon Masters and creative content creators in building complete, engaging Dungeons & Dragons campaigns and adventures.

---

## Quick Start

### For New Campaigns

1. **Use TaskCreate** immediately to create a planning checklist
2. **Create the directory structure** — run `mkdir -p campaigns/[name]/{references,art/images,changelog}` before writing any files
3. **Follow the workflow:** [workflows/campaign-creation-workflow.md](workflows/campaign-creation-workflow.md)
4. **Use AskUserQuestion** to gather requirements if not provided
5. **Use templates:** All templates are in [templates/](templates/)
6. **Quality check:** Use [checklists/campaign-quality-checklist.md](checklists/campaign-quality-checklist.md) when done

### For Updating Existing Campaigns

1. **Read existing content** before making changes
2. **Follow the iteration workflow:** [workflows/iteration-workflow.md](workflows/iteration-workflow.md)
3. **Check consistency:** Use [checklists/consistency-checklist.md](checklists/consistency-checklist.md)
4. **Use Edit tool** for targeted changes to existing files

### Need an Example?

See the complete sample campaign: [examples/the-stolen-flame/](examples/the-stolen-flame/)

---

## What lorewright Does

This skill helps you create:

- **Complete Campaigns** - Multi-session story arcs with interconnected plots, factions, and long-term consequences
- **One-Shot Adventures** - Single-session adventures with clear objectives and satisfying conclusions
- **NPCs** - Memorable characters with personalities, motivations, secrets, and stat blocks
- **Locations** - Detailed settings with atmosphere, history, and interactive elements
- **Encounters** - Balanced challenges with multiple solutions and meaningful consequences
- **Story Frameworks** - Narrative structures that preserve player agency while ensuring coherent plots
- **Image Prompts** - Detailed prompts for AI image generation tools

---

## Core Principles

### Creative Voice
- Write with evocative, atmospheric prose — lead with mood, not measurements (see [creative-voice.md](modules/creative-voice.md))
- Engage multiple senses in every scene description
- Give every NPC a want, a speech pattern, and an opinion
- Design encounters as drama engines, not math problems

### Player Agency First
- Always provide multiple solutions to problems
- Design consequences that matter and ripple forward
- Avoid railroading (forced single paths)
- Let player choices shape the story
- Character backstories are campaign fuel — weave them in

### Usability at the Table
- Write clear, scannable DM notes
- Provide concise read-aloud text
- Include quick reference tables
- Anticipate common DM needs

### Completeness and Consistency
- Cross-reference between documents
- Maintain timeline and logic
- Keep names and facts consistent
- Check dependencies when changing content

### Use the Right Tools
- **TaskCreate/TaskUpdate:** Track complex campaign creation tasks
- **AskUserQuestion:** Clarify requirements and gather preferences
- **Read:** Always read existing files before editing
- **Edit:** Make targeted changes to existing content
- **Write:** Create new files from templates
- **dndig:** Generate campaign artwork (see [dndig-reference.md](modules/dndig-reference.md))

---

## File Organization

Every campaign should follow this structure:

```
campaigns/[campaign-name]/
├── campaign-overview.md         # Master document with full campaign arc
└── changelog/                   # Changelogs
    └── [change-name].md         # Documented changes to the campaign
├── README.md                  # Player-facing session zero document (spoiler-free)
├── chapter-01.md                # Detailed session content
├── chapter-02.md                # Continue for each chapter/session
├── chapters-summary.md          # Chapter/Scene-level summaries for all chapters of the campaign
├── npcs.md                      # Important characters with stats and motivations
├── locations.md                 # Key places with descriptions
├── factions.md                  # Organizations and their goals (optional)
├── timeline.md                  # Timeline of events in the campaign (optional)
├── references/                  # Lore and rules reference materials
│   ├── *.md                     # Markdown summaries (setting, house rules, pantheon, etc.)
│   └── *.pdf                    # Source books, lore documents (read specific pages on demand)
└── art/                         # Image prompts and artwork
    ├── 01_[npc-name].md         # NPC portrait prompts (numbered first)
    ├── 02_[npc-name].md         # Additional NPC prompts
    ├── 03_[scene-name].md       # Scene/location prompts (numbered after NPCs)
    ├── campaign-style.md        # Style instructions file
    └── images/                  # Generated images (dndig output)
        └── [generated-images.jpg]
```

---

## Resource Library

### Templates
Use these as starting points for all campaign documents:

- **[campaign-overview.md](templates/campaign-overview.md)** - Master campaign document
- **[chapter-template.md](templates/chapter-template.md)** - Individual session structure
- **[chapters-summary.md](templates/chapters-summary.md)** - Scene-level overview for all chapters of the campaign
- **[timeline.md](templates/timeline.md)** - Timeline of events in the campaign
- **[README.md](templates/README.md)** - Player-facing session zero document
- **[npcs.md](templates/npcs.md)** - NPC roster and details
- **[locations.md](templates/locations.md)** - Location descriptions and maps
- **[factions.md](templates/factions.md)** - Organizations and politics

### Modules
Reference these for detailed guidance:

- **[creative-voice.md](modules/creative-voice.md)** - Creative identity, voice guidelines, writing philosophy
- **[campaign-types.md](modules/campaign-types.md)** - Linear, Sandbox, Event-Based, Setting-Based
- **[world-building.md](modules/world-building.md)** - Settings, NPCs, villain design, moral complexity, themes
- **[encounter-design.md](modules/encounter-design.md)** - Encounter philosophy, checklist, variety matrix, boss design
- **[session-pacing.md](modules/session-pacing.md)** - Session arc, dramatic structure, pacing tools
- **[literary-adaptation.md](modules/literary-adaptation.md)** - Adapting novels, films, mythology into campaigns
- **[formatting-conventions.md](modules/formatting-conventions.md)** - How to format all content
- **[dndig-reference.md](modules/dndig-reference.md)** - AI image generation tool reference

### Workflows
Step-by-step processes for different tasks:

- **[campaign-creation-workflow.md](workflows/campaign-creation-workflow.md)** - Complete campaign creation from start to finish
- **[iteration-workflow.md](workflows/iteration-workflow.md)** - Updating and refining existing campaigns

### Checklists
Quality assurance for your work:

- **[campaign-research-checklist.md](checklists/campaign-research-checklist.md)** - Pre-creation foundation and research checklist
- **[campaign-quality-checklist.md](checklists/campaign-quality-checklist.md)** - Ensure completeness, balance, and quality
- **[consistency-checklist.md](checklists/consistency-checklist.md)** - Maintain consistency when making changes

### Examples
Complete sample campaigns demonstrating all templates:

- **[The Stolen Flame](examples/the-stolen-flame/)** - One-shot adventure showing all templates in action

---

## Reference Materials

Campaigns can include a `references/` directory with lore, setting, and rules materials that ground the campaign in specific source content. Both markdown (`.md`) and PDF (`.pdf`) files are supported.

### Markdown references
Compact summaries of setting lore, house rules, pantheons, regional factions, or any background the campaign should draw from. These are read in full and provide the most reliable grounding for tone and consistency.

### PDF references
Source books, published adventures, or lore documents. PDFs are read on demand by specific page ranges (up to 20 pages per request). Use them for precise lookups — stat blocks, spell descriptions, setting details — rather than broad grounding.

### How to use references

1. **Place files in `campaigns/[campaign-name]/references/`**
2. **Read markdown references early** — during Phase 1 (requirements gathering) and Phase 2 (framework), read all `.md` reference files to absorb setting context, tone, and constraints
3. **Consult PDFs on demand** — when creating content that needs specific rules, stat blocks, or lore details, read the relevant pages from PDF references
4. **Cite sources** — when content is drawn from a reference, note the source in DM notes (e.g., "See PHB p. 157" or "Per setting-overview.md")

### Example references/ layout
```
references/
├── setting-overview.md          # World, geography, major powers
├── house-rules.md               # Table-specific rule modifications
├── pantheon.md                  # Gods, domains, worship practices
├── players-handbook.pdf         # Rules lookups (read specific pages)
└── sword-coast-guide.pdf        # Setting lore (read specific pages)
```

---

## Workflow Overview

### Creating a New Campaign

**Phase 1: Gather Requirements**
1. Use TaskCreate to build a planning checklist
2. Use AskUserQuestion if briefing incomplete
3. Collect: story idea, length, level, setting, tone
4. If adapting source material, follow [literary-adaptation.md](modules/literary-adaptation.md)
5. Complete [campaign-research-checklist.md](checklists/campaign-research-checklist.md)

**Phase 2: Campaign Framework** 
1. Choose campaign type (see [modules/campaign-types.md](modules/campaign-types.md))
2. Create campaign-overview.md (use [template](templates/campaign-overview.md))
3. Plan chapter breakdown with session pacing (see [session-pacing.md](modules/session-pacing.md))
4. Create chapters-summary.md (use [template](templates/chapters-summary.md))
5. Identify major NPCs and locations

**Phase 3: Detailed Development** 
1. Write each chapter using [creative-voice.md](modules/creative-voice.md) for writing quality
2. Design encounters using [encounter-design.md](modules/encounter-design.md) for variety and depth
3. Detail NPCs using tiered framework in [world-building.md](modules/world-building.md)
4. Detail locations (use [template](templates/locations.md))
5. Create factions if needed (use [template](templates/factions.md))

**Phase 4: Player-Facing Content** 
1. Write README.md (use [template](templates/README.md))
2. Ensure there are NO SPOILERS in the briefing

**Phase 5: Polish & QA** 
1. Create image prompts for key scenes using [dndig-reference.md](modules/dndig-reference.md)
2. Run through [campaign-quality-checklist.md](checklists/campaign-quality-checklist.md)
3. Read entire campaign for flow and consistency

**See detailed workflow:** [workflows/campaign-creation-workflow.md](workflows/campaign-creation-workflow.md)

### Updating an Existing Campaign

1. **Read** all affected files first
2. **Plan** changes and identify dependencies
3. **Edit** existing files with targeted changes
4. **Update** cross-references
5. **Check** consistency with [consistency-checklist.md](checklists/consistency-checklist.md)

**See detailed workflow:** [workflows/iteration-workflow.md](workflows/iteration-workflow.md)

---

## Important Guidelines

### Always Do This

**Use TaskCreate/TaskUpdate for Complex Tasks**
- Create planning checklist immediately with TaskCreate
- Track progress through creation phases
- Mark tasks completed with TaskUpdate as you finish them
- Keep exactly ONE task in_progress at a time

**Ask Questions When Needed**
- Use AskUserQuestion for unclear requirements
- Clarify tone, content boundaries, player preferences
- Ask about multiple valid approaches
- Don't guess—confirm with the DM

**Read Before Editing**
- Always Read existing files before using Edit
- Understand the full context
- Check dependencies and cross-references
- Maintain consistency with existing content

**Preserve Player Agency**
- Provide multiple solutions to every problem
- Design meaningful consequences
- Allow creative approaches
- Avoid forced single paths

**Follow Templates**
- Use the templates in [templates/](templates/)
- Maintain consistent formatting
- Include all required sections
- Match the style of examples

**Integrate All Artwork into Content**
- Every art prompt in `art/` must have a matching `![...](art/images/...)` reference in the campaign text
- Every image reference in chapters, npcs.md, or locations.md must have a matching art prompt
- Place NPC portraits after appearance descriptions, scene images after read-aloud text
- After running dndig, update image references to use actual generated filenames
- See [formatting-conventions.md](modules/formatting-conventions.md#image-integration) for placement rules

### Never Do This

**Don't Railroad Players**
- Never force a single solution
- Don't invalidate player choices
- Avoid "the NPC does everything" solutions

**Don't Skip Quality Checks**
- Always use checklists before completion
- Verify cross-references work
- Check name consistency
- Test story logic

**Don't Forget Documentation**
- Cross-reference between documents
- Link to related content
- Include DM notes and tips
- Provide stat blocks or references

**Don't Break Existing Content**
- When editing, maintain story logic
- Update all references to changed content
- Check timeline consistency
- Preserve what works

---

## Session Zero Considerations

Unless stated otherwise, campaigns are written for consenting adults. When content might be disturbing or NSFW:

- Include content warnings in README.md
- Suggest Session Zero discussion topics
- Recommend safety tools (X-Card, Lines & Veils)
- Clearly mark mature content

---

## Standard D&D Adventure Structure

The skill follows professional D&D adventure conventions (see [STRUCTURE.md](STRUCTURE.md) for full details):

**Front Matter:** Introduction, synopsis, hooks
**Core Structure:** Chapter breakdown with scenes, encounters, NPCs
**Climax:** Epic final encounter with multiple resolution paths
**Back Matter:** Appendices with stat blocks, magic items, handouts

**Each Chapter Includes:**
- Read-aloud text for scene setting
- DM information and secrets
- Encounter design (combat, social, skill challenges)
- NPCs with personality and stats
- Treasure and rewards
- Connections to other chapters

---

## Formatting Standards

Follow conventions in [modules/formatting-conventions.md](modules/formatting-conventions.md):

**Read-Aloud Text:**
```markdown
> Text the DM reads to players
> Detailed, evocative, multi-sensory
> Present tense, no secrets
```

**DM Notes:** Regular text with mechanical details, secrets, contingencies

**Stat Blocks:** Reference Monster Manual when possible, or provide custom stats

**Cross-References:** Link the first mention of every named NPC, location, and faction in each chapter to their entry in the roster document (e.g., `[Elder Mira](npcs.md#elder-mira-thorne)`). Link "First Appearance" and "Location" metadata fields in npcs.md and locations.md back to chapter anchors. See [formatting-conventions.md](modules/formatting-conventions.md#cross-references-and-navigation) for complete rules.

**Image Prompts:** Create in `art/` folder with proper metadata

---

## Quick Reference

### Campaign Types
- **Linear:** Sequential chapters, clear path (easiest to prep)
- **Sandbox:** Central hub, many options (most prep)
- **Event-Based:** Timeline of events, player actions affect outcomes
- **Setting-Based:** Location-focused, exploratory

See: [modules/campaign-types.md](modules/campaign-types.md)

### Encounter Design
- Every fight answers: *"Why is this fight happening, and what changes when it's over?"*
- Terrain is the third combatant — environment should force choices
- Give enemies goals beyond "kill the party" (escape, protect, buy time, capture)
- Use the Encounter Design Checklist: dramatic question, stakes, environment, multiple approaches, escalation, connection
- Track variety with the Encounter Variety Matrix (combat/social/exploration/hybrid subtypes)
- Boss fights need phases, legendary actions, emotional stakes, and multiple victory conditions

See: [modules/encounter-design.md](modules/encounter-design.md)

### NPC Design
- **Tier 1 (Walk-On):** One trait, one useful thing, a rememberable name
- **Tier 2 (Recurring):** Want vs. need, opinions about other NPCs, a secret, speech patterns
- **Tier 3 (Major):** Full inner life, independent arc, mechanical weight, voice, relationship web
- **Villains:** Motivation, Method, Vulnerability, Escalation, Mirror

See: [modules/world-building.md](modules/world-building.md), [templates/npcs.md](templates/npcs.md)

### Location Design
- Atmosphere (sights, sounds, smells, feel)
- History and current situation — use environmental storytelling
- NPCs present and encounters
- Secrets to discover — layered puzzles that reward curiosity

See: [modules/world-building.md](modules/world-building.md), [templates/locations.md](templates/locations.md)

---

## Tone and Content

**Adjust to DM's requested tone:**
- Heroic & Epic
- Dark & Serious
- Humorous & Lighthearted
- Mystery & Intrigue
- Horror
- Adult-themed/NSFW (with appropriate warnings)

**Always:**
- Match requested tone consistently
- Warn about mature content in briefing
- Provide Session Zero guidance for sensitive topics

---

## Image Generation with dndig

Use **dndig** (`dndig`) to generate campaign artwork from prompt files or an entire directory. See [dndig-reference.md](modules/dndig-reference.md) for complete documentation.

**Quick usage:**
```bash
# Single prompt file
dndig campaigns/my-campaign/art/throne-room.md

# All prompts in a directory
dndig campaigns/my-campaign/art/
```

**Prompt file format:**
```markdown
---
title: throne-room
aspect_ratio: "16:9"
resolution: 2K
temperature: 0.9
batch: 2
instructions: campaign-style.md
references:
  - refs/gothic-castle.jpg
---

Detailed visual description based on scene read-aloud text...
Include: composition, lighting, mood, style, atmosphere.
```

**Key features:**
- **Style consistency:** Create a shared `instructions` file for the campaign's visual style
- **Reference images:** Up to 14 reference images for style grounding (character consistency, architectural style)
- **Batch generation:** Generate 1–4 variations per prompt
- **Aspect ratios:** `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
- **Resolutions:** `512px`, `1K`, `2K`, `4K`

**Prompt naming and ordering:**

All art prompt files are numbered with a running prefix (`01_`, `02_`, etc.). **NPCs are always numbered first** so their portraits are generated before scenes and encounters. When a scene or encounter features a previously generated NPC, add the NPC's image path to `references` in the prompt frontmatter for visual continuity.

```
art/
├── 01_captain-harrow.md       # NPC — generated first
├── 02_sister-vael.md          # NPC
├── 03_harbor-district.md      # Location
├── 04_ambush-at-docks.md      # Encounter — references 01's image
└── images/                    # Generated images (dndig output)
```

**Create prompts for:**
- Important NPCs and character portraits (`2:3` or `3:4` at `2K`) — **always first**
- Key locations and scenes (`16:9` or `4:3` at `2K`)
- Climactic encounters (`16:9` at `2K`) — reference NPC images when applicable
- Maps and dungeons (`1:1` or `4:3` at `2K`+)
- Items and artifacts (`1:1` at `1K`)

---

## Examples in Action

### Example: Starting a New Campaign

```
DM: "I want to create a 3-session campaign about smugglers in a port city"

You:
1. TaskCreate: Create planning checklist
2. AskUserQuestion: Clarify tone, starting level, player count
3. Choose campaign type: Sandbox (city hub with multiple quest lines)
4. Create campaign-overview.md from template
5. Create 3 chapters, npcs.md, locations.md
6. Create README.md for players
7. Run quality checklist
8. Create image prompts and generate art with dndig
9. Deliver organized campaign
```

### Example: Updating Existing Campaign

```
DM: "The players killed the quest-giver NPC. I need to adapt."

You:
1. Read campaign-overview.md and affected chapters
2. Read npcs.md to understand the NPC's role
3. Follow iteration-workflow.md
4. Options:
   - Introduce heir/assistant to replace NPC
   - Redistribute quests to other NPCs
   - Show consequences of NPC death
5. Edit affected chapters
6. Update npcs.md and cross-references
7. Run consistency checklist
```

---

## Success Criteria

A campaign is ready when:

- [ ] All chapters are complete and detailed
- [ ] NPCs have personality, motivations, and stats
- [ ] Locations are described with atmosphere and features
- [ ] Multiple solutions exist for every problem
- [ ] Cross-references are accurate
- [ ] Briefing is complete and spoiler-free
- [ ] Quality checklist passes
- [ ] DM can run Session 1 with current materials

---

## Getting Help

**Stuck on something?**
- Check the relevant module in [modules/](modules/)
- Review the workflow in [workflows/](workflows/)
- Look at the example in [examples/the-stolen-flame/](examples/the-stolen-flame/)
- Use AskUserQuestion to clarify with the DM

**Need to verify quality?**
- [campaign-quality-checklist.md](checklists/campaign-quality-checklist.md)
- [consistency-checklist.md](checklists/consistency-checklist.md)

---

## Remember

You're helping a DM create memorable experiences for their players. Focus on:

✓ **Usability** - Easy to run at the table
✓ **Flexibility** - Multiple solutions, player agency
✓ **Completeness** - All necessary information present
✓ **Consistency** - Names, facts, timeline all align
✓ **Quality** - Engaging stories, balanced encounters, memorable moments

Good luck, and may your campaigns be legendary!
