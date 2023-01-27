const rowList = document.querySelectorAll(".row"); // returns an array of all the row elements

function itemDraggedOver(event)
{
  event.preventDefault(); // supresses the default action of onDragOver. Allows us to overwrite and do things
}

function itemDropped(event)
{
  event.preventDefault();
  const cardID = event.dataTransfer.getData("id"); // get data and store in variable called cardID
  const draggedCard = document.getElementById(cardID); // on card drop find the element with id = cardID
  event.target.appendChild(draggedCard); // add to event. Event would be the row we dropped our item on
}

rowList.forEach((row) => {
  row.ondragover = itemDraggedOver; // when the row is dragged call the function onDragOver
  row.ondrop = itemDropped;
})
