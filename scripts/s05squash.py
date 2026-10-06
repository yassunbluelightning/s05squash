#s05squash.py
import pj
import pjTkInter as tk
import pjSound as sound
from logStdErr import logStdErrClass
lse=logStdErrClass()
lse.setProjectName("s05squash")
lse.errToFile()

# Squash Game
# imports Modules
import pj
import random

tk.updateMainLabel("'squash.py', from \"Learning Programing with Gamecenter Arashi:\nManga ver.Hello Python\" ((C)Mitsuru Sugaya, 2020)")

# initializes Game
def initGame():
  global isGameOver, ballPosX, ballPosY
  global ballMoveX, ballMoveY, ballSize
  global racketPosX, racketSize, point, speed

  isGameOver = False
  ballPosX = 0
  ballPosY = 250
  ballMoveX = 15
  ballMoveY = -15
  ballSize = 10
  racketPosX = 0
  racketSize = 100
  point = 0
  speed = 0.1
  tk.title("Squash Game：Start！")

# draws Screen
def drawScreen():
  # clear Canvas
  tk.removeAllFromCanvas()
  # creates Canvas
  tk.createRectangle("bg",
  640,480, 1,
  0,0,10000,
  ##0,200,200,255)
  ####240,230,140,255) ###Khaki;#F0E68C;
  32,178,170,255) ###LightSeaGreen;;#20B2AA

def drawBall():
  # draws Ball
  tk.createCircle("cir1",
  ballSize,1,
  ballPosX,ballPosY,65000,
  255,0,0,255)

def drawRacket():
  # draws Racket
  tk.createRectangle("rect1",
  racketSize,10, 1,
  racketPosX,0,65000,
  255, 255,0,255)

# moves Ball
def moveBall():
  global isGameOver, point, ballPosX, ballPosY, ballMoveX, ballMoveY
  if isGameOver: return

  # collides with Side Walls
  if ballPosX + ballMoveX < 0 or ballPosX + ballMoveX > 640:
    ballMoveX *= -1
    sound.midi(0, 64,0.05)

  # collides with Ceiling
  if ballPosY + ballMoveY >= 480:
    ballMoveY *= -1
    sound.midi(0, 64,0.05)

  # collides with Racket
  if ballPosY + ballMoveY <= 10 and (
    racketPosX <= (ballPosX + ballMoveX)
    <= (racketPosX + racketSize)
    ):
    ballMoveY *= -1
    if random.randint(0, 1) == 0:
      ballMoveX *= -1
    sound.midi(0, 71,0.05)
    msgInt = random.randint(0, 4)
    if msgInt == 0:
      msgStr = "You are Good at！"
    if msgInt == 1:
      msgStr = "That's Good！"
    if msgInt == 2:
      msgStr = "That's Nice！"
    if msgInt == 3:
      msgStr = "It's Good！"
    if msgInt == 4:
      msgStr = "Awesome！"
    point += 10
    tk.title(msgStr + " Score＝" + str(point))

  # judges whether Missed
  if ballPosY + ballMoveY <= 0:
    msgInt = random.randint(0, 2)
    if msgInt == 0:
      msgStr = "You are Bad at！"
    if msgInt == 1:
      msgStr = "You missed it！"
    if msgInt == 2:
      msgStr = "I can't see it！"
    tk.title(msgStr + " Score＝" + str(point))
    sound.midi(0, 54,0.8)
    isGameOver = True

  if 0 <= ballPosX + ballMoveX <= 640:
    ballPosX = ballPosX + ballMoveX
  if 0 <= ballPosY + ballMoveY <= 480:
    ballPosY = ballPosY + ballMoveY

# Observes Mouse Move
def motion(eventX,eventY): # Observes Mouse Position
  global racketPosX
  racketPosX = eventX
  if racketPosX >= 640 - racketSize:
    racketPosX = 640 - racketSize

# Observes Whether Button Clicked.
def click(eventNum): # clicks to restart
  if eventNum == 1:
    initGame()

# Sub Routines called from MainLoop.
def gameLoop():
  drawScreen()
  drawBall()
  drawRacket()
  moveBall()

# MainLoop.
initGame()
gameLoop()

tk.bindMotionFunction("s05squash:s05squash.motion")

tk.bindButtonFunction("s05squash:s05squash.click")

tk.startTimerFunctionAfter("s05squash:s05squash.gameLoop",speed)
