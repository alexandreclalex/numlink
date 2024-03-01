import curses

BOX_DRAWING_CHARS = {
    ('S', 'N'): '┃',
    ('N', 'S'): '┃',
    ('E', 'W'): '━',
    ('W', 'E'): '━',
    ('S', 'E'): '┏',
    ('E', 'S'): '┏',
    ('S', 'W'): '┓',
    ('W', 'S'): '┓',
    ('N', 'E'): '┛',
    ('E', 'N'): '┛',
    ('N', 'W'): '┗',
    ('W', 'N'): '┗',
}

def main(stdscr: curses.window):
    # Clear screen
    stdscr.clear()

    x, y = 0, 0
    last = 'E'
    
    while True:
        key = stdscr.getkey()
        stdscr.addstr(0, 0, key)
        

    stdscr.refresh()
    stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
    
    
    

