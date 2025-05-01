from graphics import Window, Point
from cell import Cell

def main():
    win = Window(800,600)
    cell = Cell(win)
    cell.draw(Point(10,10), Point(30,30))

    cell.has_right_wall = False
    cell.draw(Point(30,30), Point(40,40))

    cell.has_right_wall = True
    cell.has_top_wall = False
    cell.draw(Point(100,100), Point(200,200))

    cell.has_top_wall = True
    cell.has_left_wall = False
    cell.draw(Point(200,200), Point(300,300))

    win.wait_for_close()

if __name__ == "__main__":
    main()  