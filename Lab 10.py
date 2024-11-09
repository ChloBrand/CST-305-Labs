# Lab 10
# Chloe Brandow

import numpy as np
import matplotlib.pyplot as plt
import random

num_blocks = 100
num_files = 5
fragmentation_rate = 0.3


def generate_fragmented_layout(num_blocks, num_files, fragmentation_rate):
    layout = np.zeros(num_blocks, dtype=int)
    file_blocks = num_blocks // num_files
    file_ids = np.arange(1, num_files + 1)

    for file_id in file_ids:
        contiguous_blocks = int(file_blocks * (1 - fragmentation_rate))
        fragmented_blocks = file_blocks - contiguous_blocks

        start_index = random.randint(0, num_blocks - contiguous_blocks)
        for i in range(contiguous_blocks):
            layout[(start_index + i) % num_blocks] = file_id

        for _ in range(fragmented_blocks):
            while True:
                index = random.randint(0, num_blocks - 1)
                if layout[index] == 0:
                    layout[index] = -file_id
                    break

    return layout


low_fragmentation_layout = generate_fragmented_layout(num_blocks, num_files, 0.1)
high_fragmentation_layout = generate_fragmented_layout(num_blocks, num_files, 0.5)


def visualize_layout(layout, title):
    colors = ['gray'] + [plt.cm.tab20(i) for i in range(1, num_files + 1)]
    cmap = {i: colors[i] for i in range(1, num_files + 1)}
    cmap.update({-i: plt.cm.tab20(i - 1) for i in range(1, num_files + 1)})

    color_layout = [cmap.get(block, 'white') for block in layout]

    fig, ax = plt.subplots(figsize=(10, 2))
    ax.bar(range(num_blocks), [1] * num_blocks, color=color_layout, edgecolor='none')
    ax.set_title(title)
    ax.axis('off')
    plt.show()


visualize_layout(low_fragmentation_layout, "Low Fragmentation")
visualize_layout(high_fragmentation_layout, "High Fragmentation")
