#!/bin/sh

# Make and Install

# gather HDA:
echo "[CMD] Gather All WIP hda, select latest and install in {dev package}/otls folders"
echo "execute python script..."
python './pHoudini/dev/scripts/hda_gathering.py'


# Build:

cd ./.build
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Debug ..
eval "mingw32-make install"