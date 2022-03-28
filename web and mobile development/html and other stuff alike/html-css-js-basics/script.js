window.addEventListener("load", function ()
{
  let counter = 0;

// camelCase?
function buttonClicked()
  {
    counter++;

    let clickedCounterElement = document.getElementById("click_counter");

    clickedCounterElement.innerHTML = "Clicked " + counter + " times!";
  }

  let clickedButtonElement = document.getElementById("click_button");

  clickedButtonElement.addEventListener("click", buttonClicked);
});