# Tests

This directory contains the test suite for the project.

## Structure

- `unit/` - Unit tests for individual components
- `integration/` - Integration tests for system interactions

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/unit/test_example.py
```

### Run with coverage
```bash
pytest --cov=src tests/
```

### Run with verbose output
```bash
pytest -v
```

## Writing Tests

### Unit Tests

Place in `tests/unit/` and name files with `test_` prefix.

Example:
```python
"""test_quantum_state.py"""
import pytest
from src.python_logic.quantum_state import QuantumState

def test_quantum_state_initialization():
    """Test quantum state initialization."""
    state = QuantumState()
    assert state is not None

def test_quantum_state_superposition():
    """Test quantum superposition."""
    state = QuantumState()
    # Add your test logic
    pass
```

### Integration Tests

Place in `tests/integration/` for testing interactions between components.

Example:
```python
"""test_blender_integration.py"""
import pytest

def test_blender_scene_loading():
    """Test loading Blender scenes."""
    # Integration test logic
    pass
```

## Test Guidelines

1. Write tests for all new functionality
2. Aim for high code coverage (>80%)
3. Keep tests focused and independent
4. Use descriptive test names
5. Use fixtures for common setup
6. Mock external dependencies (Blender, UPBGE APIs)

## Mocking Blender/UPBGE

Since `bpy` and `bge` are not available outside their environments, mock them in tests:

```python
from unittest.mock import Mock, MagicMock

def test_with_mocked_bpy():
    """Test with mocked bpy."""
    import sys
    sys.modules['bpy'] = MagicMock()
    
    # Your test code here
```
