const cards = document.querySelectorAll(".card");

function itemDragged(event) 
{
  event.dataTransfer.setData("id", event.target.id); // send data
}

cards.forEach((card) => {
  card.ondragstart = itemDragged;
});
