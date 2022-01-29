/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = (grid) => {
  
  const height = grid.length;
  const width = grid[0].length;
  const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  let count = 0;
  // define island traversal function
  const traverse = (row, col) => { 
    // return if outside boundaries or if coordinate is water/already visited ('0')
    if (row < 0 || row >= height || col < 0 || col >= width || grid[row][col] === '0') return; 
    grid[row][col] = '0'; // else mark island '1' as visited '0'...
    for (let dir of directions) {
      traverse(row + dir[0], col + dir[1]); // and traverse left, up, right, down
    }
  }

  for (let i = 0; i < height; i++) { // iterate through matrix rows
    for (let j = 0; j < width; j++) { // iterate through matrix columns
      if (grid[i][j]==='1') { // if coordinate is an island ('1')...
          traverse(i, j); // explore surrounding coordinates
          count++; // and increment island count
      }
    }
  }
  return count; // return total island count
};