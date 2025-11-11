"""
Example template for a Python logic module.

This is a placeholder showing how to structure Python modules in this project.
"""

# Type hints for better code quality
from typing import Optional, List


class ExampleClass:
    """
    Example class demonstrating structure and documentation.
    
    This class serves as a template for creating new modules in the python_logic package.
    """
    
    def __init__(self, name: str):
        """
        Initialize the example class.
        
        Args:
            name: The name of this example instance
        """
        self.name = name
        self._internal_state: Optional[dict] = None
    
    def example_method(self, value: float) -> float:
        """
        Example method showing proper documentation.
        
        Args:
            value: Input value to process
            
        Returns:
            Processed value
            
        Raises:
            ValueError: If value is negative
        """
        if value < 0:
            raise ValueError("Value must be non-negative")
        return value * 2.0
    
    def __repr__(self) -> str:
        """String representation of the object."""
        return f"ExampleClass(name='{self.name}')"


def example_function(data: List[float]) -> float:
    """
    Example standalone function.
    
    Args:
        data: List of values to process
        
    Returns:
        Average of the values
    """
    if not data:
        return 0.0
    return sum(data) / len(data)


# This allows the module to be run directly for testing
if __name__ == "__main__":
    # Example usage
    example = ExampleClass("test")
    print(example)
    print(f"Example method result: {example.example_method(5.0)}")
    print(f"Example function result: {example_function([1.0, 2.0, 3.0])}")
