# Campaign Creation Workflow

This workflow guides you through creating a complete D&D campaign from initial concept to ready-to-play content.

---

## Phase 1: Gathering Requirements

### Step 1: Collect Basic Information

**If the DM provides a briefing document**, extract:
- Game system (D&D 5e, Daggerheart, Pathfinder 2e, etc.)
- Story or plot hook
- Campaign length (one-shot, short arc, long campaign)
- Starting level and number of players
- World backdrop (classic D&D, custom, sci-fi, etc.)
- Tone and vibe
- Source material to adapt (if any — see [literary-adaptation.md](../modules/literary-adaptation.md))

**If no briefing is provided**, or the briefing is missing critical information, use AskUserQuestion to gather:

```
Questions to ask:
1. What game system are you using?
   - D&D 5e (2014 or 2024 revision)
   - Daggerheart
   - Pathfinder 2e
   - Other (specify)

2. What's your core concept or story idea?
   - Epic quest to stop an evil
   - Political intrigue
   - Dungeon crawl
   - Exploration-focused
   - Mystery investigation

3. How long should this campaign be?
   - One-shot (single session)
   - Short (3-5 sessions)
   - Medium (6-12 sessions)
   - Long (13+ sessions)

4. What's the player starting level and party size?
   - Level range depends on system
   - Party size: typically 3-6 players

5. What's the setting/backdrop?
   - Published setting (Forgotten Realms, Golarion, etc.)
   - Homebrew fantasy world
   - Sci-fi or modern
   - Other

6. What's the tone?
   - Heroic & epic
   - Dark & serious
   - Humorous & lighthearted
   - Mystery & intrigue
   - Horror
   - Adult-themed/NSFW
```

The game system determines stat block format, encounter math, skill/ability references, and mechanical terminology used throughout the campaign. All generated content should be consistent with the chosen system's conventions.

**Use TaskCreate** to create a planning checklist:
- [ ] Gather requirements
- [ ] Read reference materials (if `references/` directory exists)
- [ ] Complete research checklist ([campaign-research-checklist.md](../checklists/campaign-research-checklist.md))
- [ ] Choose campaign type
- [ ] Create campaign overview
- [ ] Refine campaign concept with author (1-2 iterations)
- [ ] Design chapters
- [ ] Create a timeline of events in the chapters
- [ ] Detail NPCs
- [ ] Detail locations
- [ ] Create factions
- [ ] Write briefing document
- [ ] Create image prompts and generate art with dndig
- [ ] Quality check

### Step 1b: Read Reference Materials

If the campaign has a `references/` directory, read its contents before proceeding:

- **Markdown files (`.md`):** Read in full — these contain setting lore, house rules, pantheon details, and other grounding context that should inform all content creation
- **PDF files (`.pdf`):** Note what's available. Read specific page ranges on demand during later phases when precise rules, stat blocks, or lore details are needed (up to 20 pages per request)

This step ensures all generated content is consistent with the DM's chosen setting, rules, and lore.

### Step 2: Choose Campaign Type

Based on requirements, recommend a campaign type (see [modules/campaign-types.md](../modules/campaign-types.md)):

**For new DMs or tightly plotted stories:** Linear
**For experienced DMs or exploration:** Sandbox/Hub
**For political/time-sensitive plots:** Event-Based
**For dungeon crawls or mystery:** Setting-Based

**Ask the DM** if unsure which type fits best.

---

## Phase 2: Campaign Framework

### Step 2b: Create Campaign Directory Structure

Before writing any files, create the campaign directory structure:

```bash
mkdir -p campaigns/[campaign-name]/{references,art/images,changelog}
```

This creates:
```
campaigns/[campaign-name]/
├── references/       # Lore and rules reference materials (.md, .pdf)
├── art/
│   └── images/       # Generated images (dndig output)
└── changelog/        # Documented changes
```

Campaign files (`campaign-overview.md`, chapters, `npcs.md`, etc.) are written directly into the campaign root as they are created in subsequent steps.

### Step 3: Create Campaign Overview

Using [templates/campaign-overview.md](../templates/campaign-overview.md):

**3.1: Write Adventure Background**
- What happened before the campaign starts?
- What forces are in motion?
- What's the core conflict?

**3.2: Write Adventure Synopsis**
- High-level overview of the story
- Major story beats (Chapter 1, Chapter 2, Chapter 3)
- Key decision points

**3.3: Create Adventure Hooks**
- Primary hook that pulls characters in
- 2-3 alternate hooks for different character motivations
- Connection to broader world (if applicable)

