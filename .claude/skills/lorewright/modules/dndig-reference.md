# dndig — AI Image Generation Tool

`dndig` is a command-line tool for generating AI images using Google's Gemini API. It takes markdown prompt files with YAML frontmatter and produces high-quality images for campaign illustrations, character portraits, scene art, and maps.

**Location:** `dndig` (relative to the lorewright project root)

---

## CLI Usage

```bash
dndig <prompt_file> [options]
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-o, --output-dir DIR` | Output directory for generated images | `artwork` |
| `-w, --workers N` | Maximum concurrent workers for batch | `4` |
| `-v, --verbose` | Enable verbose output with progress bar | off |
| `--debug` | Enable debug logging (most verbose) | off |
| `--api-key KEY` | API key (overrides `GEMINI_API_KEY` env var) | from env |
| `--version` | Show version and exit | — |

### Requirements

- Python 3.13+
- `GEMINI_API_KEY` environment variable (or use `--api-key`)
- `google-genai` and `tqdm` packages (installed with dndig)

---

## Prompt File Format

Prompt files are Markdown with YAML frontmatter. Place them in the campaign's `art/` directory.

```markdown
---
title: throne-room
aspect_ratio: "16:9"
resolution: 2K
temperature: 0.9
batch: 2
instructions: campaign-style.md
references:
  - assets/gothic-castle-ref.jpg
  - assets/dark-lighting-ref.png
---

A vast throne room carved from obsidian, its vaulted ceiling lost in shadow.
Rows of massive columns rise like petrified trees, their surfaces etched with
scenes of ancient conquest. A single shaft of pale moonlight falls through a
shattered dome onto an empty throne of black iron. The floor is cracked marble
veined with something that glows faintly red. The air feels heavy, expectant.
Style: dark fantasy, painterly, dramatic lighting, high detail.
```

### Frontmatter Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `title` | string | `generated_image` | Output filename prefix (required for meaningful names) |
| `aspect_ratio` | string | `1:1` | Image aspect ratio |
| `resolution` | string | `1K` | Output resolution |
| `temperature` | float | `1.0` | Creativity level (0.0 = deterministic, 1.0 = most creative) |
| `batch` | int | `1` | Number of images to generate per call (1–4) |
| `instructions` | string | — | Path to system style instructions file (relative to prompt file) |
| `references` | list | — | List of reference image paths (relative to prompt file, max 14) |

### Aspect Ratios

| Value | Use Case |
|-------|----------|
| `1:1` | Character portraits, tokens, icons |
| `2:3` | Portrait orientation character art |
| `3:2` | Landscape scenes, wide environments |
| `3:4` | Tall scenes, tower interiors, vertical compositions |
| `4:3` | Classic scene composition, location art |
| `4:5` | Near-square portraits with slight vertical emphasis |
| `5:4` | Near-square landscapes with slight horizontal emphasis |
| `9:16` | Tall vertical: maps, full-body character sheets, tower exteriors |
| `16:9` | Wide panoramic: landscapes, battle maps, establishing shots |
| `21:9` | Ultra-wide: panoramic vistas, banner art |

### Resolutions

| Value | Pixels | Use Case |
|-------|--------|----------|
| `512px` | 512px | Quick drafts, thumbnails, iteration |
| `1K` | 1024px | Standard quality, web use, VTT tokens |
| `2K` | 2048px | High quality prints, detailed art |
| `4K` | 4096px | Maximum quality, large prints, splash art |

---

## Key Features

### System Instructions (Style Consistency)

Create a style instructions file for visual consistency across an entire campaign. Reference it from every prompt file.

**Example: `art/campaign-style.md`**
```markdown
Dark fantasy illustration style. Muted earth tones with selective color
accents in crimson and gold. Painterly brushwork, dramatic chiaroscuro
lighting. Reminiscent of classic fantasy book cover art. Characters should
have realistic proportions. Architecture should feel weathered and ancient.
No anime or cartoon styles.
```

Then reference it in prompt frontmatter:
```yaml
instructions: campaign-style.md
```

### Reference Images (Style Grounding)

Provide up to 14 reference images to ground the generated output in a specific visual style, character appearance, or environmental feel.

**Use cases:**
- Maintain consistent character appearance across multiple scenes
- Establish architectural style from real-world references
- Match a specific art style from existing illustrations

```yaml
references:
  - refs/character-face.jpg
  - refs/castle-style.png
  - refs/color-palette.jpg
```

### Batch Generation

Generate multiple variations of the same prompt in a single call (1–4 images). Useful for exploring different interpretations of a scene or generating options for the DM to choose from.

```yaml
batch: 4
temperature: 1.0
```

Higher temperature with multiple batches gives more variety. Lower temperature gives more consistent results.

---

## Output

### Generated Files

Images are saved to the output directory (default: `artwork/`):
- **Images:** `{title}_{timestamp}_{index}.{ext}` (e.g., `throne-room_20240315_143022_1.png`)
- **Metadata:** `{title}_{timestamp}_metadata.json` (generation parameters and file paths)

### Example Workflow

```bash
# Generate a single location image
dndig campaigns/my-campaign/art/throne-room.md

# Generate all art for a campaign (batch)
for f in campaigns/my-campaign/art/*.md; do dndig "$f" -o campaigns/my-campaign/art/ -v; done

# Generate quick drafts at low resolution
dndig art/npc-villain.md -o drafts/ -v
```

---

## Campaign Art Integration

When creating image prompts for a campaign, follow this pattern:

1. **Create a style instructions file** (`art/campaign-style.md`) to maintain visual consistency
2. **Base prompts on read-aloud text** — the scene description written for DM use doubles as the foundation for the image prompt
3. **Add visual specifics** the DM text might not include: composition, lighting direction, color palette, art style, camera angle
4. **Use consistent frontmatter** across the campaign — same instructions file, similar resolution, appropriate aspect ratios per content type

### Recommended Aspect Ratios by Content Type

| Content | Aspect Ratio | Resolution |
|---------|-------------|------------|
| Character portraits | `2:3` or `3:4` | `2K` |
| Location scenes | `16:9` or `4:3` | `2K` |
| Battle maps | `1:1` or `4:3` | `2K` or `4K` |
| Panoramic vistas | `21:9` or `16:9` | `2K` |
| Item/artifact art | `1:1` | `1K` |
| Full-body character | `9:16` | `2K` |
