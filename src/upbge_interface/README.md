# UPBGE Interface Module

This directory contains interfaces to UPBGE (Blender Game Engine).

## Purpose

- Interface with UPBGE's `bge` module
- Game engine integration
- Real-time rendering management
- Input handling
- Game loop integration

## Note

Code in this module requires UPBGE's `bge` module, which is available when running inside UPBGE.

## Example Usage

```python
try:
    import bge
    # Your UPBGE code here
except ImportError:
    print("bge not available. Run this script inside UPBGE.")
```

## Running in UPBGE

1. Open your .blend file in UPBGE
2. Attach scripts to game objects via Logic Bricks
3. Press P to start the game engine
