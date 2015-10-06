# Rice University
# An Introduction to Interactive Programming in Python
# Mini-project 4

# Implementation of classic arcade game Pong
# by Theresa MacDonald

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,1]

paddle1_pos = paddle2_pos = WIDTH / 2
score1 = score2 = paddle1_vel = paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = -random.randrange(120,240) / 80 
    if direction == RIGHT:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(60, 180) / 80   

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2
    direction = [LEFT, RIGHT]
    score1 = 0
    score2 = 0
    spawn_ball(direction[random.randrange(0,2)])


def draw(canvas):
    global score1, score2, ball_pos, ball_vel
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball, and determine whether paddle and ball collide
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (paddle1_pos - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle1_pos+HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0] #increase velocity by 10%
        else:
            spawn_ball(True)
            score2 += 1
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        
        if (paddle2_pos - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle2_pos+HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0] #increase velocity by 10%
        else:
            spawn_ball(False)
            score1 += 1
            
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'Lime', 'Lime')
    
    # update paddle's vertical position, keep paddle on the screen
   
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    elif paddle1_pos + paddle1_vel < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos + paddle1_vel > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    elif paddle2_pos + paddle2_vel < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos + paddle2_vel > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Orange")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Fuchsia")
     
    
    # draw scores
    canvas.draw_text(str(score1), [100,100], 40, "Orange", "sans-serif")
    canvas.draw_text(str(score2), [500,100], 40, "Fuchsia", "sans-serif")
    
    # draw backgroung image
    canvas.draw_text('PONG', (150, 340), 100, 'Navy', 'sans-serif')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 9
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel

   
def keyup(key):
    global paddle1_vel, paddle2_vel  
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

# start frame
new_game()
frame.start()

