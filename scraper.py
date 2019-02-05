import pyscreenshot as ImageGrab
from pyautogui import press
import time
import os
import datetime
import uuid

teamPositions = [
    [35, 70, 150, 150],
    [1235, 70, 1350, 150],
]

def capturePlayer( tick, team, player, pos):
    im = ImageGrab.grab(bbox=pos)  # X1,Y1,X2,Y2
    path = "screenshots\\team{team}\\player{player}\\".format(
        player=player, team=team)
    if not os.path.exists(path):
        os.makedirs(path)
    im.save( path + "tick{tick}_{uuid}.png".format(tick=tick, timestamp=uuid.uuid4()))
    pos[0] = pos[0] + 105
    pos[2] = pos[0] + 140

def captureTeam( tick, team ):
    pos = teamPositions[team].copy()
    for player in range(0, 6):
        capturePlayer( tick, team, player, pos )


def captureTeams( tick ):
    for team in range(0, 2):
        captureTeam( tick, team )

def captureGame( ticks, skips ):
    time.sleep(5)
    for i in range(1, ticks):
    # skip 
        for j in range(1, skips):
            press('right')

        captureTeams( i )

def main():
    captureGame( 100, 5 )


if __name__ == '__main__':
    main()