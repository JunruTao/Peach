#!/bin/sh

powershell "./dev_osTools/clean.ps1"

# gather HDA:
echo "[CMD] Gather All WIP hda, select latest and install in {dev package}/otls folders"
echo "execute python script..."
python './pHoudini/dev/scripts/hda_gathering.py'

python ./dev_osTools/cmake_configlive/cmake_config_build_all.py
python ./dev_changeLogs/scripts/changelog_version_up.py
# Build:
cd ./.build
# cmake debug
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Debug ..
# make install
eval "mingw32-make install"