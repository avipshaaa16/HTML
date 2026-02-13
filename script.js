function myfunction() {
    var a = 19;
    document.getElementById("result").innerHTML = a + a;
}
function validate(e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msg = document.getElementById("message");
    let message = "";
    if (email === "") {
        message = "Pls enter a correct email";
        msg.style.color = "red";
    }
    else if (password === "") {
        message = "Password must contain 8 characters";
        msg.style.color = "red";
    }
    else if (age === "") {
        message = "Age should be above 5";
        msg.style.color = "red";
    }
    else {
        message = "Login successful";
        msg.style.color = "green";
    }
    msg.innerHTML = message;
}
document.getElementById("loginform").onsubmit = validate;
document.getElementById("email").oninput = () => validate({ preventDefault: () => { } })
document.getElementById("password").oninput = () => validate({ preventDefault: () => { } })
document.getElementById("age").oninput = () => validate({ preventDefault: () => { } })