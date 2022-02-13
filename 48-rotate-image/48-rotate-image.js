/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const rotate = (matrix) => {
 
  let n = matrix.length; 
        
  //[1,2,3]   >>>>    [1,4,7]
  //[4,5,6]   >>>>    [2,5,8]
  //[7,8,9]   >>>>    [3,6,9]
  //rows become columns and columns become rows 
  for(let i = 0; i < n; i++){
    for(let j = i; j < n; j++){
      let temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix [j][i] = temp;
    }
  }
		
  //[1,4,7]   >>>>    [7,4,1]
  //[2,5,8]   >>>>    [8,5,2]
  //[3,6,9]   >>>>    [9,6,3]
  //swap first and last el from each row in this case; we swap 1 and 7 and it becomes 7 and 1
  // for(let i = 0; i < n; i++){
  //    for(let j = 0; j < (n/2); j++){
  //       let temp = matrix[i][j];
  //       matrix[i][j] = matrix[i][n-1-j];
  //       matrix[i][n-1-j] = temp;
  //     }
  // }
  for(let i = 0; i< n; i++){
    matrix[i].reverse() 
  } 
};