# Blender Interface Module

This directory contains interfaces to Blender's `bpy` API.

## Purpose

- Interact with Blender's Python API (bpy)
- Scene setup and manipulation
- Rendering control
- Asset import/export

## Note

Code in this module requires Blender's `bpy` module, which is available when running scripts inside Blender or using `bpy-standalone`.

## Example Usage

```python
try:
    import bpy
    # Your Blender API code here
except ImportError:
    print("bpy not available. Run this script inside Blender.")
```

## Running Blender Scripts

From command line:
```bash
blender --background --python your_script.py
```

Or run interactively from Blender's scripting workspace.
