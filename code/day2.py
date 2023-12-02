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

def valid_game(d):
    for k, vs in d.items():
        if k == 'red':
            if not all(v <= 12 for v in vs):
                return False
        if k == 'blue':
            if not all(v <= 14 for v in vs):
                return False
        if k == 'green':
            if not all(v <= 13 for v in vs):
                return False
    return True

def minimal_game(d):
    return {k: max(v) for k, v in d.items()}

def game_power(d):
    ret = 1
    for x in d.values():
        ret *= x
    return ret

with THIS_INPUT.open('r') as f:
    ds = collections.defaultdict(lambda: collections.defaultdict(list))
    for line in f.readlines():
        line = line.strip()
        game_index, rest = line.split(":")
        games = rest.split(";")
        for idx, game in enumerate(games):
            colors = game.split(",")
            for color in colors:
                if "red" in color:
                    ds[game_index]['red'].append(int("".join(x for x in color if x.isdigit())))
                elif "green" in color:
                    ds[game_index]['green'].append(int("".join(x for x in color if x.isdigit())))
                elif "blue" in color:
                    ds[game_index]['blue'].append(int("".join(x for x in color if x.isdigit())))

    print(sum(int(k.split(" ")[-1]) for k, v in ds.items() if valid_game(v)))

    print(sum(game_power(minimal_game(v)) for v in ds.values()))
