// emailMasker.js
// This file contains a function to mask email addresses

function maskEmail(email) {
  const atIndex = email.indexOf("@");

  const username = email.slice(0, atIndex);
  const domain = email.slice(atIndex);

  const firstChar = username[0];
  const lastChar = username[username.length - 1];
  const stars = "*".repeat(username.length - 2); // Mask all but first and last character

  return firstChar + stars + lastChar + domain;
}


const email = "reginaldgyasi62@gmail.com";
console.log(maskEmail(email));