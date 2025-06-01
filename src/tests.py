import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_cell_size(self):
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, 12, 10, cell_size_x, cell_size_y)
        self.assertEqual(
            m1._Maze__cell_size_x,
            cell_size_x,
        )
        self.assertEqual(
            m1._Maze__cell_size_y,
            cell_size_y,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        visited = False
        for col in range(num_cols):
            for row in range(num_rows):
                visited |= m1._Maze__cells[col][row].visited

        self.assertEqual(
            visited,
            False,
        )

if __name__ == "__main__":
    unittest.main()
