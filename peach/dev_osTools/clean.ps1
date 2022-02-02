Write-Host "Full Clean-up Debug Install"
Remove-Item -force -recurse E:\dev\peach_dev_projects\Peach\*  -exclude *.ini *.pconfig
Remove-Item -force -recurse E:\dev\peach_dev\peach\pHoudini\dev\packages\PeachPy\*
Remove-Item -force -recurse E:\dev\peach_dev\peach\pHoudini\dev\PeachEnv\python_panels\* -exclude 'default.pypanel'
Remove-Item -force -recurse E:\dev\peach_dev\peach\pHoudini\dev\packages\PeachAsset\python_panels\*