import numpy as np
import matplotlib.pyplot as plt
from farrow_and_ball import *

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_enum):
    # Create figure and adjust figure height to number of colormaps
    cmap_enum_list = [e for e in cmap_enum]
    cmap_category_name = cmap_enum.__name__

    nrows = len(cmap_enum_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(cmap_category_name, fontsize=14)

    for ax, cmap_enum in zip(axs, cmap_enum_list):
        ax.imshow(gradient, aspect='auto', cmap=build_colormap(cmap_enum, True))
        ax.text(-0.01, 0.5, cmap_enum.name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    fig.savefig(f"images/{cmap_category_name}.png")


for cmap_enum in [SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette]:
    plot_color_gradients(cmap_enum)

# plt.show()