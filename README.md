# Maze Solver

A Python-based maze generator and solver with graphical visualization using Tkinter. This project creates random mazes using recursive backtracking and solves them using depth-first search (DFS) algorithm.

## Features

- **Random Maze Generation**: Uses recursive backtracking algorithm to generate unique, solvable mazes
- **Visual Maze Solving**: Real-time visualization of the maze-solving process
- **Customizable Parameters**: Adjustable maze dimensions, cell sizes, and window dimensions
- **Interactive GUI**: Built with Tkinter for cross-platform compatibility
- **Animated Solution**: Shows the path-finding process with visual feedback
- **Comprehensive Testing**: Unit tests to ensure maze generation correctness

## Demo

The program generates a random maze and then solves it step-by-step:

- **Black lines**: Maze walls
- **White gaps**: Open passages
- **Red line**: Current solution path being explored
- **Gray line**: Backtracked (dead-end) paths

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- No external dependencies required

## Installation

1. Clone the repository:

```bash
git clone https://github.com/karprabha/maze-solver.git
cd maze-solver
```

2. Ensure you have Python 3 installed:

```bash
python3 --version
```

## Usage

### Running the Maze Solver

**Option 1: Using the shell script**

```bash
./main.sh
```

**Option 2: Direct Python execution**

```bash
python3 src/main.py
```

### Running Tests

**Option 1: Using the test script**

```bash
./test.sh
```

**Option 2: Direct test execution**

```bash
python3 -m unittest discover -s src
```

## How It Works

### Maze Generation

1. **Initialization**: Creates a grid of cells, each with four walls
2. **Entrance/Exit**: Removes the top wall of the starting cell and bottom wall of the ending cell
3. **Recursive Backtracking**:
   - Starts from the top-left corner (0,0)
   - Randomly chooses an unvisited neighboring cell
   - Removes the wall between current and chosen cell
   - Recursively continues until all cells are visited

### Maze Solving

1. **Depth-First Search**: Explores paths from start to finish
2. **Visualization**:
   - Red lines show the current path being explored
   - Gray lines show backtracked dead-end paths
3. **Backtracking**: When hitting a dead end, the algorithm backtracks and tries alternative routes

## Configuration

You can modify the maze parameters in `src/main.py`:

```python
num_rows = 12        # Number of rows in the maze
num_cols = 16        # Number of columns in the maze
margin = 50          # Border margin around the maze
screen_x = 800       # Window width
screen_y = 600       # Window height
```

For debugging purposes, you can also set a specific seed:

```python
seed_for_debug = 10
maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed_for_debug)
```

## Project Structure

```
maze-solver/
├── src/
│   ├── main.py      # Entry point of the application
│   ├── maze.py      # Main maze class with generation and solving logic
│   ├── cell.py      # Individual maze cell implementation
│   ├── window.py    # Tkinter window wrapper for graphics
│   ├── line.py      # Line drawing utility
│   ├── point.py     # Point coordinate utility
│   └── tests.py     # Unit tests for maze functionality
├── main.sh          # Shell script to run the application
├── test.sh          # Shell script to run tests
└── README.md        # This file
```

## Algorithm Details

### Recursive Backtracking (Maze Generation)

- **Time Complexity**: O(n) where n is the number of cells
- **Space Complexity**: O(n) for the recursion stack
- Guarantees a perfect maze (exactly one path between any two cells)

### Depth-First Search (Maze Solving)

- **Time Complexity**: O(V + E) where V is vertices (cells) and E is edges (passages)
- **Space Complexity**: O(V) for the recursion stack
- Finds a solution if one exists, though not necessarily the shortest path

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

The project includes comprehensive unit tests that verify:

- Correct maze cell creation and dimensions
- Proper entrance and exit wall removal
- Cell visiting state management
- Maze generation parameters

Run the tests to ensure everything works correctly:

```bash
./test.sh
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [karprabha](https://github.com/karprabha)

## Acknowledgments

- Inspired by classic maze generation and pathfinding algorithms
- Built as a learning project to understand recursive algorithms and computer graphics
