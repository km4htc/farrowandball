from enum import Enum
from typing import List, Union
from matplotlib.colors import LinearSegmentedColormap

fb_colors = {
    "Middleton Pink": "#fde7e5",
    "Calluna": "#ccc8ce",
    "Sugaroom Red": "#d0bfcd",
    "Brassica": "#8d8089",
    "Pelt": "#50414c",
    "Brinjal": "#5e3a42",
    "Preference Red": "#6d4247",
    "Sulking Room Pink": "#a0837f",
    "Cinder Rose": "#c6a4a6",
    "Nancys Blushes": "#ecb7b8",
    "Rangwali": "#bf7a8f",
    "Lake Red": "#c8526a",
    "Rectory Red": "#a53c49",
    "Incarnadine": "#a04344",
    "Blazer": "#b64f48",
    "Harissa": "#ae5043",
    "Charlottes Locks": "#d65f3d",
    "Book Room": "#ab6758",
    "Red Earth": "#c57b67",
    "India Yellow": "#cb9e59",
    "Sudbury Yellow": "#dcb771",
    "Babouche": "#ecc363",
    "Yellowcake": "#ebe05e",
    "Yellow Ground": "#f2cf86",
    "Dayroom Yellow": "#f7e29d",
    "Dorset Cream": "#efd5a1",
    "Tallow": "#fdedd7",
    "Farrows Cream": "#efdbb3",
    "Hay": "#dec795",
    "Citrona": "#dbcc7c",
    "Churlish Green": "#c8bd83",
    "Yeabridge Green": "#909e6e",
    "Bancha": "#686a47",
    "Duck Green": "#465741",
    "Green Ground": "#dbdab6",
    "Cooking Apple Green": "#c4c6a5",
    "Lichen": "#a1a189",
    "Breakfast Room Green": "#94a68a",
    "Calke Green": "#758769",
    "Emerald Green": "#7bae72",
    "Verdigris": "#3e8b67",
    "Vardo": "#427e83",
    "Arsenic": "#84b59c",
    "Green Smoke": "#737c70",
    "Oval Room Blue": "#8b9d9b",
    "Green Blue": "#acbdb2",
    "Dix Blue": "#99b0ab",
    "Parma Gray": "#b1bfc5",
    "Blue Ground": "#a1c5c8",
    "Stone Blue": "#7997a1",
    "Inchyra Blue": "#586768",
    "Hague Blue": "#3d4e57",
    "Stiffkey Blue": "#4d5b6a",
    "St Giles Blue": "#599ec4",
    "Ultra Marine Blue": "#5d82a1",
    "Cooks Blue": "#6a90b4",
    "Lulworth Blue": "#a0b8c8",
    "Pitch Blue": "#636e8f",
    "Imperial Purple": "#55566b",
    "Scotch Blue": "#41404c",
    "Paean Black": "#494248",
    "Railings": "#45494b",
    "Off Black": "#444546",
    "Pitch Black": "#3b3938",
    "Pigeon": "#a0a093",
    "Old White": "#cec3ad",
    "Strong White": "#e5e0db",
    "Cabbage White": "#e8eeea",
}


def _fb_cols(*colors):
    return [fb_colors[n] for n in colors]


fb_palettes = {
    "all": _fb_cols(*fb_colors.keys()),
    "original": _fb_cols(
        "Stiffkey Blue",
        "Cooks Blue",
        "St Giles Blue",
        "Blue Ground",
        "Stone Blue",
        "Vardo",
        "Arsenic",
        "Yeabridge Green",
        "Bancha",
        "Churlish Green",
        "India Yellow",
        "Babouche",
        "Red Earth",
        "Charlottes Locks",
        "Incarnadine",
        "Rangwali",
        "Brassica",
        "Pelt",
    ),
    "pinks": _fb_cols(
        "Middleton Pink", "Nancys Blushes", "Rangwali", "Lake Red", "Rectory Red"
    ),
    "pinks2": _fb_cols(
        "Middleton Pink",
        "Nancys Blushes",
        "Rangwali",
        "Brinjal",
        "Pelt",
        "Sugaroom Red",
    ),
    "reds": _fb_cols(
        "Red Earth", "Charlottes Locks", "Blazer", "Rectory Red", "Preference Red"
    ),
    "yellows": _fb_cols(
        "Tallow", "Dayroom Yellow", "Yellow Ground", "Babouche", "India Yellow"
    ),
    "greens": _fb_cols("Churlish Green", "Yeabridge Green", "Bancha", "Duck Green"),
    "greens2": _fb_cols(
        "Cooking Apple Green",
        "Breakfast Room Green",
        "Calke Green",
        "Duck Green",
        "Green Smoke",
        "Railings",
    ),
    "blues": _fb_cols(
        "Parma Gray", "Blue Ground", "Stone Blue", "Inchyra Blue", "Hague Blue"
    ),
    "blues2": _fb_cols(
        "Cabbage White",
        "Lulworth Blue",
        "Ultra Marine Blue",
        "Stiffkey Blue",
        "Scotch Blue",
    ),
    "deepspec": _fb_cols(
        "Stiffkey Blue",
        "Hague Blue",
        "Duck Green",
        "Bancha",
        "India Yellow",
        "Harissa",
        "Incarnadine",
        "Brinjal",
        "Pelt",
        "Brassica",
    ),
    "spec": _fb_cols(
        "St Giles Blue",
        "Ultra Marine Blue",
        "Vardo",
        "Verdigris",
        "Emerald Green",
        "Babouche",
        "Charlottes Locks",
        "Rectory Red",
        "Lake Red",
        "Rangwali",
    ),
    "lightspec": _fb_cols(
        "Lulworth Blue",
        "Blue Ground",
        "Dix Blue",
        "Breakfast Room Green",
        "Yeabridge Green",
        "Dayroom Yellow",
        "Book Room",
        "Cinder Rose",
        "Nancys Blushes",
    ),
    "lighterspec": _fb_cols(
        "Cabbage White",
        "Parma Gray",
        "Green Blue",
        "Cooking Apple Green",
        "Churlish Green",
        "Yellow Ground",
        "Red Earth",
        "Sugaroom Red",
        "Middleton Pink",
    ),
    "mono": _fb_cols("Strong White", "Pitch Black"),
    "tonka": _fb_cols("Babouche", "Inchyra Blue", "Blazer", "Off Black"),
    "bellsprout": _fb_cols("Arsenic", "Citrona", "Sulking Room Pink", "Preference Red"),
    "dockers": _fb_cols("Stone Blue", "Calke Green", "Sudbury Yellow", "Scotch Blue"),
    "fruitypebbles": _fb_cols("Lake Red", "Vardo", "Verdigris", "Yellowcake"),
    "day": _fb_cols(
        "Hay",
        "Farrows Cream",
        "Green Ground",
        "Oval Room Blue",
        "Imperial Purple",
        "Pitch Blue",
        "Cooks Blue",
    ),
    "daylong": _fb_cols(
        "Tallow",
        "Dorset Cream",
        "Lichen",
        "Green Smoke",
        "Inchyra Blue",
        "Railings",
        "Pitch Black",
    ),
    "army": _fb_cols(
        "Calluna", "Old White", "Lichen", "Pigeon", "Off Black", "Paean Black"
    ),
}


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


