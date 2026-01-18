// Function to find the length of the longest word in a sentence


function findLongestWordLength(sentence) {
  const words = sentence.split(" ");
  let longestLength = 0;

  for (const word of words) {
    if (word.length > longestLength) {
      longestLength = word.length
    }
  }

  return longestLength;
} 