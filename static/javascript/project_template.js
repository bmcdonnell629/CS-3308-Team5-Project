window.onload = function() {
    const login_button = document.querySelector("#login_button");               // Login/About/Home buttons in header
    login_button.addEventListener("click", login);
    const about_button = document.querySelector("#about_button");
    about_button.addEventListener("click", about);
    const home_button = document.querySelector("#home_button");
    home_button.addEventListener("click", home);
    
}

function login(){
    location.href="https://scrabble-for-the-rabble.onrender.com/login";
}

function about(){
    location.href="https://scrabble-for-the-rabble.onrender.com/about";
}

function home(){
    location.href="https://scrabble-for-the-rabble.onrender.com/";
}
