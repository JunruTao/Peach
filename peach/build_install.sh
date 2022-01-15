#!/bin/sh

# Make and Install

# gather HDA:
# [ disabled ] this script does not collect HDAs
# Build:

cd ./.build
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Debug ..
eval "mingw32-make install"