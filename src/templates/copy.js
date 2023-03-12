function copyFunction(){
    var copyText = document.getElementById("finalResult");

    //Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    //copy = copyText.textContent;
     // Copy the text inside the text field
    navigator.clipboard.writeText(copyText);
  
    // Alert the copied text
    alert("Copied!");
  }
