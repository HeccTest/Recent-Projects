// Change all buttons to have red text
// Move the Alternative treatment button to the end of the button set.
// Add a hover state to change to green text and back


const buttons = document.querySelectorAll("button") // create a nodelist of all button elements

for(let i = 0; i < buttons.length; i++) // iterate through the entire button nodelist
{
    buttons[i].style.color = "red" // set text to red
    buttons[i].addEventListener('mouseout', function() {
        buttons[i].style.color = "red" // if mouse moves out of element, make text red
    });
    buttons[i].addEventListener('mouseover', function() {
        buttons[i].style.color = "green" // if mouse moves over element (hover), make text green
    });
}

buttons[0].parentElement.appendChild(buttons[0]) // append the "alternative treatment" button to the parentElement (the div box). This will move the element to the end of the button set.