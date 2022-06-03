// function to change text in the hero section

let i = 0;
function heroText(){
  let text=["modern", "healthy", "urban", "individual", "free", "hipster", "authentic", "modern", "modern", "modern", "modern"];
  let textLen = text.length;
  
  // looping over the array using modulo and increasing counter 
  
  document.getElementById('heroText').innerText = text[i%textLen];
  i++;            
}

// text changes every 500 milliseconds

setInterval(heroText, 500);
