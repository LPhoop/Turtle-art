import random
# CAC, 3/2023
# This class just allows me to use a single color palette throughout my various scripts.
# It isn't very useful as is, but we will make a better version soon.
colors= ['#c5aeb1', '#e2c1c0', '#d29380', '#ccb97e', '#6667ab', '#86a293', '#884c5e', '#9d848e']
# Colorhunt.co
colors2 =['#F5EAEA', '#FFB84C', '#F16767', '#A459D1']
#80s color calette color hex
colors_80s = ['#FF48C4', '#2BD1FC', '#F3EA5F', '#C04DF9', '#FF3F3F']


colorPalettes = colors, colors2

def randomPaletteColor():
    palatte = random.choice(colorPalettes)
    return random.choice(palatte)