#!/usr/bin/env python
import subprocess
subprocess.run(["C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe", 
                "-con", 
                "--debug-python", 
                "--python", 
                "script_cache/bln_import_cmds.py"])
