import curses
import time

# initialize ncurses
stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()

# set up ball properties
ball_x = 0
ball_y = 0
ball_vx = 1
ball_vy = 1
ball_char = 'O'

# loop to animate ball
while True:
    # clear screen
    stdscr.clear()

    # move ball
    ball_x += ball_vx
    ball_y += ball_vy

    # check ball bounds
    if ball_x >= curses.COLS - 1:
        ball_vx = -1
    elif ball_x <= 0:
        ball_vx = 1

    if ball_y >= curses.LINES - 1:
        ball_vy = -1
    elif ball_y <= 0:
        ball_vy = 1

    # draw ball
    stdscr.addstr(ball_y, ball_x, ball_char)

    # refresh screen
    stdscr.refresh()

    # wait a bit before updating again
    time.sleep(0.1)

# clean up ncurses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
