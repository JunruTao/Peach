#!/bin/sh

# Make and Install

# gather HDA:
# [ disabled ] this script does not collect HDAs
# Build:


python ./dev_osTools/cmake_configlive/cmake_config_devlib_only_nv.py

cd ./.build
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Debug ..
eval "mingw32-make install"