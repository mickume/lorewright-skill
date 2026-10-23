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
- Insert an image reference immediately after the read-aloud text, pointing at the pick dndig will produce: `![Alt Text](art/scenes/images/<title>.jpg)`. The path is fixed by the prompt's folder and title, so it is correct before the image exists.

**Art Prompts**
- The campaign's `art/` directory is a [dndig](modules/dndig-reference.md) project: `dndig.yaml`, `.gitignore`, `README.md` (from [templates/art-README.md](templates/art-README.md)) and `styles/campaign.md` at its root
- One markdown file per subject, in a folder per kind: `characters/`, `locations/`, `scenes/`, and optionally `items/` and `maps/`
- File name = `title`, lowercase kebab-case, unique across all of `art/`; no numeric prefixes (dndig orders runs by dependency)
- A scene lists the characters in it under `cast:` and the places it reuses under `references:` (by title), so their approved portraits travel with it as reference images
- **Every art prompt must be referenced** by at least one `![...](art/<folder>/images/<title>.jpg)` embed in the campaign content (chapters, npcs.md, or locations.md)
- **Every image embed in content must have a matching art prompt** — no image references without a corresponding prompt file

```markdown
---
title: ambush-at-the-docks  # = file name (scenes/ambush-at-the-docks.md); unique in art/
kind: scene                 # character | scene | location | item | other
aspect_ratio: "16:9"        # see dndig-reference.md
resolution: 2K              # 1K, 2K, 4K
takes: 2                    # candidates to choose from
cast: [captain-harrow]      # character titles whose picks keep faces consistent
references: [harbor-district]  # other prompt titles or image files
---

Your detailed and verbose description, it has to inspire the player's imagination, based on the description created for the DM. Name the cast and describe what they do, not what they look like.
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

Campaign documents should be richly cross-linked to support navigation in both raw markdown and HTML/PDF/ebook exports. Follow these rules:

**First-mention rule:** In each chapter, link the first mention of every named NPC to `npcs.md#anchor`, every named location to `locations.md#anchor`, and every faction to `factions.md#anchor`. Subsequent mentions in the same chapter do not need links.

**Metadata fields:** "First Appearance", "Location", and "Relationships" fields in `npcs.md`, `locations.md`, and `factions.md` should always be links to the target document and anchor.

**Scene transitions:** "Connections" sections at the end of each scene should link to the target scene or chapter (e.g., `[Scene 2](#scene-2-ambush-in-thornwood)` or `[Chapter 2](chapter-02.md)`).

**Tables:** NPC and location names in overview tables (campaign-overview.md, factions.md, locations.md) should link to their detailed entries.

**Read-aloud text:** Do not add links inside blockquote (`>`) read-aloud text — keep it clean for the DM to read aloud.

See [formatting-conventions.md](modules/formatting-conventions.md#cross-references-and-navigation) for the complete linking reference.
