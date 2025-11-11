# Getting Started with the Quantum Orbitals Game

This guide will help you set up your development environment and start working on the project.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Development Workflow](#development-workflow)
5. [Testing](#testing)
6. [Common Tasks](#common-tasks)

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Python 3.8+**
   - Download from [python.org](https://www.python.org/)
   - Verify: `python --version`

2. **Blender 3.0+**
   - Download from [blender.org](https://www.blender.org/)
   - Verify: Open Blender and check Help > About Blender

3. **UPBGE 0.3+**
   - Download from [upbge.org](https://upbge.org/)
   - UPBGE is a fork of Blender with game engine capabilities

4. **Git**
   - Download from [git-scm.com](https://git-scm.com/)
   - Verify: `git --version`

### Optional but Recommended

- **Visual Studio Code** or your preferred IDE
- **Git GUI client** (e.g., GitHub Desktop, GitKraken)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ScottJGilbert/phys-199-final-project.git
cd phys-199-final-project
```

### 2. Set Up Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
# Install main dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### 4. Verify Installation

```bash
# Run tests to verify setup
pytest

# Check code formatting
black --check src/ tests/

# Run type checker
mypy src/
```

## Project Structure

```
phys-199-final-project/
├── src/                    # Source code
│   ├── python_logic/       # Core Python logic
│   ├── blender_interface/  # Blender API interfaces
│   └── upbge_interface/    # UPBGE interfaces
├── blender/                # Blender files
│   ├── scenes/             # .blend scene files
│   └── scripts/            # Blender automation scripts
├── upbge/                  # UPBGE scripts
│   ├── game_logic/         # Game logic
│   └── components/         # Reusable components
├── assets/                 # Game assets
├── tests/                  # Test files
└── docs/                   # Documentation
```

See [STRUCTURE.md](STRUCTURE.md) for detailed documentation.

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Develop Your Feature

- Write code in appropriate directories
- Follow the existing code style
- Add docstrings to functions and classes
- Use type hints where appropriate

### 3. Write Tests

```bash
# Create test file in tests/unit/ or tests/integration/
# Run your tests
pytest tests/unit/test_your_feature.py -v
```

### 4. Format and Lint

```bash
# Format code
black src/ tests/

# Lint code
pylint src/

# Type check
mypy src/
```

### 5. Commit and Push

```bash
git add .
git commit -m "Add feature: description of your feature"
git push origin feature/your-feature-name
```

### 6. Create Pull Request

Open a pull request on GitHub for review.

## Testing

### Run All Tests

```bash
pytest
```

### Run Specific Tests

```bash
# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/

# Run specific test file
pytest tests/unit/test_example_template.py

# Run specific test function
pytest tests/unit/test_example_template.py::TestExampleClass::test_initialization
```

### Run with Coverage

```bash
pytest --cov=src tests/
```

### Generate Coverage Report

```bash
pytest --cov=src --cov-report=html tests/
# Open htmlcov/index.html in browser
```

## Common Tasks

### Working with Blender Scripts

#### Run a Blender Script

```bash
# With GUI
blender --python blender/scripts/example_scene_setup.py

# Background (no GUI)
blender --background --python blender/scripts/example_scene_setup.py

# With a specific .blend file
blender blender/scenes/your_scene.blend --python blender/scripts/your_script.py
```

### Working with UPBGE

1. Open UPBGE
2. Load a .blend file from `blender/scenes/`
3. Open the Logic Editor (Shift + F2)
4. Attach Python controllers to game objects
5. Select scripts from `upbge/game_logic/` or `upbge/components/`
6. Press P to start the game

### Adding New Python Modules

1. Create your module in appropriate directory:
   - `src/python_logic/` for core logic
   - `src/blender_interface/` for Blender integration
   - `src/upbge_interface/` for UPBGE integration

2. Follow the template structure (see `example_template.py`)

3. Write tests in `tests/unit/` or `tests/integration/`

4. Update `__init__.py` if needed

### Adding Dependencies

1. Add to `requirements.txt` (main dependencies)
2. Or add to `requirements-dev.txt` (development only)
3. Install: `pip install -r requirements.txt`
4. Commit the updated requirements file

## Troubleshooting

### bpy Module Not Found

- `bpy` is only available inside Blender
- To use `bpy` outside Blender, try `pip install bpy` (limited functionality)
- For full functionality, run scripts inside Blender

### bge Module Not Found

- `bge` is only available inside UPBGE
- Scripts using `bge` must be run within UPBGE game engine

### Tests Failing

- Ensure virtual environment is activated
- Ensure all dependencies are installed
- Check that you're running from project root directory

### Import Errors

- Make sure you're running from project root
- Python may need to find the `src/` directory:
  ```bash
  export PYTHONPATH="${PYTHONPATH}:$(pwd)"
  ```

## Next Steps

1. Read the full [STRUCTURE.md](STRUCTURE.md) documentation
2. Explore example files in each directory
3. Review existing tests to understand testing patterns
4. Start implementing your features!

## Resources

- [Blender Python API Documentation](https://docs.blender.org/api/current/)
- [UPBGE Documentation](https://upbge.org/docs/)
- [Python Testing with pytest](https://docs.pytest.org/)
- [Quantum Computing with Qiskit](https://qiskit.org/documentation/)

## Getting Help

- Check the `docs/` directory for additional documentation
- Review example files for patterns and best practices
- Open an issue on GitHub for bugs or questions
