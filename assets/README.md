# Assets

This directory contains all game assets organized by type.

## Directory Structure

- `models/` - 3D models (.obj, .fbx, .dae, .gltf, etc.)
- `textures/` - Texture images (.png, .jpg, .exr, etc.)
- `sounds/` - Audio files (.wav, .ogg, .mp3, etc.)
- `data/` - Data files (JSON, CSV, configuration files, etc.)

## Asset Guidelines

### 3D Models
- Use appropriate polygon counts
- Ensure proper UV unwrapping
- Apply scale and rotation before exporting
- Include both high-poly and low-poly versions if needed

### Textures
- Use power-of-2 dimensions when possible (512, 1024, 2048, etc.)
- Use appropriate formats:
  - PNG for textures with transparency
  - JPEG for diffuse maps
  - EXR for HDR images
- Organize by material or object

### Sounds
- Use appropriate sample rates (44.1kHz or 48kHz)
- Compress to OGG for in-game audio
- Keep uncompressed WAV files as source

### Data Files
- Use JSON for configuration
- Use CSV for tabular data
- Document data schemas

## Asset Naming

Use descriptive, lowercase names with underscores:
- `player_ship_model.fbx`
- `metal_texture_diffuse.png`
- `explosion_sound.ogg`
- `level_config.json`
