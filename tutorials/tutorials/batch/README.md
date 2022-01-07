# Batch 


### `Demo 1`: Run Program
Some simple example on how to open programs in Batch. Example1: Open `VSCode` with project dir using batch file.
Unlike the shell script, batch has to specify the program.exe dir to run. In this case, leave the first `""` as empty, follow the structure:

> <sub>format: </sub>

|`START` `""` `"<the_program.exe>"` `<path>\.`|
|:---|

> <sub>`.bat` example: open `vscode` of my document dir</sub>

```BAT
START "" "C:\Users\1\AppData\Local\Programs\Microsoft VS Code\Code.exe" E:\dev\peach_dev\docs\.
```