/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    const j = nums.indexOf(complement, i + 1); // Start searching from the next index to avoid using the same element twice

    if (j !== -1) {
      return [i, j];
    }
  }
};
