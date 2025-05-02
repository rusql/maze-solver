from cell import Cell
from graphics import Point, Window
from maze import Maze

def main():
    margin = 4
    win = Window(800, 600)
    Maze(x1=margin, y1=margin, num_rows=5, num_cols=2, cell_size_x=10, cell_size_y=10, win=win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
