from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()yapp = App()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
# Background

myapp=Spacegame()
myapp.run()
