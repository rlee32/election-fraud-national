#!/usr/bin/env python3

from matplotlib import pyplot as plt
import json
from typing import Dict
import numpy as np

ax = plt.subplot(111)

def plot_turnout(turnout: Dict[int, int], name: str):
    tt = list(turnout.items())
    tt = [(int(x[0]), x[1]) for x in tt]
    tt.sort()
    ax.plot([x[0] for x in tt], [x[1] for x in tt], label=name)

def plot_json(json_file: str, name: str):
    with open(json_file, 'r') as f:
        turnout = json.load(f)
        plot_turnout(turnout, name)

if __name__ == '__main__':
    plot_json('missouri.json', 'Missouri')
    ax.legend()
    plt.xlabel('Age')
    plt.ylabel('Normalized Turnout (votes / voters / statewide turnout)')
    plt.title('Normalized Turnout vs. Age')
    plt.show()



