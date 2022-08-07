const { describe, it } = require("mocha");
const { expect } = require("chai");

const happyNumber = require("./../leetcode/happy-number");

describe("Happy Number exists", () => {
  it("Should return True in the output", () => {
    const numbers = [19, 7];
    numbers.forEach((number) => {
      var result = happyNumber(number);
      expect(result).to.be.true;
    });
  });
});

describe("Happy Number not exists", () => {
  it("Should return False in the output", () => {
    const numbers = [2];
    numbers.forEach((number) => {
      var result = happyNumber(number);
      expect(result).to.be.false;
    });
  });
});
