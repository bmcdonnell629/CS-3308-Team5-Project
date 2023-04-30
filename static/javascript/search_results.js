window.onload = function() {
    const login_button = document.querySelector("#login_button");
    login_button.addEventListener("click", login);
    const about_button = document.querySelector("#about_button");
    about_button.addEventListener("click", about);
    const home_button = document.querySelector("#home_button");
    home_button.addEventListener("click", home);
    
    get_results();
}

function login() {
    location.href="https://scrabble-for-the-rabble.onrender.com/login";
}

function about() {
    location.href="https://scrabble-for-the-rabble.onrender.com/about";
}

function home() {
    location.href="https://scrabble-for-the-rabble.onrender.com/";
}

function get_results() {
    const results_url = window.location.search;
    const search_parameters = new URLSearchParams(results_url);
    const search_word = search_parameters.get("search_word");
    const input_word = document.getElementById("input_word");
    input_word.textContent = search_word;
}
