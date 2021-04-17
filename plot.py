#!/usr/bin/env python3

from matplotlib import pyplot as plt
import json
from typing import Dict
import numpy as np

ax = plt.subplot(111)

MAX_AGE = 105

def plot_turnout(turnout: Dict[int, int], name: str):
    tt = list(turnout.items())
    tt = [(int(x[0]), x[1]) for x in tt if int(x[0]) <= MAX_AGE]
    tt.sort()
    ax.plot([x[0] for x in tt], [x[1] for x in tt], label=name)

def plot_json(json_file: str, name: str):
    with open(json_file, 'r') as f:
        turnout = json.load(f)
        plot_turnout(turnout, name)

if __name__ == '__main__':
    plot_json('missouri2020.json', 'Missouri')
    plot_json('pennsylvania2020.json', 'Pennsylvania')
    plot_json('ohio2020.json', 'Ohio')
    plot_json('oklahoma2020.json', 'Oklahoma')
    plot_json('north-carolina-2020.json', 'North Carolina')
    plot_json('idaho2020.json', 'Idaho')
    ax.legend()
    plt.xlabel('Age')
    plt.ylabel('Normalized Turnout (votes / voters / statewide turnout)')
    plt.title('Normalized Turnout vs. Age in the 2020 General Election')
    plt.show()