**3.4: Plan Chapter Breakdown**
- How many chapters needed?
- What's the focus of each chapter?
- What level should characters be?

**Examples:**
- One-shot: 1 chapter, 4-6 hours
- Short campaign: 3-5 chapters
- Medium campaign: 6-12 chapters
- Long campaign: 13+ chapters

**3.5: Identify Key Elements**
- Major NPCs (at least 3-5)
- Key locations (at least 3-5)
- Factions (optional, but recommended for complexity)

### Step 4: Design Story Framework

Following [modules/world-building.md](../modules/world-building.md):

**4.1: Establish the Setting**
- Define boundaries (don't build the entire world)
- Create structured creative space
- Establish tone clearly

**4.2: Plan Major NPCs**
- Create 3-5 major NPCs:
  - At least one ally/quest giver
  - At least one antagonist/villain
  - Supporting characters

**4.3: Design Key Locations**
- Create 3-5 major locations:
  - Starting location
  - At least one dungeon/challenge location
  - Climax location
  - Supporting locations

**4.4: Develop Factions (optional)**
- For complex campaigns, create 2-4 factions
- Define their goals and conflicts
- Show how they interact with each other

---

## Phase 2b: Creative Refinement

Before investing time in detailed chapter writing, pause and present the campaign concept back to the author for collaborative refinement. This phase ensures the author's vision is fully captured and that the creative foundation is solid before building on it.

**Run 1-2 refinement iterations.** Each iteration follows the same structure: present, discuss, revise.

### Step 4b: Present the Campaign Concept

Summarize what has been established so far in a clear, concise pitch:

- **Setting & Tone** — the world, era, and atmosphere in a few sentences
- **Central Conflict** — what drives the story; the core tension
- **Plot Arc** — the major story beats from hook to climax to resolution
- **Key NPCs** — the 3-5 most important characters: who they are, what they want, and why they matter
- **Narrative Themes** — what the campaign is really *about* beneath the adventure
- **Player Experience** — what the players will *feel* and *do* at the table; the kinds of choices they'll face

Frame this as a conversation, not a deliverable. The goal is to surface assumptions and invite the author to push back, redirect, or expand.

### Step 4c: Solicit Focused Feedback

Use AskUserQuestion to guide the discussion. Ask about areas where author input matters most:

```
Refinement questions (adapt to what's relevant):

1. Does this plot arc feel right? Any beats you'd shift, cut, or add?
2. Do these NPCs land? Anyone missing — a rival, mentor, wildcard?
3. Is the tone what you had in mind, or should we push it darker / lighter / weirder?
4. Are there themes or narrative threads you want woven in?
5. Anything that feels off, generic, or not quite *yours*?
```

Don't ask all of these at once — pick 2-3 that matter most given what was just presented.

### Step 4d: Revise the Framework

Based on the author's feedback:

1. Update `campaign-overview.md` with any changes to plot, NPCs, setting, or tone
2. Revise `chapters-summary.md` if the story structure shifted
3. Adjust NPC concepts, faction dynamics, or location plans as needed
4. Note any new constraints or creative direction the author introduced

### Step 4e: Confirm and Move Forward

After 1-2 iterations, confirm alignment before proceeding:

```
Confirmation question:
"Are you happy with the overall direction — setting, plot, characters, tone —
or is there anything else you'd like to adjust before we start writing the
detailed chapters?"
```

Only proceed to Phase 3 once the author confirms they're satisfied with the creative foundation. If the author raises new concerns, do another refinement pass.

---

## Phase 3: Detailed Development

### Step 5: Write Chapters

For each chapter, using [templates/chapter-template.md](../templates/chapter-template.md):

**5.1: Chapter Overview**
- Synopsis
- Objectives (primary, secondary, optional)
- Expected duration
- Time of the events in the chapter

**5.2: Break Into Scenes**
- Each chapter should have 3-5 scenes
- Follow the Session Arc for pacing (see [session-pacing.md](../modules/session-pacing.md)): Cold Open → Rising Action → Climax → Falling Action → Cliffhanger
- Each scene should have:
  - Read-aloud description (follow [creative-voice.md](../modules/creative-voice.md) guidelines)
  - DM information
  - Possible player actions
  - Encounters or challenges
  - Connections to other scenes

**5.3: Design Encounters**
- Follow [encounter-design.md](../modules/encounter-design.md) for each encounter
- Use the Encounter Design Checklist (dramatic question, stakes, environment, approaches, escalation, connection)
- Track variety with the Encounter Variety Matrix
- Match difficulty to party level
- Provide multiple solutions

**5.4: Create Scene Climax**
- Each chapter should build to a meaningful moment
- Multiple resolution paths (combat, diplomacy, stealth)
- Consequences that matter

**5.5: Add Transitions**
- How does this chapter lead to the next?
- What hooks or cliffhangers set up future content?

**Pacing guideline:**
- 1 hour per scene
- 3-5 scenes per session
- Budget time for roleplay and player creativity

### Step 6: Detail NPCs

Using [templates/npcs.md](../templates/npcs.md):

**6.1: Major NPCs** (3-5)
- Full details: appearance, personality, motivations, secrets
- Stat blocks
- Roleplaying tips
- How they evolve through the campaign

**6.2: Supporting NPCs** (5-10)
- Condensed format
- Key information and quirks
- What they know and want

**6.3: Minor NPCs** (as needed)
- Quick reference table
- One memorable trait each

### Step 7: Detail Locations

Using [templates/locations.md](../templates/locations.md):

**7.1: Major Locations** (3-5)
- Full details: atmosphere, history, key features
- Sub-locations within
- NPCs present
- Secrets and encounters

**7.2: Supporting Locations** (5-10)
- Quick format
- Essential information
- What players can do there

**7.3: Travel & Maps**
- How locations connect
- Travel times
- Random encounters

### Step 8: Detail Factions (if applicable)

Using [templates/factions.md](../templates/factions.md):

**8.1: Create 2-4 Factions**
- Goals and motivations
- Leadership and structure
- Resources and activities
- Relationships with other factions

**8.2: Define Faction Dynamics**
- Conflicts between factions
- How party can influence them
- Quests and rewards

---

## Phase 4: Player-Facing Content

### Step 9: Write Briefing Document

Using [templates/README.md](../templates/README.md):

**9.1: Campaign Overview**
- Spoiler-free description
- Essential information (level, length, tone)

**9.2: Setting Information**
- What characters living in this world would know
- Recent events
- Common knowledge

**9.3: Character Creation Guidelines**
- Allowed content
- Ability score method
- Character concept guidance

**9.4: Session Zero Topics**
- Table rules
- Content warnings and boundaries
- Safety tools
- Playstyle preferences

**IMPORTANT:** No spoilers! Only include information players should know before starting.

---

## Phase 5: Polish & Enhancement

### Step 10: Create Image Prompts

For key locations, NPCs, and scenes. See [dndig-reference.md](../modules/dndig-reference.md) for full tool documentation.

**10.1: Create Campaign Style File**
- Create `art/campaign-style.md` with visual style instructions for consistency across all artwork
- Reference this file from every prompt's `instructions` field

**10.2: Identify Visual Moments**
- Major NPCs
- Opening scenes
- Important locations
- Climactic encounters

**10.3: Write Prompts (NPCs First)**

All prompt files use a numbered prefix (`01_`, `02_`, etc.). **NPCs are always numbered first** so their portraits are generated before any scene or encounter. When a later prompt features a previously generated NPC, add the NPC's image path to `references` in the frontmatter for visual continuity.

- Create NPC portrait prompts first (`01_npc-name.md`, `02_npc-name.md`, ...)
- Then locations (`03_location-name.md`, ...)
- Then encounters/scenes — reference generated NPC images when applicable
- Base on read-aloud descriptions
- Include style guidance, composition, lighting, mood
- Use appropriate aspect ratios per content type (see dndig reference)

**NPC portrait format:**
```markdown
---
title: captain-harrow
aspect_ratio: "2:3"
resolution: 2K
instructions: campaign-style.md
---

Detailed visual description of the NPC...
```

**Scene/encounter format (referencing NPC):**
```markdown
---
title: ambush-at-the-docks
aspect_ratio: "16:9"
resolution: 2K
instructions: campaign-style.md
references:
  - images/captain-harrow_20240315_143022_1.png
---

Captain Harrow stands at the edge of the pier, cutlass drawn...
```

**10.4: Generate Images**
```bash
# All prompts in the art directory (NPCs processed first due to numbering)
dndig campaigns/[campaign-name]/art/

# Or a single prompt
dndig campaigns/[campaign-name]/art/[prompt-file].md
```

**10.5: Insert Image References into Content**

After generating images, go back through the campaign documents and ensure every generated image is embedded at the right place. This step closes the loop between art creation and campaign content.

For each art prompt file:
1. Identify the corresponding location in the campaign text (chapter, npcs.md, or locations.md)
2. Insert or update the `![Alt Text](art/images/filename.png)` reference using the actual generated filename
3. Follow the placement rules from [formatting-conventions.md](../modules/formatting-conventions.md#image-integration):
   - **NPC portraits** → after the appearance description in `npcs.md`
   - **Scene/location images** → after the read-aloud text in the chapter or `locations.md`
   - **Encounter images** → after the encounter intro in the chapter
   - **Maps** → in the map section of the location

**10.6: Verify Image Integration**

Cross-check that:
- Every art prompt file (excluding `campaign-style.md`) has at least one `![...](art/images/...)` reference in the campaign content
- Every `![...](art/images/...)` reference in chapters, npcs.md, and locations.md has a corresponding art prompt in `art/`
- All image paths point to files that exist in `art/images/`

### Step 11: Add Supporting Materials

**11.1: Handouts** (optional)
- Letters, clues, maps players find
- In-world documents

**11.2: Custom Content** (optional)
- Magic items
- Monster stat blocks
- Homebrew rules

**11.3: Random Tables** (optional)
- Random encounters
- Random NPCs
- Treasure tables

Using [templates/timeline.md](../templates/timeline.md):

**11.4: Timeline**
- Sequential timeline of events in the campaign, ordered by chapter and scene
- List of important events and their time the DM should know about

---

## Phase 6: Quality Assurance

### Step 12: Quality Check

Use [checklists/campaign-quality-checklist.md](../checklists/campaign-quality-checklist.md):

**12.1: Completeness Check**
- All chapters written
- All NPCs detailed
- All locations described
- Briefing document complete

**12.2: Consistency Check**
- Names consistent throughout
- Timeline makes sense
- NPCs and locations appear where stated
- Cross-references correct

**12.3: Balance Check**
- Encounters appropriate for level
- Variety in challenge types
- Pacing feels right

**12.4: Story Check**
- Clear hooks and motivations
- Multiple resolution paths
- Player agency preserved
- Consequences matter

### Step 13: Final Review

**13.1: Read-Through**
- Read the entire campaign as a DM would use it
- Check for clarity and usability at the table

**13.2: Cross-References**
- Ensure all links between documents work
- Check all references to other sections

**13.3: DM Notes**
- Add any missing tips or guidance
- Include common pitfalls and solutions

**13.4: Timeline**
- Verify the timeline and update timeline.md if there are inconsistencies

---

## Phase 7: Delivery

### Step 14: Organize Files

Ensure proper structure:

```
campaigns/[campaign-name]/
├── campaign-overview.md
├── README.md
├── chapter-01.md
├── chapter-02.md
├── [additional chapters]
├── chapters-summary.md
├── npcs.md
├── locations.md
├── factions.md
├── references/                  # (optional) Lore and rules reference materials
│   ├── *.md
│   └── *.pdf
├── art/
│   ├── 01_[npc-name].md
│   ├── 02_[scene-name].md
│   ├── campaign-style.md
│   └── images/
│       └── [generated-images.jpg]
└── [optional additional files]
```

### Step 15: Summary

Provide the DM with:
- Location of all files
- Overview of what was created
- Recommended next steps
- How to use the campaign

---

## Tips for Efficient Workflow

### Time Management

**Phase 1-2 (Framework):** 20% of time
- Get this right; everything builds on it

**Phase 3 (Details):** 50% of time
- Most labor-intensive
- Can be done incrementally

**Phase 4-5 (Polish):** 20% of time
- Don't skip this; makes campaign usable

**Phase 6-7 (QA & Delivery):** 10% of time
- Final touches matter

### Iterative Development

**Don't try to perfect everything at once:**
1. Complete framework (Phases 1-2)
2. Refine the concept with the author (Phase 2b) — get alignment on setting, plot, NPCs, and tone before writing details
3. Write first chapter in detail
4. Get DM feedback on chapter style and depth
5. Adjust approach for remaining chapters
6. Detail remaining chapters
7. Polish and quality check

### Use Todo List

Track progress with TaskCreate:
```
[ ] Requirements gathered
[ ] Campaign type chosen
[ ] Campaign overview complete
[ ] Chapter 1 complete
[ ] Chapter 2 complete
[...continue for all chapters]
[ ] NPCs detailed
[ ] Locations detailed
[ ] Factions detailed
[ ] Briefing written
[ ] Quality check passed
```

### Ask Questions

Don't hesitate to use AskUserQuestion when:
- Requirements are unclear
- Multiple valid approaches exist
- DM preference matters
- Ambiguity in the story

### Stay Focused

**Do:**
- Follow the templates
- Maintain consistency
- Think about usability at the table
- Provide multiple solutions

**Don't:**
- Over-detail minor NPCs or locations
- Write railroad plots
- Create content that will never be used
- Forget player agency
