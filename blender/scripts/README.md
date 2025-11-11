# Blender Scripts

This directory contains Blender Python scripts for automation and scene setup.

## Purpose

- Automate repetitive tasks in Blender
- Scene generation scripts
- Asset import/export scripts
- Batch processing

## Running Scripts

### From Blender UI
1. Open Blender
2. Switch to Scripting workspace
3. Open script file
4. Click "Run Script"

### From Command Line
```bash
blender --background --python script_name.py
```

### With a .blend File
```bash
blender your_scene.blend --background --python script_name.py
```

## Example Script

```python
"""example_setup.py - Example scene setup script"""
import bpy

def setup_scene():
    """Setup basic scene elements."""
    # Clear existing objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Add camera
    bpy.ops.object.camera_add(location=(0, -10, 5))
    
    # Add light
    bpy.ops.object.light_add(type='SUN', location=(0, 0, 10))

if __name__ == "__main__":
    setup_scene()
```
