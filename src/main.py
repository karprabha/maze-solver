import sys
from maze import Maze
from window import Window

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    sys.setrecursionlimit(10000)
    seed_for_debug = 10
    # maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed_for_debug)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()

if __name__ == "__main__":
    main()
