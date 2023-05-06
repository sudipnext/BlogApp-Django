const userName = document.getElementById("username");
const passWord = document.getElementById("password")
const userError = document.getElementById("userError");
const passError = document.getElementById("passError");
function validateEmail() {
  const emailInput = document.getElementById("email");
  const emailError = document.getElementById("emailError");
  const emailRegex = /^\S+@\S+\.\S+$/;

  if (!emailRegex.test(emailInput.value)) {
    emailError.textContent = "Email is invalid";
  } else {
    emailError.textContent = "";
  }
}
const usernamePattern = /^[a-zA-Z0-9_-]{3,16}$/;

function validateUser() {
  if (!usernamePattern.test(userName.value)) {
    userError.textContent = "User is Invalid";
  } else {
    userError.textContent = "";
  }
}
const passwordPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,}$/

function validatePassword() {
    if (!passwordPattern.test(passWord.value)) {
      passError.textContent = "Password is Invalid";
    } else {
      passError.textContent = "";
    }
  }