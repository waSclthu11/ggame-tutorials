"""waSclthu11's ggame tutorial"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

myapp = App()
#define colors and line style
green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)

# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))
# Original image is too big. Scale it to 1/10 its original size
ball.scale = 0.1
# custom attributes
ball.direction = 1
ball.go = True
# reverse - change the ball direction
def reverse(b):
    b.direction *= -1
    
# Set up function for handling screen refresh
def step():
    if ball.go:
        ball.x += ball.direction
        if ball.x + ball.width > myapp.width or ball.x < 0:
            ball.x -= ball.direction
            reverse(ball)
myapp.run(step)

