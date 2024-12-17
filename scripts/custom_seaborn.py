import matplotlib as mpl
import matplotlib.font_manager as fm
import seaborn
import requests
from pathlib import Path

class ColorPalette:
    def __init__(self, palette_name="Irag's Palette (Default)"):
        """
        Initializes a new instance of the ColorPalette class.

        Parameters:
        - palette_name (str): The name of the color palette. Defaults to "irag Palette".

        The ColorPalette class represents a collection of colors and provides methods to add, retrieve,
        remove, and list colors. It also includes a method to display the palette.

        The colors are stored in a dictionary where the keys are the color names and the values are the
        corresponding hex color values.

        Example usage:
        >>> irag = ColorPalette()
        >>> irag.display_palette()
        Palette: irag Palette
        push to bg: #DDDDDD
        dark gray: #3b3b3b
        gray: gray
        light gray: #BFBFBF
        dark blue: #072ea5
        blue: #5099fe
        light blue: #91c2ed
        light orange: #fbb181
        orange: #FB7B33
        dark orange: #ff3e06
        dark teal: #299ba1
        teal: #2e99a2
        light teal: #8af0dd
        soft black: #333333
        """
        self.palette_name = palette_name
        self.colors = {
            "push to bg" : '#DDDDDD',

            "dark gray": '#3b3b3b',
            "gray": 'gray',
            "light gray": '#BFBFBF',

            "dark blue": '#072ea5',
            "blue": '#5099fe',
            "light blue": '#91c2ed',

            "light orange": '#fbb181',
            "orange": '#FB7B33',
            "dark orange": '#ff3e06',

            "dark teal": '#299ba1',
            "teal": '#2e99a2',
            "light teal": '#8af0dd',

            "soft black": '#333333'
        }
    
    def add_color(self, name, hex_value):
        """Adds a color to the palette."""
        self.colors[name] = hex_value
    
    def color(self, name):
        """Retrieves the hex value of a color by its name."""
        return self.colors.get(name, None)
    
    def remove_color(self, name):
        """Removes a color from the palette."""
        if name in self.colors:
            del self.colors[name]
        else:
            print(f"Color '{name}' not found in the palette.")
    
    def list_colors(self):
        """Lists all colors in the palette."""
        return self.colors
    
    def display_palette(self):
        """Displays all colors with their hex values."""
        if not self.colors:
            print(f"{self.palette_name} is empty.")
        else:
            print(f"Palette: {self.palette_name}")
            for name, hex_value in self.colors.items():
                print(f"{name}: {hex_value}")    

def download_font(url: str, font_name: str, cache_dir="cache"):
    # Create the cache directory if it doesn't exist
    Path(cache_dir).mkdir(parents=True, exist_ok=True)

    # Define the font file path
    font_path = Path(cache_dir) / f"{font_name}.ttf"
    
    # Check if font is already cached
    if not font_path.is_file():
        response = requests.get(url)
        response.raise_for_status()  # Ensure the download is successful

        # Save the file to the cache directory
        with open(font_path, "wb") as file:
            file.write(response.content)
        print(f"Font downloaded and saved to: {font_path}")
    else:
        print(f"Font loaded from cache: {font_path}")

    return font_path

font_url = "https://github.com/Chris-Gari/Global-Terrorism-EDA/raw/main/Roboto-Bold.ttf"
font_file = download_font(font_url, "Roboto-Bold")

font_path = 'cache/Roboto-Bold.ttf'
fm.fontManager.addfont(font_path)
prop = fm.FontProperties(fname=font_path)

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

irag = ColorPalette()  
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] =  False
mpl.rcParams['axes.labelcolor'] =  irag.color("soft black")
mpl.rcParams['axes.titlecolor'] =  irag.color("dark gray")
mpl.rcParams['xtick.color'] = irag.color("light gray")
mpl.rcParams['ytick.color'] = irag.color("light gray")
mpl.rcParams['xtick.labelcolor'] = irag.color("gray")
mpl.rcParams['ytick.labelcolor'] = irag.color("soft black")
mpl.rcParams['font.family'] = 'Roboto'
mpl.rcParams['xaxis.labellocation'] = 'left'
mpl.rcParams['yaxis.labellocation'] = 'top' 
mpl.rcParams['axes.labelpad'] = 10.0  
mpl.rcParams['axes.edgecolor'] = irag.color("light gray")

seaborn.set_palette([irag.color('gray')])
