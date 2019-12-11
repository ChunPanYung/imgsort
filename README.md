# Imgsort
---
CLI Command use for sorting images


## Usage
>usage: main.py [--options] PATH [PATH...]

**PATH**: Needs to have at least 1 SOURCE directory(s) and only 1 DESTINATION directory.  If used with `--dry_run`, only needs SOURCE directory(s).

<br>

**Optional Arguments**

|Options        |Description                                                              |
|---------------|-------------------------------------------------------------------------|
|-v, --verbose  |print details information                                                |
|-r, --recursive|sort images in subdirectories                                            |
|-d, --dry_run  |print out summary of such execution, but no actual sorting takes in place|               
|-c, --copy     |copy images instead of moving images                                     |


## Update [Date Here]
Add verbose function

Add Dry_run function