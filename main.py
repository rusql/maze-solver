from graphics import Window, Line, Point

def main():
    win = Window(800,600)
    win.draw_line(Line(Point(100, 100), Point(200, 200)), "white")
    win.draw_line(Line(Point(50, 50), Point(50, 500)), "white")
    #win.draw_line(Line(Point(1, 1), Point(100, 100)), "white")
    win.wait_for_close()

if __name__ == "__main__":
    main()  