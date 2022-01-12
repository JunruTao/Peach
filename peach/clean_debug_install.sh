#!/bin/sh

powershell "./dev_osTools/clean.ps1"

cd ./.build

# cmake debug
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Debug ..
# make install
eval "mingw32-make install"