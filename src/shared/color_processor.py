"""
Color Processor Module

This module provides functionality for color processing using the `colorama`
library and font options using the `pyfiglet` library.
It initializes colorama, enumerates available colors and fonts, and
offers functions to display color and font options.

Functions:
- `display_colors() -> None:`: Displays a numbered list of available color options.
- `display_fonts() -> None:`: Displays a numbered list of available font options.

Usage:
1. Import the module: `import shared.color_processor`
2. Use the provided functions to display color and font options.
"""
import colorama
import pyfiglet
from colorama import Fore

colorama.init(autoreset=True)
colors = dict(enumerate(sorted(Fore.__dict__.keys())))
fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))


def display_colors() -> None:
    """
    Displays available color options.

    Prints a numbered list of color options available in the `colors` dictionary.
    """
    for i in colors:
        print(str(i) + ". " + colors[i])


def display_fonts() -> None:
    """
    Displays available font options.

    Prints a numbered list of font options available in the `fonts` dictionary.
    """
    for i in fonts:
        print(str(i) + ". " + fonts[i])
