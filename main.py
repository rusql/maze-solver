from graphics import Window
from maze import Maze

def main():
    margin = 10
    win = Window(1024,768)
    Maze(x1=margin, y1=margin, num_rows=35, num_cols=35, cell_size_x=20, cell_size_y=20, win=win)    
    win.wait_for_close()

if __name__ == "__main__":
    main()
