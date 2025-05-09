import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        num_cols = 1
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        num_cols = 3
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_adjacent_cells(self):
        num_cols = 3
        num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        adjacent_cells = maze._get_adjacent_cells(1, 1)
        self.assertListEqual(
            [(1, 0), (1, 2), (0, 1), (2, 1)],
            adjacent_cells,
        )

        num_cols = 2
        num_rows = 1
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        adjacent_cells = maze._get_adjacent_cells(1, 0)
        self.assertListEqual([(0, 0)], adjacent_cells)

        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        adjacent_cells = maze._get_adjacent_cells(1, 1)
        self.assertListEqual([(1, 0), (0, 1)], adjacent_cells)

        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        adjacent_cells = maze._get_adjacent_cells(1, 0)
        self.assertEqual([(1, 1), (0, 0)], adjacent_cells)

        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        adjacent_cells = maze._get_adjacent_cells(0, 0)
        self.assertEqual([(0, 1), (1, 0)], adjacent_cells)

        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        adjacent_cells = maze._get_adjacent_cells(0, 1)
        self.assertEqual([(0, 0), (1, 1)], adjacent_cells)

    def test_cells_visited(self):
        maze = Maze(x1=0, y1=0, num_rows=2, num_cols=2, cell_size_x=10, cell_size_y=10)
        for col_num in range(maze._num_cols):
            for row_num in range(maze._num_rows):
                self.assertEqual(maze._cells[col_num][row_num].visited, False)


if __name__ == "__main__":
    unittest.main()
