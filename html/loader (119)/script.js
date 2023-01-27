const loader = document.getElementById("loader");
const content = document.getElementById("content");

let blueValue = 230;
let redValue = 106;
let direction = 1;


function start(){
  // const timer = setTimeout(displayContent, 25000); // will run the function displayContent after 25000 miliseconds (25 seconds)
  const myFunc = setInterval(function () {
    if(blueValue <= 0 || blueValue >= 255){
      direction = direction * -1; // reverse direction
    }

    blueValue = blueValue + direction;
    redValue += 1;

    loader.style.borderTopColor = "rgb(106, 151,"+blueValue+")";
    loader.style.borderBottomColor = "rgb(106, 151,"+blueValue+")";
  }, 10);
}

// "rgb(" + redValue + ",151," + blueValue + ")";
