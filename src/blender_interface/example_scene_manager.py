"""
Example Blender interface module.

This demonstrates how to structure modules that interface with Blender's bpy API.
"""

from typing import Optional, Tuple

# Try to import bpy, handle gracefully if not available
try:
    import bpy
    BPY_AVAILABLE = True
except ImportError:
    BPY_AVAILABLE = False
    print("Warning: bpy module not available. This module requires Blender.")


class BlenderSceneManager:
    """
    Example class for managing Blender scenes.
    
    This class demonstrates how to interface with Blender's API while handling
    cases where bpy is not available (for testing outside Blender).
    """
    
    def __init__(self):
        """Initialize the scene manager."""
        if not BPY_AVAILABLE:
            raise RuntimeError("Blender API (bpy) is not available")
        
        self.scene = None
    
    def setup_camera(self, location: Tuple[float, float, float] = (0, -10, 5)):
        """
        Setup a camera in the scene.
        
        Args:
            location: Camera position (x, y, z)
            
        Returns:
            Camera object if bpy is available, None otherwise
        """
        if not BPY_AVAILABLE:
            return None
        
        # Add camera
        bpy.ops.object.camera_add(location=location)
        camera = bpy.context.active_object
        return camera
    
    def get_scene(self):
        """
        Get the current Blender scene.
        
        Returns:
            Current scene object
        """
        if not BPY_AVAILABLE:
            return None
        return bpy.context.scene


def check_blender_version() -> Optional[str]:
    """
    Check the Blender version.
    
    Returns:
        Version string if bpy is available, None otherwise
    """
    if not BPY_AVAILABLE:
        return None
    return bpy.app.version_string


# Example usage when run as script in Blender
if __name__ == "__main__":
    if BPY_AVAILABLE:
        print(f"Blender version: {check_blender_version()}")
        manager = BlenderSceneManager()
        print("Blender interface initialized successfully")
    else:
        print("This script must be run inside Blender")
