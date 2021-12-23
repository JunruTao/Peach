# +++ Before Loading the ps script, run:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

$generator = "MinGW Makefiles"

function Do-CMakeD{
	# cmake debug function	
	& "cmake.exe" '-G' $generator '-DCMAKE_BUILD_TYPE=Debug' ".."
}

function Do-CMakeR{
	# cmake release function
	& "cmake.exe" '-G' $generator '-DCMAKE_BUILD_TYPE=Release' ".."
}

function Do-MinGwMake{
	# MinGW-Makefiles
	& "mingw32-make"
}

function Do-MinGwMakeInstall{
	# MinGW-Makefiles
	& "mingw32-make" 'install'
}

Set-Alias cmaked Do-CMakeD
Set-Alias cmaker Do-CMakeR
Set-Alias mm Do-MinGwMake
Set-Alias mmi Do-MinGwMakeInstall