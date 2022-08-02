const { describe, it } = require("mocha");
const { expect } = require("chai");

const binarySearch = require("../../binary_search/binary_search");

describe("Binary search result exists", function () {
  it("should return TRUE in the output", function () {
    var result = binarySearch(
      [10, 20, 30, 50, 60, 80, 110, 130, 140, 170],
      110
    );
    expect(result).to.be.true;
  });
});

describe("Binary search result exists", function () {
  it("should return FALSE in the output", function () {
    var result = binarySearch([10, 20, 30, 50, 60, 80, 110, 130, 140, 170], 90);
    expect(result).to.be.false;
  });
});
