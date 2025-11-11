"""
Example unit test file.

This demonstrates how to write unit tests for the python_logic modules.
"""

import pytest
from src.python_logic.example_template import ExampleClass, example_function


class TestExampleClass:
    """Test suite for ExampleClass."""
    
    def test_initialization(self):
        """Test that ExampleClass initializes correctly."""
        example = ExampleClass("test")
        assert example.name == "test"
        assert example._internal_state is None
    
    def test_example_method_positive(self):
        """Test example_method with positive value."""
        example = ExampleClass("test")
        result = example.example_method(5.0)
        assert result == 10.0
    
    def test_example_method_zero(self):
        """Test example_method with zero."""
        example = ExampleClass("test")
        result = example.example_method(0.0)
        assert result == 0.0
    
    def test_example_method_negative(self):
        """Test that example_method raises ValueError for negative input."""
        example = ExampleClass("test")
        with pytest.raises(ValueError, match="must be non-negative"):
            example.example_method(-1.0)
    
    def test_repr(self):
        """Test string representation."""
        example = ExampleClass("test")
        assert repr(example) == "ExampleClass(name='test')"


class TestExampleFunction:
    """Test suite for example_function."""
    
    def test_with_values(self):
        """Test function with normal values."""
        result = example_function([1.0, 2.0, 3.0])
        assert result == 2.0
    
    def test_with_empty_list(self):
        """Test function with empty list."""
        result = example_function([])
        assert result == 0.0
    
    def test_with_single_value(self):
        """Test function with single value."""
        result = example_function([5.0])
        assert result == 5.0


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
