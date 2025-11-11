# Project Structure Documentation

## Overview

This project is a hybrid quantum computing and orbital physics video game built using Python, Blender, and UPBGE (Blender Game Engine).

## Directory Structure

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
│   └── data/               # Data files (JSON, CSV, etc.)
├── tests/                  # Test files
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── docs/                   # Additional documentation
├── requirements.txt        # Python dependencies
└── README.md               # Main project README
```

## Setup Instructions

### Prerequisites

1. **Blender**: Download and install Blender (version 3.0+) from [blender.org](https://www.blender.org/)
2. **UPBGE**: Download and install UPBGE from [upbge.org](https://upbge.org/)
3. **Python**: Python 3.8+ (typically bundled with Blender/UPBGE)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd phys-199-final-project
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: Some dependencies like `bpy` are bundled with Blender and may not be installable via pip.

### Running the Project

#### Using UPBGE
1. Open UPBGE
2. Load a scene from `blender/scenes/`
3. Run the game logic scripts from `upbge/game_logic/`

#### Running Python Logic Standalone
```bash
python -m src.python_logic
```

## Module Documentation

### src/python_logic/
Core Python logic independent of Blender/UPBGE. Contains:
- Quantum mechanics calculations
- Physics simulations
- Game state management

### src/blender_interface/
Interfaces with Blender's `bpy` API for:
- Scene setup and manipulation
- Rendering
- Asset management

### src/upbge_interface/
Interfaces with UPBGE's `bge` module for:
- Game engine integration
- Real-time rendering
- Input handling

### blender/
Blender-specific files:
- `scenes/`: .blend files containing game scenes
- `scripts/`: Python scripts for Blender automation

### upbge/
UPBGE-specific files:
- `game_logic/`: Game logic scripts executed by UPBGE
- `components/`: Reusable game components (player controller, camera, etc.)

### assets/
Game assets organized by type:
- `models/`: 3D models (.obj, .fbx, etc.)
- `textures/`: Image files for textures
- `sounds/`: Audio files
- `data/`: Configuration and data files

### tests/
Test suite:
- `unit/`: Unit tests for individual components
- `integration/`: Integration tests for system components

## Development Workflow

1. **Design**: Plan features and create documentation in `docs/`
2. **Implement**: Write Python logic in `src/`, create Blender scenes in `blender/`
3. **Test**: Write and run tests in `tests/`
4. **Integrate**: Connect Python logic with UPBGE in `upbge/`
5. **Iterate**: Refine and optimize

## Testing

Run tests using pytest:
```bash
pytest tests/
```

Run tests with coverage:
```bash
pytest --cov=src tests/
```

## Code Quality

Format code with black:
```bash
black src/ tests/
```

Lint code with pylint:
```bash
pylint src/
```

Type check with mypy:
```bash
mypy src/
```

## Contributing

1. Follow the existing directory structure
2. Keep modules modular and independent where possible
3. Write tests for new functionality
4. Document new features in `docs/`

## License

[Add license information]

## Contact

[Add contact information]
