/*
Problem: Given an array of integers of size ‘n’, Our aim is to calculate 
the maximum sum of ‘k’ consecutive elements in the array.
*/

const arr = [1, 4, 2, 10, 23, 3, 1, 0, 20];
const K = 4;

const slidingWindowTechnique = (arr, K) => {
  const length = arr.length;
  if (length < K) return 0;

  var currentMax = 0;
  for (var i = 0; i < K; i++) {
    currentMax += arr[i];
  }
  var maxSoFar = currentMax;

  for (var i = 0; i < length - K; i++) {
    currentMax = currentMax + arr[K] - arr[i];
    maxSoFar = Math.max(maxSoFar, currentMax);
    K++;
  }

  return maxSoFar;
};

const maximumSumOfKConsecutiveElements = slidingWindowTechnique(arr, K);
console.log(`Maximum sum of K consecutive elements ${maximumSumOfKConsecutiveElements}`);
