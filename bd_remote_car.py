from bluedot import *
from signal import pause
import sys

# import other scripts : sys.path.append('path')

# script that creates and manages interactions with BlueDot buttons
# --> main script


# remote format : acc. + brake at left, and left/right at right
bd = BlueDot(cols=6, rows=3) # MockBlueDot for tests without bluetooth client


acc = bd[0, 0]
brake = bd[0, 2]
left = bd[3, 1]
right = bd[5,1]

bd[0, 1].visible = False
bd[1, 0].visible = False
bd[1, 1].visible = False
bd[1, 2].visible = False
bd[2, 0].visible = False
bd[2, 1].visible = False
bd[2, 2].visible = False
bd[3, 0].visible = False
bd[3, 2].visible = False
bd[4, 0].visible = False
bd[4, 1].visible = False
bd[4, 2].visible = False
bd[5, 0].visible = False
bd[5, 2].visible = False


acc.square = brake.square = True
left.border = right.border = True
acc.color = brake.color = (150, 150, 150)
left.color = right.color = (200, 0, 0)


pause()

# next test : effect of pressing / releasing buttons
