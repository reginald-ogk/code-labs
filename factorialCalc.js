/* Factorial Calculator
   This script calculates the factorial of a given number
   and logs the result to the console.
*/


const num = 5;
function factorialCalculator(number) {
  let result = 1;
  for (let i = 1; i <= number; i++) {
    result = result * i;
  }

  return result;
}

const factorial = factorialCalculator(num);

const resultMsg = `Factorial of ${num} is ${factorial}`;

console.log(resultMsg);