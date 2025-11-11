# UPBGE Game Logic

This directory contains the game logic scripts that run within UPBGE.

## Purpose

- Game mechanics implementation
- Player controls
- Game state management
- AI and NPC behavior

## Structure

Organize your game logic scripts here. They will be attached to game objects in UPBGE.

## Example Script

```python
"""example_controller.py - Example game object controller"""
import bge

def main():
    """Main game logic function."""
    controller = bge.logic.getCurrentController()
    owner = controller.owner
    
    # Your game logic here
    
if __name__ == "__main__":
    main()
```

## Attaching Scripts

1. Select a game object in UPBGE
2. Open the Logic Editor
3. Add a Python controller
4. Select your script file
5. Connect sensors and actuators
