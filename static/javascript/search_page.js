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
    location.href="https://scrabble-for-the-rabble.onrender.com/login";
}

function about(){
    location.href="https://scrabble-for-the-rabble.onrender.com/about";
}

function home(){
    location.href="https://scrabble-for-the-rabble.onrender.com/";
}

function search(){
    const search_word = document.getElementById("search_bar").value;
    location.href = "https://scrabble-for-the-rabble.onrender.com/search_results?search_word=" + search_word;
}
