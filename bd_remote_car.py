from bluedot import *
from signal import pause
import sys

# import other scripts : sys.path.append('path')

# script that creates and manages interactions with BlueDot buttons
# --> main script


# remote format : acc. + brake at left, and left/right at right
bd = BlueDot(cols=4, rows=3) # MockBlueDot for tests without bluetooth client


acc = bd[0, 0]
brake = bd[0, 2]
left = bd[2, 1]
right = bd[3,1]

bd[0, 1].visible, bd[1, 0].visible, bd[1, 1].visible, bd[1, 2].visible, bd[2, 0].visible, bd[2, 2].visible, bd[3, 0].visible, bd[3, 2] = [False] * 8

acc.square = brake.square = True
left.border = right.border = True
acc.color = brake.color = (150, 150, 150)
left.color = right.color = (200, 0, 0)


pause()

# next test : effect of pressing / releasing buttons
