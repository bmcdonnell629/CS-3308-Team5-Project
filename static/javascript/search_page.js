window.onload = function() {
    const login_button = document.querySelector("#login_button");
    login_button.addEventListener("click", login);
    const about_button = document.querySelector("#about_button");
    about_button.addEventListener("click", about);
    const home_button = document.querySelector("#home_button");
    home_button.addEventListener("click", home);
    const search_button = document.querySelector("#search_button");
    search_button.addEventListener("click", search);
}

function login(){
    location.href="https://scrabble-for-the-rabble.onrender.com/";
}

function about(){
    location.href="https://scrabble-for-the-rabble.onrender.com/about";
}

function home(){
    location.href="https://scrabble-for-the-rabble.onrender.com/search";
}

function search(){
    location.href="https://scrabble-for-the-rabble.onrender.com/search_results";
}