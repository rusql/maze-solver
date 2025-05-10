import time
import random
from typing import Optional, List, Tuple
from cell import Cell
from graphics import Point, Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Optional[Window] = None,
        seed=None,
    ):
        if seed is not None:
            random.seed(seed)
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Optional[Window] = win
        self._cells:List[List[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve()

    def _solve (self):
        self._solve_r(0,0)

    def _solve_r(self, i:int, j:int) -> bool:        
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        unblocked_neighbours = self._unblocked_neighbours(i,j)
        unvisited_accessable_neighbours = list(filter(lambda xy: not self._cells[xy[0]][xy[1]].visited, unblocked_neighbours))
        for neighbour in unvisited_accessable_neighbours:
            neighbour_cell = self._cells[neighbour[0]][neighbour[1]]
            self._cells[i][j].draw_move(neighbour_cell)
            if self._solve_r(neighbour[0], neighbour[1]):
                return True
            self._cells[i][j].draw_move(neighbour_cell, undo=True)
        return False
                



    def _unblocked_neighbours(self, x:int, y:int):
        unblocked_neighbours:List[Tuple[int, int]] = []
        ## Above neighbour
        if y > 0 and not self._cells[x][y].has_top_wall and not self._cells[x][y-1].has_bottom_wall:
            unblocked_neighbours.append((x, y-1))
        ## Below neighbour
        if y < self._num_rows - 1 and not self._cells[x][y].has_bottom_wall and not self._cells[x][y+1].has_top_wall:
            unblocked_neighbours.append((x, y+1))
        ## Left neighbour
        if x > 0 and not self._cells[x][y].has_left_wall and not self._cells[x-1][y].has_right_wall:
            unblocked_neighbours.append((x-1, y))
        ## Right neighbour
        if x < self._num_rows - 1 and not self._cells[x][y].has_right_wall and not self._cells[x+1][y].has_left_wall:
            unblocked_neighbours.append((x+1, y))

        return unblocked_neighbours

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_cells = self._get_adjacent_cells(i, j)
            possible_directions = list(
                filter(lambda xy: not self._cells[xy[0]][xy[1]].visited, adjacent_cells)
            )
            if len(possible_directions) == 0:
                self._draw_cell(i, j, 0)
                return
            chosen_wall_index = 0
            if len(possible_directions) > 0:
                chosen_wall_index = random.randint(0, len(possible_directions) - 1)
                new_cell_x, new_cell_y = possible_directions[chosen_wall_index]
                self._break_wall(i, j, new_cell_x, new_cell_y)
                self._break_walls_r(new_cell_x, new_cell_y)

    def _break_wall(self, x1, y1, x2, y2):
        # cell 2 left of cell 1
        if x2 == x1 - 1 and y1 == y2:
            self._cells[x1][y1].has_left_wall = False
            self._cells[x2][y2].has_right_wall = False

        # cell 2 right of cell 1
        elif x2 == x1 + 1 and y1 == y2:
            self._cells[x1][y1].has_right_wall = False
            self._cells[x2][y2].has_left_wall = False

        # cell 2 above cell 1
        elif y2 == y1 - 1 and x1 == x2:
            self._cells[x1][y1].has_top_wall = False
            self._cells[x2][y2].has_bottom_wall = False

        # cell 2 below cell 1
        elif y2 == y1 + 1 and x1 == x2:
            self._cells[x1][y1].has_bottom_wall = False
            self._cells[x2][y2].has_top_wall = False


    def _get_adjacent_cells(self, i: int, j: int) -> List[Tuple[int, int]]:
        adjacent_cells: List[Tuple[int,int]] = []

        # up
        if j > 0 and self._num_rows > 1:
            adjacent_cells.append((i, j - 1))
        # down
        if j < self._num_rows - 1 and self._num_rows > 1:
            adjacent_cells.append((i, j + 1))
        # left
        if i > 0 and self._num_cols > 1:
            adjacent_cells.append((i - 1, j))
        # right
        if i < self._num_cols - 1 and self._num_cols > 1:
            adjacent_cells.append((i + 1, j))
        return adjacent_cells

    def _create_cells(self) -> None:
        for col_num in range(self._num_cols):
            col:List[Cell] = []
            self._cells.append(col)
            for row_num in range(self._num_rows):
                col.append(Cell(self._win))

        if self._win is None:
            return

        for col_num in range(self._num_cols):
            for row_num in range(self._num_rows):
                self._draw_cell(col_num, row_num, 0)

    def _draw_cell(self, col: int, row: int, time_delay: float = 0.05):
        if self._win is None:
            return

        cell = self._cells[col][row]

        y1 = row * self._cell_size_y
        y2 = (row * self._cell_size_y) + self._cell_size_y
        x1 = col * self._cell_size_x
        x2 = (col * self._cell_size_x) + self._cell_size_x

        x1 += self._x1
        x2 += self._x1
        y1 += self._y1
        y2 += self._y1

        cell.draw(Point(x1, y1), Point(x2, y2))
        self._animate(time_delay)

    def _animate(self, time_delay: float = 0.05):
        if self._win is not None:
            self._win.redraw()
        if time_delay > 0:
            time.sleep(time_delay)

    def _break_entrance_and_exit(self) -> None:
        entrance_cell: Cell = self._cells[0][0]
        exit_cell: Cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        entrance_cell.redraw()
        exit_cell.redraw()

    def _reset_cells_visited(self):
        for col_num in range(self._num_cols):
            for row_num in range(self._num_rows):
                self._cells[col_num][row_num].visited = False


if __name__ == "__main__":
    win = Window(800, 600)
    m = Maze(
        x1=4, y1=4, num_rows=2, num_cols=2, cell_size_x=10, cell_size_y=10, win=win
    )
