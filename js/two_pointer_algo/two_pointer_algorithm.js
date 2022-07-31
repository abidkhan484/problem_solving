/*
Problem: Given a sorted array A (sorted in ascending order), having N integers, 
find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
*/

const arr = [10, 20, 35, 50, 75, 80];
const X = 110;

const isPairSum = (arr, X) => {
  var length = arr.length;
  var firstPointer = 0;
  var secondPointer = length - 1;

  var currentSum;
  while (firstPointer < secondPointer) {
    currentSum = arr[firstPointer] + arr[secondPointer];
    if (currentSum === X) {
      return true;
    } else if (currentSum > X) {
      secondPointer--;
    } else {
      firstPointer++;
    }
  }
  return false;
};

const result = isPairSum(arr, X);
console.log(`Sum of two value of an array is matched with ${X}: Status(${result})`);
