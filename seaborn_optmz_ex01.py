import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os


def visual(results: list) -> None:
    sns.histplot(results)

    plt.savefig('data_vis.png')


def compute_heavy(data):
    return [x * 2 for x in data]


results = compute_heavy(range(100000))
visual(results)