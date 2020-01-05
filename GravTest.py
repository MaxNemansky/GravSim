import pygame, sys, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()

window = pygame.display.set_mode((600, 600))

clock = pygame.time

timeSurp = 10 # Doba mezi cykly v milisekundách
gravConst = 1 # Gravitační konstanta

class Body:
    def __init__(self, loc, mass, vel, a, aVec, color):
        self.loc = loc # Array in the format (x possition, y possition)
        self.mass = mass # Body mass - NOT IN KG - Take size of gravConst into consideration
        self.vel = vel # Array in the format (x component of the velocity vector, y component of the velocity vector)
        self.a = a # Absolute value of acceleration
        self.aVec = aVec # Array in the format (x component of the acceleration vector, y component of the acceleration vector)
        self.color = color # Color of the body, has no effect on the simulation itself, should be passed as an array
    def setLoc(self, loc):
        self.loc = loc
    def setMass(self, mass):
        self.mass = mass
    def setVel(self, vel):
        self.vel = vel
    def setA(self, a):
        self.a = a
    def setAVec(self, aVec):
        self.aVec = aVec
    def setColor(self, color):
        self.color = color

class GravCalc: # Gravity calculation class, the core of the simulation
    def __init__(self, bodies):
        self.bodies = bodies
    def calcPosition(self, body):
        for bo in self.bodies:
            if body == bo:
                pass # Check if second body isn't first body
            else:
                body.setA(bo.mass*gravConst/(math.pow(bo.loc[0]-body.loc[0],2)+math.pow(bo.loc[1]-body.loc[1],2))) # Absolutní hodnota zrychlení
                cosAlpha = ((bo.loc[0]-body.loc[0])/(math.sqrt(math.pow(bo.loc[0]-body.loc[0],2)+math.pow(bo.loc[1]-body.loc[1],2))))
                sinAlpha = ((bo.loc[1]-body.loc[1])/(math.sqrt(math.pow(bo.loc[0]-body.loc[0],2)+math.pow(bo.loc[1]-body.loc[1],2))))
                body.setAVec((cosAlpha*body.a, sinAlpha*body.a)) # Compute acceleration vector components
                body.setVel((body.vel[0] + body.aVec[0], body.vel[1] + body.aVec[1])) # Compute velocity vector components
        body.setLoc((body.loc[0] + body.vel[0], body.loc[1] + body.vel[1])) # Set new body location
        return body.loc



bo1 = Body((200,300), 100, (0,0.5), 0, (0,0), (255,0,0))
bo2 = Body((400,300), 100, (0,-0.5), 0, (0,0), (0,0,255))
bo3 = Body((100,200), 20, (0.2,0), 0, (0,0), (0,100,255))

bodyArray = (bo1, bo2, bo4)
calc = GravCalc((bodyArray))

while True:
    window.fill((255, 255, 255))
    
    for body in bodyArray:
        loc = calc.calcPosition(body) # Calculate new values for body properties
        pygame.draw.circle(window, body.color, (int(body.loc[0]), int(body.loc[1])), 10, 0) # Draw body
    
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.wait(timeSurp)