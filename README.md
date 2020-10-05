# OSUrecompress

Compress OSU! beatmaps or skins folders back to '.osz/.osk' files. 

Want to make the jump to OSU!Lazer but can't manually export your library of 1k+ beatmaps?

Here is the tool for you!

## Introduction

This script is mostly aimed towards Linux users who do not benefit from the "Import from stable" feature.

This script allows you to convert your beatmaps or skins back to the '.osz' and '.osk' file formats respectively that are recognized by OSU!

## Installation
1. Clone or download and extract the project  

1. `cd` into the project directory  

2. Allow the user to execute the script  
   `chmod u+x OSUrecompress.py` 

You can now run the script with `./OSUrecompress.py` while in the project directory.

## Usage
This script is meant to be used in the terminal followed by the arguments below:  

### Required  

`-b, --beatmaps`      
Items in the SOURCE folder will be converted to **beatmap** format (.osz)

`-s, --skins`      
Items in the SOURCE folder will be converted to **skin** format (.osk)

*Either `-b` or `-r` is needed, but they cannot be combined.*


`  --source SOURCE`  
Enter the path to the folder containing your uncompressed beatmaps or skins  
Example: `--source /path/to/osu/Songs/`

`--destination DESTINATION`  
Enter the path to the folder where you want your files to be saved  

### Optional

`-h, --help`      
Shows information about the program
  
`-R, --remove`  
Deletes the files in the SOURCE folder after compression to save space.  
**Please note that deletion through this option is irreversible.**
It is only there for people who wish to save space and not keep the files used by OSU!stable.

## Please Note
- The generated '.osz/osk' files can be opened by OSU!Stable and OSU!Lazer, but they will be deleted right after being processed by the game.  
  
- OSU!Lazer uses a binary-like file structure. Therefore, this script cannot be used to compress beatmaps from an OSU!Lazer folder.