# from https://stackoverflow.com/a/32558749/6386471
def _levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1]))
                )
        distances = distances_
    return distances[-1]


class PaletteNotFoundError(Exception):
    def __init__(self, tried_name):
        distances = {k: _levenshteinDistance(tried_name, k) for k in fb_palettes.keys()}
        min_distance_key = min(distances, key=distances.get)
        message = f"Palette {tried_name} not found.\n\tDid you mean: {min_distance_key}"
        super().__init__(message)


class PaletteTypeNotImplementedError(Exception):
    def __init__(self, palette):
        message = (
            f"Palette {type(palette)} not implemented.\n"
            "\tUse one of SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette"
        )
        super().__init__(message)


def all_palettes() -> List[str]:
    """Returns all implemented palette names.

    Returns:
        List[str]: The name of all implemented palettes.
    """
    return list(fb_palettes.keys())


def _get_palette_name(palette: Union[Enum, str]):
    if isinstance(palette, Enum):
        if not isinstance(
            palette,
            (SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette),
        ):
            raise PaletteTypeNotImplementedError(palette)
        palette_name = palette.value
    elif isinstance(palette, str):
        palette_name = palette
    else:
        raise TypeError(f"Unsupported input {palette} of type {type(palette)}")

    return palette_name


def get_palette(palette: Union[Enum, str], reverse: bool = False) -> List[str]:
    """Get the palette hex string definition.

    Args:
        palette (Union[Enum, str]): The palettes to use. Can either be a string or one
            of the enums [SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette].
        reverse (bool, optional): Reverse the color gradient. Defaults to False.

    Raises:
        PaletteNotFoundError: If the palette name is not defined.
        PaletteTypeNotImplementedError: If an Enum is passed which does not belong to
            [SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette].
        TypeError: If the input for the palette is not accepted.

    Returns:
        List[str]: A list of hex string defining the color palette.
    """
    palette_name = _get_palette_name(palette)
    if palette_name not in fb_palettes:
        raise PaletteNotFoundError(palette_name)

    palette = fb_palettes[palette_name]

    if reverse:
        return palette[::-1]
    else:
        return palette


def get_interpolated_palette(
    palette: Union[Enum, str], num_colors: int, reverse: bool = False
) -> List[List[float]]:
    return build_colormap(palette, True, reverse=reverse)(
        [x * 1 / (num_colors - 1) for x in range(0, num_colors)]
    )


def build_colormap(
    palette: Union[Enum, str], continuous: bool, reverse: bool = False
) -> LinearSegmentedColormap:
    """Builds a matplotlib color map from a palette definition.

    Args:
        palette (Union[Enum, str]): The palettes to use. Can either be a string or one
            of the enums [SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette].
        continuous (bool): Builds a continuous color map or a sequential one.
        reverse (bool, optional): Reverse the color gradient. Defaults to False.

    Raises:
        PaletteNotFoundError: If the palette name is not defined.
        PaletteTypeNotImplementedError: If an Enum is passed which does not belong to
            [SpectralPalette, DivergentPalette, BaseColorPalette, MiscPalette].
        TypeError: If the input for the palette is not accepted.

    Returns:
        LinearSegmentedColormap: The color map ready to be used in matplotlib.
    """
    palette_name = _get_palette_name(palette)
    palette = get_palette(palette, reverse=reverse)

    return LinearSegmentedColormap.from_list(
        palette_name, palette, N=256 if continuous else len(palette)
    )
