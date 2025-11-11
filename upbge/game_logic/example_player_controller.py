"""
Example UPBGE game logic script.

This script demonstrates basic game logic that can be attached to game objects in UPBGE.
To use:
1. Open your .blend file in UPBGE
2. Select a game object
3. Open Logic Editor
4. Add a Python controller
5. Select this script
6. Connect sensors and actuators as needed
"""

try:
    import bge
except ImportError:
    print("Error: This script must be run inside UPBGE")
    exit(1)


def main():
    """
    Main game logic function.
    
    This is called each frame when the Python controller is triggered.
    """
    # Get the controller that called this script
    controller = bge.logic.getCurrentController()
    
    # Get the game object this controller is attached to
    owner = controller.owner
    
    # Get sensors
    sensors = controller.sensors
    
    # Get actuators
    actuators = controller.actuators
    
    # Example: Check keyboard input
    keyboard = bge.logic.keyboard
    
    # Movement speed
    speed = 0.1
    
    # Example movement controls
    if bge.logic.KX_INPUT_ACTIVE == keyboard.inputs[bge.events.WKEY].status:
        # Move forward (negative Y in Blender)
        owner.worldPosition.y -= speed
    
    if bge.logic.KX_INPUT_ACTIVE == keyboard.inputs[bge.events.SKEY].status:
        # Move backward
        owner.worldPosition.y += speed
    
    if bge.logic.KX_INPUT_ACTIVE == keyboard.inputs[bge.events.AKEY].status:
        # Move left
        owner.worldPosition.x -= speed
    
    if bge.logic.KX_INPUT_ACTIVE == keyboard.inputs[bge.events.DKEY].status:
        # Move right
        owner.worldPosition.x += speed
    
    # Example: Print position (for debugging)
    # print(f"Position: {owner.worldPosition}")


# Entry point
if __name__ == "__main__":
    main()
