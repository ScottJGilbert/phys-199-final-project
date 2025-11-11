# Quantum Orbitals Game - PHYS 199 Final Project

My final project: a hybrid quantum computing, orbitals, and art video game for my PHYS 199 CHP class.

## Overview

This project combines quantum mechanics, orbital physics, and interactive visualization using Python, Blender, and UPBGE (Blender Game Engine).

## Project Structure

```
phys-199-final-project/
├── src/                    # Source code
│   ├── python_logic/       # Core Python logic (quantum mechanics, physics)
│   ├── blender_interface/  # Blender bpy API interfaces
│   └── upbge_interface/    # UPBGE game engine interfaces
├── blender/                # Blender-specific files
│   ├── scenes/             # Blender scene files (.blend)
│   └── scripts/            # Blender Python scripts
├── upbge/                  # UPBGE-specific files
│   ├── game_logic/         # Game logic scripts
│   └── components/         # Reusable game components
├── assets/                 # Game assets
│   ├── models/             # 3D models
│   ├── textures/           # Texture files
│   ├── sounds/             # Audio files
│   └── data/               # Data files
├── tests/                  # Test files
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Quick Start

### Prerequisites

1. **Blender** (version 3.0+): [Download here](https://www.blender.org/)
2. **UPBGE**: [Download here](https://upbge.org/)
3. **Python** 3.8+ (typically bundled with Blender/UPBGE)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ScottJGilbert/phys-199-final-project.git
   cd phys-199-final-project
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: `bpy` and `bge` modules are bundled with Blender/UPBGE.

### Development

- **Python Logic**: Develop standalone Python modules in `src/python_logic/`
- **Blender Scenes**: Create and edit scenes in `blender/scenes/`
- **UPBGE Scripts**: Write game logic in `upbge/game_logic/`
- **Assets**: Store all game assets in `assets/`

### Testing

Run tests with pytest:
```bash
pytest tests/
```

With coverage:
```bash
pytest --cov=src tests/
```

### Code Quality

Format code:
```bash
black src/ tests/
```

Lint code:
```bash
pylint src/
```

Type check:
```bash
mypy src/
```

## Documentation

See [docs/STRUCTURE.md](docs/STRUCTURE.md) for detailed documentation about the project structure and development workflow.

Each directory contains its own README with specific guidelines:
- [src/python_logic/README.md](src/python_logic/README.md)
- [src/blender_interface/README.md](src/blender_interface/README.md)
- [src/upbge_interface/README.md](src/upbge_interface/README.md)
- [blender/scenes/README.md](blender/scenes/README.md)
- [blender/scripts/README.md](blender/scripts/README.md)
- [upbge/game_logic/README.md](upbge/game_logic/README.md)
- [upbge/components/README.md](upbge/components/README.md)
- [assets/README.md](assets/README.md)
- [tests/README.md](tests/README.md)

## Features (To Be Implemented)

- Quantum mechanics simulations
- Orbital physics visualization
- Interactive 3D gameplay
- Educational content about quantum computing
- Artistic visualization of quantum states

## License

[Add license information]

## Contact

Scott J Gilbert - PHYS 199 CHP
