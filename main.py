from graphics import Window
from maze import Maze

def main():
    margin = 10
    win = Window(800,600)
    Maze(x1=margin, y1=margin, num_rows=5, num_cols=5, cell_size_x=50, cell_size_y=50, win=win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
