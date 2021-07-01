import matplotlib.pyplot as plt
import numpy as np
from farrow_and_ball import *
from matplotlib.colors import LinearSegmentedColormap

plt.style.use("styles/minimal.mplstyle")

x = np.arange(0, np.pi, 0.1)
y = np.arange(0, 2 * np.pi, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(Y) * 10

n_bins = [3, 6, 10, 100]  # Discretizes the interpolation into bins

palettes = [
    ("Spectral", SpectralPalette),
    ("Divergent", DivergentPalette),
    ("Base Color", BaseColorPalette),
    ("Misc", MiscPalette),
]

for palette_type_name, palette_type in palettes:
    for palette in palette_type:
        fig, axs = plt.subplots(2, 2, figsize=(6, 9))
        fig.suptitle(f"{palette_type_name}: {palette.value}", fontsize=16)
        fig.subplots_adjust(left=0.02, bottom=0.06, right=0.95, top=0.94, wspace=0.05)
        for n_bin, ax in zip(n_bins, axs.ravel()):
            # Create the colormap
            cmap = LinearSegmentedColormap.from_list(
                palette.value, get_palette(palette), N=n_bin
            )
            # Fewer bins will result in "coarser" colomap interpolation
            im = ax.imshow(Z, origin="lower", cmap=cmap)
            ax.set_title("N bins: %s" % n_bin)
            fig.colorbar(im, ax=ax)
        plt.show()
