import curses

BOX_DRAWING_CHARS = {
    'N': {
        'N': '┃',
        'E': '┏',
        'S': '┃',
        'W': '┓',
    },
    'E': {
        'N': '┛',
        'E': '━',
        'S': '┓',
        'W': '━',
    },
    'S': {
        'N': '┃',
        'E': '┗',
        'S': '┃',
        'W': '┛',
    },
    'W': {
        'N': '┗',
        'E': '━',
        'S': '┏',
        'W': '━',
    },
}

KEY_TO_DIR = {
    'KEY_RIGHT': 'E',
    'KEY_LEFT': 'W',
    'KEY_UP': 'N',
    'KEY_DOWN': 'S'
}

MOVE = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}

def main(stdscr: curses.window):
    # Clear screen
    stdscr.clear()

    x, y = 0, 0
    last = 'E'
    draw = False
    prev = None
    while True:
        if prev == None:
            prev = chr(stdscr.inch(y, x))
        stdscr.addstr(y, x, '░')
        key = stdscr.getkey()
        if key == ' ':  
            draw = not draw
        elif key in KEY_TO_DIR:
            direction = KEY_TO_DIR[key]
            if draw:
                stdscr.addstr(y, x, BOX_DRAWING_CHARS[last][direction])
            else:
                stdscr.addstr(y, x, prev)
            prev = None
            dx, dy = MOVE[direction]
            x += dx
            y += dy
            last = direction
        else:
            break
        

    stdscr.refresh()
    stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
    
    
    

