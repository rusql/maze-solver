import time
from cell import Cell
from graphics import Point, Window


class Maze:
    def __init__(
            self,
            x1 : float,
            y1 :float,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window,
        ):
        
        self._x1: float = x1
        self._y1: float = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win:Window = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        col = []
        for col_num in range(self._num_cols): 
            self._cells.append(col)
            for row_num in range(self._num_rows):
                col.append(Cell(self._win))

        for col_num in range(self._num_cols): 
            for row_num in range(self._num_rows):
                self._draw_cell(col_num, row_num)
        
    def _draw_cell(self, col:int, row:int):
        cell = self._cells[col][row]

        y1 = row * self._cell_size_y
        y2 = (row * self._cell_size_y)+self._cell_size_y 
        x1 = (col * self._cell_size_x)
        x2 = (col * self._cell_size_x)+self._cell_size_x

        x1 += self._x1
        x2 += self._x1
        y1 += self._y1
        y2 += self._y1

        cell.draw(Point(x1, y1), Point(x2, y2))
        self._animate()

    def _animate(self, time_delay: float = 0.05):
        self._win.redraw()
        time.sleep(time_delay)

if __name__ == "__main__":
    win = Window(800,600)
    m = Maze(0, 0, 3, 3, 10, 10, win)