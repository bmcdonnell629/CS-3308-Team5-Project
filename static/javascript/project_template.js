window.onload = function() {
    const login_button = document.querySelector("#login_button");               // Login/About/Home buttons in header
    login_button.addEventListener("click", login);
    const about_button = document.querySelector("#about_button");
    about_button.addEventListener("click", about);
    const home_button = document.querySelector("#home_button");
    home_button.addEventListener("click", home);
    const score_button = document.querySelector("#score_button");
    score_button.addEventListener("click", score);
    const logout_button = document.querySelector("#logout_button");
    logout_button.addEventListener("click", logout);
    
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

function score(){
    location.href="https://scrabble-for-the-rabble.onrender.com/user_score";
}

function logout(){
    location.href="https://scrabble-for-the-rabble.onrender.com/logout";
}
