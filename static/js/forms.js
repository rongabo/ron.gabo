function isNumber(str) {
    var pattern = /^\d+$/;
    return pattern.test(str);
}
function isEmail(str) {
    var pattern =/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return pattern.test(str);
}

function validateMyForm() {
    let ID = document.forms["MyForm"]["id"].value;
    if (ID.length != 9 || !isNumber(ID)) {
        alert('You need 9 numbers in ID');
        return false;
    }

    let Email = document.forms["MyForm"]["email"].value
    if (!isEmail(Email)) {
        alert("Email entered is not valid. Please enter a valid Email.");
        return false;
    }

    
  }