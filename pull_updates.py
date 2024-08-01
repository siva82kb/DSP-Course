
"""
Script to pull the latest course materials from the preparatory folders.
"""

import os
import sys
import pathlib
import glob


# Lecture notes folder
src_lec_dir = pathlib.Path('../../intro_to_dsp/lectures')
dest_lec_dir = pathlib.Path("lecture_slides")
dest_lec_dir.mkdir(exist_ok=True)
lec_dirs = glob.glob(str(src_lec_dir / '*-*'))
# Got through each folder and get the .pdf file
for lec in lec_dirs:
    lec_files = glob.glob(str(pathlib.Path(lec) / '*.pdf'))
    # Copy files to the destination lectures folder
    for lec_file in lec_files:
        os.system(f'cp {lec_file} {dest_lec_dir.as_posix()}')

# Assignment folder
src_lec_dir = pathlib.Path('../../intro_to_dsp/assignment')
dest_lec_dir = pathlib.Path("assignments")
dest_lec_dir.mkdir(exist_ok=True)
lec_dirs = glob.glob(str(src_lec_dir / '*-*'))
# Got through each folder and get the .pdf file
for lec in lec_dirs:
    lec_files = glob.glob(str(pathlib.Path(lec) / '*.pdf'))
    # Copy files to the destination lectures folder
    for lec_file in lec_files:
        os.system(f'cp {lec_file} {dest_lec_dir.as_posix()}')

# Notes folder


# # Miscellaneous folder