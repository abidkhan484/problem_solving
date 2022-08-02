const arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170];
const X = 110;

const binarySearch = (arr, X) => {
  var start = 0,
    end = arr.length - 1,
    mid;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    if (arr[mid] == X) {
      return true;
    } else if (arr[mid] < X) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return false;
};

// const resultStatus = binarySearch(arr, X);
// console.log(`The value ${X} in the arr is: ${resultStatus}`);

module.exports = binarySearch;
