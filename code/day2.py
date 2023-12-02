#!/usr/bin/env nix-shell
#! nix-shell -i python3.11 -p python311

import pathlib
import operator
import itertools
import collections
from collections import defaultdict
import math

THIS_FILE = pathlib.Path(__file__)
THIS_DAY = pathlib.Path(__file__).stem
CODE_DIR = THIS_FILE.parents[0]
INPUTS_DIR = CODE_DIR / ".." / "inputs"
THIS_INPUT = INPUTS_DIR / pathlib.Path(THIS_DAY).with_suffix(".txt")

def valid_game(d):
    mapping = { "red": 12, "blue": 14, "green": 13, }
    return all(all(v <= mapping[k] for v in vs) for k, vs in d.items())

def minimal_game(d):
    return {k: max(v) for k, v in d.items()}

def game_power(d):
    return math.prod(d.values())

filter_digits = lambda s: "".join(x for x in s if x.isdigit()).strip()
filter_alpha = lambda s: "".join(x for x in s if not x.isdigit()).strip()

with THIS_INPUT.open('r') as f:
    ds = defaultdict(lambda: defaultdict(list))
    for line in [x.strip() for x in f.readlines()]:
        game_index, rest = line.split(":")
        game_index = int(filter_digits(game_index))
        for game in rest.split(";"):
            colors = [x.strip() for x in game.split(",")]
            for color in colors:
                count = int(filter_digits(color))
                color = filter_alpha(color)
                ds[game_index][color].append(count)

    print("Part 1: ", sum(k for k, v in ds.items() if valid_game(v)))
    print("Part 2: ", sum(game_power(minimal_game(v)) for v in ds.values()))
