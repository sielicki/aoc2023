#!/usr/bin/env nix-shell
#! nix-shell -i python3.11 -p python311

import pathlib
import operator
import itertools
import collections

THIS_FILE = pathlib.Path(__file__)
THIS_DAY = pathlib.Path(__file__).stem
CODE_DIR = THIS_FILE.parents[0]
INPUTS_DIR = CODE_DIR / ".." / "inputs"
THIS_INPUT = INPUTS_DIR / pathlib.Path(THIS_DAY).with_suffix(".txt")

with THIS_INPUT.open('r') as f:
    print(f.readlines())
