// Determines if a given year is a leap year
// Usage: isLeapYear(2020) returns "2020 is a leap year."
// Usage: isLeapYear(2021) returns "2021 is not a leap year."

let year = 2024;

function isLeapYear(year) {
  const leap = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;

  return leap ? `${year} is a leap year.` : `${year} is not a leap year.`;
}

const result = isLeapYear(year);
console.log(result);