from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Line:
    def __init__(self, p1: Point, p2: Point, width: int = 2):
        self.__point1: Point = p1
        self.__point2: Point = p2
        self.__width = width

    def draw(self, canvas: Canvas, fill_color: str):
        # canvas.create_line(1, 1, 2, 2, fill=fill_color, width=2)
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
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(width=width, height=height)
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

    def draw_line(self, line: Line, fill_color: str = "white"):
        line.draw(self.__canvas, fill_color)


class Cell:
    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1: float = None
        self._x2: float = None
        self._y1: float = None
        self._y2: float = None
        self._win = window

    def draw(self, top_left_position: Point, bottom_right_position: Point):
        if self.has_top_wall:
            top_wall = Line(
                Point(top_left_position.x, top_left_position.y),
                Point(bottom_right_position.x, top_left_position.y),
            )
            self._win.draw_line(top_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(
                Point(top_left_position.x, bottom_right_position.y),
                Point(bottom_right_position.x, bottom_right_position.y),
            )
            self._win.draw_line(bottom_wall)

        if self.has_right_wall:
            right_wall = Line(
                Point(bottom_right_position.x, top_left_position.y),
                Point(bottom_right_position.x, bottom_right_position.y),
            )
            self._win.draw_line(right_wall)

        if self.has_left_wall:
            left_line = Line(
                Point(top_left_position.x, top_left_position.y),
                Point(top_left_position.x, bottom_right_position.y),
            )
            self._win.draw_line(left_line)
