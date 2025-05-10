from typing import Optional
from graphics import Line, Point, Window


class Cell:
    def __init__(self, window: Optional[Window]):
        self.has_left_wall: bool = True
        self.has_right_wall:bool = True
        self.has_top_wall:bool = True
        self.has_bottom_wall = True
        self.visited:bool = False
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = window

        self._undo_color = "gray"
        self._forward_color = "red"

    def redraw(self):
        self.draw(
            Point(self._x1, self._y1),
            Point(self._x2, self._y2),
        )

    def draw(self, top_left_position: Point, bottom_right_position: Point):

        self._x1 = top_left_position.x
        self._y1 = top_left_position.y
        self._x2 = bottom_right_position.x
        self._y2 = bottom_right_position.y

        if self._win is None:
            return
        
        top_wall = Line(
            Point(top_left_position.x, top_left_position.y),
            Point(bottom_right_position.x, top_left_position.y),
        )
        if self.has_top_wall:
            self._win.draw_line(top_wall, self._win.foreground_color)
        else:
            self._win.draw_line(top_wall, self._win.background_color)

        bottom_wall = Line(
            Point(top_left_position.x, bottom_right_position.y),
            Point(bottom_right_position.x, bottom_right_position.y),
        )
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, self._win.foreground_color)
        else:
            self._win.draw_line(bottom_wall, self._win.background_color)

        right_wall = Line(
            Point(bottom_right_position.x, top_left_position.y),
            Point(bottom_right_position.x, bottom_right_position.y),
        )
        if self.has_right_wall:
            self._win.draw_line(right_wall, self._win.foreground_color)
        else:
            self._win.draw_line(right_wall, self._win.background_color)

        left_wall = Line(
            Point(top_left_position.x, top_left_position.y),
            Point(top_left_position.x, bottom_right_position.y),
        )
        if self.has_left_wall:
            self._win.draw_line(left_wall, self._win.foreground_color)
        else:
            self._win.draw_line(left_wall, self._win.background_color)

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
        line_colour = self._forward_color
        if undo:
            line_colour = self._undo_color
        if self._win is not None:
            self._win.draw_line(line, line_colour)
