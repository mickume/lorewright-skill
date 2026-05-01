# The Standard D&D Adventure Structure

Based on analyzing official D&D Beyond materials and Wizards of the Coast publications, here's the typical anatomy of a professional D&D adventure:

## FRONT MATTER

### Cover & Credits
- Title

### Table of Contents**
- Chapter breakdown
- Appendices
- Maps reference

### Introduction
- Adventure Background - establishes the story's foundation
- Target level range
- Expected playtime/session count
- Prerequisites (what books/materials needed)
- Recommended player characters: what race/class the campaign is best for

## CORE STRUCTURE

### Adventure Synopsis
- High-level overview of what might happen during the adventure, showing expected flow of encounters even if non-linear, highlighting important connectors between scenes
- Major story beats
- Key NPCs overview
- The "hook" that pulls characters into the adventure, which must be compelling or personal to the players and their characters

### Adventure Hooks
- Multiple ways to involve the party, using knowledge of players and their characters' goals to make compelling hooks
- Connection to broader campaign (if applicable)
- Alternate entry points

### Chapter Breakdown

Each chapter typically includes:

#### Location/Scene Description
- Read-aloud text for the DM. Be very detailled and verbose here, it has to inspire the player's imagination.
- Suggested dialog and read-out for interactions with NPCs.
- Suggest skill checks or saving throws (and their difficulties) to progress the story. List information that might revealed, based on the outcomes of checks.
- DM notes
- Image creation prompt, used with AI image creation tools (dndig)
- Scope considerations based on adventure level: high-level adventures need environmental challenges while low-level adventures shouldn't have environment as additional threat

#### Encounters
- Varied challenges that test adventurers differently - attack, defense, skill use, problem-solving, investigation, and roleplaying
- Combat encounters with stat blocks
- Social encounters
- Skill challenges
- Puzzles/traps

#### NPCs
- Description of the NPC if it is unique, i.e. not based on typical DnD 5e canon.
- Stat blocks or references to DnD canon (source books)
- Personality traits
- Motivations and goals
- Roleplay guidance


#### Treasure & Rewards
- Loot tables
- Magic items
- Experience points/milestone guidance

## CLIMAX & CONCLUSION

### Final Encounter/Climax
- The most fantastic and epic encounter in the adventure, with dramatically decisive moments when crucial knowledge or decisive action pays off
- Should be meaningful - players should care about what happens if they fail
- Multiple resolution paths
- Consequences of success/failure

### Resolution & Epilogue
- Wrap-up scenarios
- Campaign hooks for future adventures
- Character rewards and advancement

## BACK MATTER

### Appendices
- New monsters (full stat blocks)
- New magic items
- Handouts
- Random encounter tables
- NPC roster with page references


## FORMATTING CONVENTIONS

**Read-Aloud Text:**
- Very detailled and verbose description, it has inspire the player's imagination. It also serves as prompt for AI image generation.
- No hidden information players shouldn't know

**DM Notes:**
- Regular text
- Mechanical information
- Secret information
- Conditional outcomes

**Location/Scene Description**
- Very detailled and verbose description, it has inspire the player's imagination. It also serves as prompt for AI image generation.
- Insert an image reference (`![Alt Text](art/images/filename.png)`) immediately after the read-aloud text. Before generation, use the prompt's `title` as a placeholder filename; after generation, update to the actual filename.

**Art Prompts**
- An individual markdown file per subject (NPC, location, scene, encounter)
- All files use a numbered prefix: `01_name.md`, `02_name.md`, etc.
- **NPCs are always numbered first** so portraits are generated before scenes/encounters
- When a scene or encounter features a previously generated NPC, add the NPC's image path to `references` in the frontmatter for visual continuity
- **Every art prompt must be referenced** by at least one `![...](art/images/...)` embed in the campaign content (chapters, npcs.md, or locations.md)
- **Every image embed in content must have a matching art prompt** — no image references without a corresponding prompt file

```markdown
---
title: location             # Output filename prefix (required)
aspect_ratio: "4:3"         # Options: 16:9, 9:16, 1:1, 4:3, 3:4
resolution: 1K              # Options: 1K, 2K, 4K
instructions: [campaign]_instr.md  # Optional style instructions file
references:                 # Optional — include generated NPC images for continuity
  - images/npc-name_timestamp_1.png
---

Your detailled and verbose description, it has to inspire the player's imagination, based on the description created for the DM.
```

**Image Placement:**
- **NPC portraits:** after the appearance description in `npcs.md`
- **Scene/location images:** after the read-aloud text in chapters and/or `locations.md`
- **Encounter images:** after the encounter intro read-aloud text in chapters
- **Maps:** in the map section of the relevant location

**Maps**
- Very detailled and verbose description, it has inspire the player's imagination. It also serves as prompt for AI image generation.
- Use styled, Mermaid diagrams (flowchart LR) for visualization, if needed.
- Insert a placeholder link for a map image.

**Stat Blocks:**
- Standardized format
- Quick reference for combat
- Page references to DnDBeyond source books

**Sidebars:**
- Optional/Homebrew rules or content
- Variant encounters
- DM tips
- Historical/lore information

## Cross-Linking Conventions

Campaign documents should be richly cross-linked to support navigation in both raw markdown and HTML/PDF/ebook exports (via lorepages). Follow these rules:

**First-mention rule:** In each chapter, link the first mention of every named NPC to `npcs.md#anchor`, every named location to `locations.md#anchor`, and every faction to `factions.md#anchor`. Subsequent mentions in the same chapter do not need links.

**Metadata fields:** "First Appearance", "Location", and "Relationships" fields in `npcs.md`, `locations.md`, and `factions.md` should always be links to the target document and anchor.

**Scene transitions:** "Connections" sections at the end of each scene should link to the target scene or chapter (e.g., `[Scene 2](#scene-2-ambush-in-thornwood)` or `[Chapter 2](chapter-02.md)`).

**Tables:** NPC and location names in overview tables (campaign-overview.md, factions.md, locations.md) should link to their detailed entries.

**Read-aloud text:** Do not add links inside blockquote (`>`) read-aloud text — keep it clean for the DM to read aloud.

See [formatting-conventions.md](modules/formatting-conventions.md#cross-references-and-navigation) for the complete linking reference.
