/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // Negative numbers are not palindromes
    if (x < 0) return false;

    // Convert the number to a string
    const str = x.toString();

    // Check if the string is equal to its reverse
    return str === str.split('').reverse().join('');
};
