import curses
import time

# initialize ncurses
stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# set up game properties
PADDLE_WIDTH = 3
PADDLE_HEIGHT = 15
BALL_CHAR = 'O'
PADDLE_CHAR = '|'

ball_x = curses.COLS // 2
ball_y = curses.LINES // 2
ball_vx = 1
ball_vy = 1

paddle1_x = 0
paddle1_y = curses.LINES // 2 - PADDLE_HEIGHT // 2
paddle2_x = curses.COLS - PADDLE_WIDTH
paddle2_y = curses.LINES // 2 - PADDLE_HEIGHT // 2

score1 = 0
score2 = 0

# draw paddle function
def draw_paddle(x, y):
    for i in range(PADDLE_HEIGHT):
        stdscr.addstr(y + i, x, PADDLE_CHAR)

# loop to animate game
while True:
    # clear screen
    stdscr.clear()

    # move ball
    ball_x += ball_vx
    ball_y += ball_vy

    # check ball bounds
    if ball_x >= curses.COLS - 1:
        ball_vx = -1
        score1 += 1
        ball_x = curses.COLS // 2
        ball_y = curses.LINES // 2
    elif ball_x <= 0:
        ball_vx = 1
        score2 += 1
        ball_x = curses.COLS // 2
        ball_y = curses.LINES // 2

    if ball_y >= curses.LINES - 1 or ball_y <= 0:
        ball_vy *= -1

    # check paddle collisions
    if ball_x == paddle1_x + PADDLE_WIDTH and ball_y >= paddle1_y and ball_y < paddle1_y + PADDLE_HEIGHT:
        ball_vx *= -1

    if ball_x == paddle2_x and ball_y >= paddle2_y and ball_y < paddle2_y + PADDLE_HEIGHT:
        ball_vx *= -1

    # move paddles
    key = stdscr.getch()
    if key == ord('w') and paddle1_y > 0:
        paddle1_y -= 1
    elif key == ord('s') and paddle1_y + PADDLE_HEIGHT < curses.LINES:
        paddle1_y += 1
    elif key == curses.KEY_UP and paddle2_y > 0:
        paddle2_y -= 1
    elif key == curses.KEY_DOWN and paddle2_y + PADDLE_HEIGHT < curses.LINES:
        paddle2_y += 1

    # draw game objects
    draw_paddle(paddle1_x, paddle1_y)
    draw_paddle(paddle2_x, paddle2_y)
    stdscr.addstr(ball_y, ball_x, BALL_CHAR)
    stdscr.addstr(0, 0, f"Player 1: {score1} | Player 2: {score2}")

    # refresh screen
    stdscr.refresh()

    # wait a bit before updating again
    time.sleep(0.05)

# clean up ncurses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
