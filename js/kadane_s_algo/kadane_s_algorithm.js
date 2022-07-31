/* 
Problem: Write an efficient program to find the sum of the contiguous 
subarray within a one-dimensional array of numbers that has the largest sum. 
*/

const arr = [-2, -3, 4, -1, -2, 1, 5, -3];

const kadaneSAlgorithm = (arr) => {
  if (!arr.length) return 0;

  return arr.reduce(
    (prev, curr) => {
      var maxEndHere = Math.max(curr, curr + prev.maxEndHere);
      var maxSoFar = Math.max(maxEndHere, prev.maxSoFar);
      return {
        maxEndHere,
        maxSoFar,
      };
    },
    {
      maxEndHere: Number.NEGATIVE_INFINITY,
      maxSoFar: Number.NEGATIVE_INFINITY,
    }
  ).maxSoFar;
};

const largestSumContiguousSubarray = kadaneSAlgorithm(arr);
console.log(`Largest sum contiguous subarray ${largestSumContiguousSubarray}`);
