# control the position of a ball using the arrow keys
# to run in http://www.codeskulptor.org/
import simplegui
# Initialize globals
WIDTH = 400
HEIGHT = 400
BALL_RADIUS = 10
ball_position = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_position, BALL_RADIUS, 1, "Red", "White")    

def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_position[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_position[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_position[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_position[1] -= vel   
    print "Ball position : x[" + str(ball_position[0]) +"], y["+ str(ball_position[0])+"]"
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
