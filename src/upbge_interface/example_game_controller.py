"""
Example UPBGE interface module.

This demonstrates how to structure modules that interface with UPBGE's bge API.
"""

from typing import Optional, Any

# Try to import bge, handle gracefully if not available
try:
    import bge
    BGE_AVAILABLE = True
except ImportError:
    BGE_AVAILABLE = False
    print("Warning: bge module not available. This module requires UPBGE.")


class GameObjectController:
    """
    Example controller for game objects in UPBGE.
    
    This class demonstrates how to interface with UPBGE's API while handling
    cases where bge is not available (for testing outside UPBGE).
    """
    
    def __init__(self):
        """Initialize the game object controller."""
        if not BGE_AVAILABLE:
            raise RuntimeError("UPBGE API (bge) is not available")
        
        self.controller = None
        self.owner = None
    
    def get_current_controller(self) -> Optional[Any]:
        """
        Get the current logic controller.
        
        Returns:
            Controller object if bge is available, None otherwise
        """
        if not BGE_AVAILABLE:
            return None
        return bge.logic.getCurrentController()
    
    def get_owner(self) -> Optional[Any]:
        """
        Get the owner object of the controller.
        
        Returns:
            Owner game object if bge is available, None otherwise
        """
        if not BGE_AVAILABLE:
            return None
        
        controller = self.get_current_controller()
        if controller:
            return controller.owner
        return None
    
    def move_object(self, velocity: tuple):
        """
        Move the owner object with given velocity.
        
        Args:
            velocity: (x, y, z) velocity tuple
        """
        if not BGE_AVAILABLE:
            return
        
        owner = self.get_owner()
        if owner:
            owner.worldLinearVelocity = velocity


def get_game_fps() -> Optional[float]:
    """
    Get the current game FPS.
    
    Returns:
        FPS value if bge is available, None otherwise
    """
    if not BGE_AVAILABLE:
        return None
    return bge.logic.getLogicTicRate()


# Example usage when run as script in UPBGE
if __name__ == "__main__":
    if BGE_AVAILABLE:
        fps = get_game_fps()
        print(f"Game running at: {fps} FPS")
        controller = GameObjectController()
        print("UPBGE interface initialized successfully")
    else:
        print("This script must be run inside UPBGE")
