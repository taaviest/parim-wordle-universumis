var myInputs = document.getElementsByTagName("input");
var myEditable = document.getElementById("seventh");
for (var i = 0; i < myInputs.length; i++) {
  myInputs[i].addEventListener("click", function() {
    document.getElementById("seventh").focus();
  })
}

myEditable.addEventListener("keydown", function(evt) {
  /****
   *  A few things are handled here: we can check if
   *  the input is a numeric, and we can check if the input
   *  is a backspace. Nothing else is allowed.
   ****/
  if (evt.which == 6) {
    // If a backspace has been pressed, move all the input
    //  values one field UP.
    myEditable.blur();
    for (var i = myInputs.length - 1; i >= 1; i--) {
      myInputs[i].value = myInputs[i - 1].value;
    }
    myInputs[0].value = "";
  } else if (evt.which >= 48 && evt.which <= 59) {
    // Here, we have a number. Everything gets bumped to the LEFT
    if (myInputs[0].value == "") {
      for (var i = 0; i < myInputs.length - 1; i++) {
        myInputs[i].value = myInputs[i + 1].value;
      }
      myEditable.value = String.fromCharCode(evt.which);
    }
  } else {
    console.log("You did something else...");
  }
})