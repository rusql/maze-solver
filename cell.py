from graphics import Line, Point, Window


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

        self._x1 = top_left_position.x
        self._y1 = top_left_position.y
        self._x2 = bottom_right_position.x
        self._y2 = bottom_right_position.y

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
            left_wall = Line(
                Point(top_left_position.x, top_left_position.y),
                Point(top_left_position.x, bottom_right_position.y),
            )
            self._win.draw_line(left_wall)

    def draw_move(self, to_cell, undo=False):
        from_point = Point(
            self._x1 + abs((self._x2 - self._x1) // 2),
            self._y1 + abs((self._y2 - self._y1) // 2),
        )
        to_point = Point(
            to_cell._x1 + abs((to_cell._x2 - to_cell._x1) // 2),
            to_cell._y1 + abs((to_cell._y2 - to_cell._y1) // 2),
        )

        line = Line(from_point, to_point)
        line_colour = "red"
        if undo:
            line_colour = "gray"
        self._win.draw_line(line, line_colour)
