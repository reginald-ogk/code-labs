/* Chunky Monkey
   This function splits an array into groups of a specified size
   and returns a two-dimensional array.
*/

function chunkArrayInGroups(arr, number) {
  const result = [];

  for (let i = 0; i < arr.length; i += number) {
    result.push(arr.slice(i, i + number));
  }

  return result;
}