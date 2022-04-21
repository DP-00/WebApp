let i = 0;
function heroText(){
  let text=["modern", "healthy", "urban", "individual", "free", "hipster", "authentic", "modern", "modern", "modern", "modern"];
  let textLen = text.length;
  document.getElementById('heroText').innerText = text[i%textLen];
  i++;            
}
setInterval(heroText, 500);