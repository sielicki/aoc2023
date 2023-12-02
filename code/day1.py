#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python311

import pathlib
import operator

THIS_FILE = pathlib.Path(__file__)
THIS_DAY = pathlib.Path(__file__).stem
CODE_DIR = THIS_FILE.parents[0]
INPUTS_DIR = CODE_DIR / ".." / "inputs"
THIS_INPUT = INPUTS_DIR / pathlib.Path(THIS_DAY).with_suffix(".txt")

wordmap = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, }
digimap = { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, }
bothmap = {**digimap, **wordmap}

tot = 0
with THIS_INPUT.open('r') as f:
    for x in f.readlines():
        line = x.strip()
        findings = {idx: v for idx in range(len(line)+1) for k, v in bothmap.items() if line[idx:idx+len(k)] == k}
        tot += int(findings[min(findings.keys())]*10) + int(findings[max(findings.keys())])

print(tot)
