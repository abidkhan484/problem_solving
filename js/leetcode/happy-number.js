/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  const initialNumberList = [];
  number = n;
  while (number != 1) {
    n = number;
    number = 0;
    while (n != 0) {
      number += Math.pow(n % 10, 2);
      n = Math.floor(n / 10);
    }

    if (initialNumberList.includes(number)) {
      break;
    }

    initialNumberList.push(number);
  }
  return number == 1 ? true : false;
};

module.exports = isHappy;
