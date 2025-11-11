"""
Example reusable component for UPBGE.

This demonstrates a reusable, object-oriented component that can be attached
to multiple game objects.
"""

try:
    import bge
    from mathutils import Vector
except ImportError:
    print("Error: This script requires UPBGE/Blender environment")
    exit(1)


class CameraFollow:
    """
    Camera follow component.
    
    Makes the owner object (camera) follow a target object smoothly.
    """
    
    def __init__(self, owner, target_name: str, offset: Vector = None, smoothness: float = 0.1):
        """
        Initialize the camera follow component.
        
        Args:
            owner: The camera game object
            target_name: Name of the object to follow
            offset: Position offset from target (default: (0, -5, 2))
            smoothness: How smooth the follow is (0-1, lower = smoother)
        """
        self.owner = owner
        self.target_name = target_name
        self.offset = offset if offset else Vector((0, -5, 2))
        self.smoothness = smoothness
        self.target = None
    
    def find_target(self):
        """Find the target object by name."""
        scene = bge.logic.getCurrentScene()
        for obj in scene.objects:
            if obj.name == self.target_name:
                self.target = obj
                return True
        return False
    
    def update(self):
        """
        Update camera position (call this each frame).
        """
        # Find target if not yet found
        if not self.target:
            if not self.find_target():
                return
        
        # Calculate desired position
        desired_pos = self.target.worldPosition + self.offset
        
        # Smooth interpolation
        current_pos = self.owner.worldPosition
        new_pos = current_pos.lerp(desired_pos, self.smoothness)
        
        self.owner.worldPosition = new_pos
        
        # Make camera look at target
        direction = self.target.worldPosition - self.owner.worldPosition
        self.owner.alignAxisToVect(direction, 2)  # Align Z-axis


# Global instance (persistent across frames)
camera_follow_instance = None


def main():
    """Main function called by UPBGE controller."""
    global camera_follow_instance
    
    controller = bge.logic.getCurrentController()
    owner = controller.owner
    
    # Initialize on first call
    if camera_follow_instance is None:
        # Change "Player" to your target object name
        camera_follow_instance = CameraFollow(owner, "Player")
        print("Camera follow component initialized")
    
    # Update each frame
    camera_follow_instance.update()


if __name__ == "__main__":
    main()
