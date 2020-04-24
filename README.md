# Maze Generation with Recursive backtracker
Implemented using PyGame module in python.

## Recursive backtracker
1. Make the initial cell the current cell and mark it as visited
2. While there are unvisited cells
      1. If the current cell has any neighbours which have not been visited
            1. Choose randomly one of the unvisited neighbours 
            2. Push the current cell to the stack
            3. Remove the wall between the current cell and the chosen neighbour cell
            4. Make the chosen cell the current cell and mark it as visited
      2. Else if stack is not empty
            1. Pop a cell from the stack
            2. Make it the current cell

Reference : https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
