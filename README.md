# Farrow&Ball Matplotlib

[![pypi Badge](https://img.shields.io/badge/pypi-0.0.2-blue)](https://pypi.org/project/farrow-and-ball/)

This is a python port for the matplotlib library of the [R Package](https://github.com/km4htc/farrowandball) for ggplot2.

![spec palette charts](https://github.com/vork/farrowandball/raw/master/images/chart/spec.png)
![tonka palette charts](https://github.com/vork/farrowandball/raw/master/images/chart/tonka.png)

The style for the charts is provided in the [styles](https://github.com/vork/farrowandball/tree/master/styles) folder

# Installation

A python version >= 3 is required.
```bash
pip install farrow-and-ball
```

# Usage

The usage is quite simple:

```python
from farrow_and_ball import *
import numpy as np
import matplotlib.pyplot as plt

# Define a gray scale image
x = np.arange(0, np.pi, 0.1)
y = np.arange(0, 2 * np.pi, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(Y) * 10

# Get the color map
cmap = build_colormap(DivergentPalette.DAY, True)

# Draw image
plt.imshow(Z, origin="lower", cmap=cmap)
plt.show()
```

One can also directly get the color map definition as a list of strings with `farrow_and_ball.get_palette()`.

# Palettes

The palettes are organized in Enums:

```python
class SpectralPalette(Enum):
    DEEPSPEC = "deepspec"
    SPEC = "spec"
    LIGHTSPEC = "lightspec"
    LIGHTERSPEC = "lighterspec"


class DivergentPalette(Enum):
    DAY = "day"
    DAYLONG = "daylong"
    ARMY = "army"
    MONO = "mono"


class BaseColorPalette(Enum):
    PINKS = "pinks"
    PINKS_VAR = "pinks2"
    REDS = "reds"
    YELLOWS = "yellows"
    GREENS = "greens"
    GREENS_VAR = "greens2"
    BLUES = "blues"
    BLUES_VAR = "blues2"


class MiscPalette(Enum):
    TONKA = "tonka"
    BELLSPOUT = "bellsprout"
    DOCKERS = "dockers"
    FRUITYPEBBLES = "fruitypebbles"
```

One can also directly enter the name as a string, e.g. `build_colormap("day", True)`.

## Color Maps

### Continuous
![Spectral Palette](https://github.com/vork/farrowandball/raw/master/images/continuous/SpectralPalette.png)
![Divergent Palette](https://github.com/vork/farrowandball/raw/master/images/continuous/DivergentPalette.png)
![Base Color Palette](https://github.com/vork/farrowandball/raw/master/images/continuous/BaseColorPalette.png)
![Misc Palette](https://github.com/vork/farrowandball/raw/master/images/continuous/MiscPalette.png)

### Discrete
![Spectral Palette](https://github.com/vork/farrowandball/raw/master/images/discrete/SpectralPalette.png)
![Divergent Palette](https://github.com/vork/farrowandball/raw/master/images/discrete/DivergentPalette.png)
![Base Color Palette](https://github.com/vork/farrowandball/raw/master/images/discrete/BaseColorPalette.png)
![Misc Palette](https://github.com/vork/farrowandball/raw/master/images/discrete/MiscPalette.png)