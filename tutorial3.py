"""waSclthu11's ggame tutorial"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

myapp = App()
myapp.run()
# define colors and line style
green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))