#!/bin/sh

powershell "./dev_osTools/clean.ps1"

cd ./.build
eval "mingw32-make install"