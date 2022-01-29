const numIslands = (grid: string[][]): number => {
  let count = 0;
  const n = grid.length;
  const m = grid[0].length;
  const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  // initialize recursive, traversal function
  const DFS = (row: number, col: number): number => {
    // base: if traversing outside boundaries or if island/water is found, exit recursive
    if (row < 0 || row >= n || col < 0 || col >= m || grid[row][col]==='0') return;
    grid[row][col] = '0'; // mark island as visited
    for (let dir of directions) DFS(row + dir[0], col + dir[1]); // traverse in each direction
  }
  // iterate through matrix
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < m; col++) {
      if (grid[row][col]==='1') { // if island is found...
        DFS(row, col); // traverse island
        count++; // increment count
      }
    }
  }
  return count; // return total count
};