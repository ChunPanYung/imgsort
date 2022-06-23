# Imgsort
---
CLI Command use for sorting images.  It will sort all images by size, moving from `SOURCE` to 
`DESTINATION` directory. It will create one or more subdirectories in `DESTINATION` directory,
name of subdirectories is indicated by the image size it will contain, ex: 1920x1080.

## Update [2020-08-18]
* Use PyInstaller to build single executable
* Update README.md to include Build Your Own Session

## Usage
>usage: imgsort [--options] PATH [PATH...]

**PATH**: Needs to have at least 1 SOURCE directory(s) and only 1 DESTINATION directory.  If used with `--summary`, only SOURCE directory(s) is needed.

<br>

**Optional Arguments**

|Options        |Description                                                              |
|---------------|-------------------------------------------------------------------------|
|-v, --verbose  |print details information                                                |
|-r, --recursive|sort images in subdirectories                                            |
|-s, --summary  |print out summary of such execution, but no actual sorting takes in place|               
|-c, --copy     |copy images instead of moving images                                     |
|-i, --include  |Only sort images with indicated size, ex: --include=1920x1080,1440x2560  |
|-e, --exclude  |exclude images of certain size, ex: --exclude=1920x1080,1440x2560        |

## Example
> imgsort -v `/home/user/SOURCE/*` `/home/user/DESTINATION`

Move and sort all the images in folder `SOURCE`, excluding subdirectories, and moving
them to `/home/user/DESTINATION`.  `-v` indicates it will print out details information on screen.

> imgsort --include=1920x1080,1440x2560 --recursive  --copy /home/user/unsorted_imgs /home/user/sorted

Copy only images with size of 1920x1080 and 1440x2560 from `/home/user/SOURCE` to
`/home/user/DESTINATION`, it will also open directory in `SOURCE` folder and search any qualified images.

> imgsort -e 1920x1080,1440x2560 -sr /home/user/SOURCE

print summary images (numbers and total size), grouped by image size, excluding 1920x1080 and 1440x2560.  It will also open directory in `SOURCE` folder and search any qualified images.

## System Requirement
* Python 3.10.*
* Pillow 9.1.1
* PyInstaller 5.1 (for compile into single executable)

## Build Your Own
1. Download and install Miniconda or Anaconda
2. create new environment from environment.yml file: 
> conda env create -f environment.yml
3. Use Pyinstaller to compile into single executables
> pyinstaller --clean --onefile --name imgsort main.py
