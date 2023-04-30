from random import random, choice

palettes = {
    "colors_70s" : ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e'],
    "colors_80s" : ['#FF48C4', '#2BD1FC', '#F3EA5F', '#C04DF9', '#FF3F3F'],
    "colorIORandom" : ['#493548', '#AA8F66', '#A72608', '#247BA0', '#9DD9D2'],
    "Burger_King" : ['#EC1C24', '#FDBD10', '#0066B2', '#ED7902'],
    "Viridis (4)" : ['#fde725','#35b779','#31688e','#440154'],
    'Tol Dark (6)': ['#222255', '#225555', '#225522', '#666633', '#663333', '#555555'],
    "Hope College (6)": ['#F46A1F', '#002244', '#F7E654', '#BED600', '#00685B', '#00B0CA'],
    "Grayscale (7)": ['#FFFFFF', '#D5D5D5', '#AAAAAA', '#808080', '#555555', '#2A2A2A', '#000000'],
    "Custom Orange shades 1 (5)" : ["#f88633", "#f8a032", "#f8bd3b", "#f8d633", "#f8f033"],
    "Custom Pale Green (5)" : ["#41f513", "#83f5c1", "#f53286", "#f599c3", "#b5f5d8"],
    "Custom Light Colors" : ["#2cfae1", "#9454fa","#fa5467","#bafa54","#97faef",],
    "Custom Blue Shades" : ["#349efa", "#3368fa", "#4040fa", "#6833fa", "#8e14fa"],
    "Custom Complementary dark Blue to orange" : ["#5cafd4","#72b6d4","#d47348","#d49072","#9dc4d4"],
}

paletteList = list(palettes.items())

def getPalette(name):
    """
    Returns the colors of the palette of the given name,
    or None if there is no such palette.
    Returns a copy of the internal color array stored here.
    :param name:
    :return:
    """
    if name in palettes:
        return palettes.get(name).copy()
    else:
        return None

def randomNamedPalette():
    """
    Returns a random palette along with its name,
    with the name being first and the list of colors second.
    Returns a copy of the internal color array stored here.
    :return:
    """
    n,c=choice(paletteList)
    return n,c.copy()

def randomPalette():
    """
    :return:
    returns the colors of a random palette from the list.
    Does not return the name.
    Returns a copy of the internal color array stored here.
    """
    return choice(paletteList)[1].copy()