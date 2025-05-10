from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point, width: int = 2):
        self.__point1: Point = p1
        self.__point2: Point = p2
        self.__width = width

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=self.__width,
        )


class Window:

    def __init__(self, width: int, height: int):
        self.background_color = "white"
        self.foreground_color = "black"
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(width=width, height=height, bg=self.background_color)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill_color = None):
        if fill_color is None:
            fill_color = self.foreground_color
        line.draw(self.__canvas, fill_color)
