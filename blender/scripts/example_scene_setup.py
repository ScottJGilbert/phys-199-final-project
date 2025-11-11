"""
Example Blender automation script.

This script demonstrates how to automate tasks in Blender using Python.
Run this script inside Blender or from command line:
    blender --background --python example_scene_setup.py
"""

try:
    import bpy
except ImportError:
    print("Error: This script must be run inside Blender")
    exit(1)


def clear_scene():
    """Remove all objects from the current scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    print("Scene cleared")


def setup_basic_scene():
    """
    Setup a basic scene with camera, light, and a reference object.
    
    This is a template for creating initial game scenes.
    """
    # Clear existing scene
    clear_scene()
    
    # Add camera
    bpy.ops.object.camera_add(location=(7, -7, 5))
    camera = bpy.context.active_object
    camera.rotation_euler = (1.1, 0, 0.785)
    print(f"Added camera: {camera.name}")
    
    # Set as active camera
    bpy.context.scene.camera = camera
    
    # Add sun light
    bpy.ops.object.light_add(type='SUN', location=(0, 0, 10))
    light = bpy.context.active_object
    light.data.energy = 2.0
    print(f"Added light: {light.name}")
    
    # Add a reference cube
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
    cube = bpy.context.active_object
    cube.name = "ReferenceCube"
    print(f"Added reference object: {cube.name}")
    
    # Add ground plane
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, -1), size=10)
    plane = bpy.context.active_object
    plane.name = "Ground"
    print(f"Added ground: {plane.name}")
    
    print("Basic scene setup complete")


def save_scene(filepath: str):
    """
    Save the current scene to a file.
    
    Args:
        filepath: Path where to save the .blend file
    """
    bpy.ops.wm.save_as_mainfile(filepath=filepath)
    print(f"Scene saved to: {filepath}")


if __name__ == "__main__":
    print("=== Blender Scene Setup Script ===")
    print(f"Blender version: {bpy.app.version_string}")
    
    # Setup the scene
    setup_basic_scene()
    
    # Optionally save (uncomment to use)
    # save_scene("/path/to/your/scene.blend")
    
    print("=== Script Complete ===")
