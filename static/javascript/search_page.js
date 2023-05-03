window.onload = function() {
    const login_button = document.querySelector("#login_button");
    login_button.addEventListener("click", login);
    const about_button = document.querySelector("#about_button");
    about_button.addEventListener("click", about);
    const home_button = document.querySelector("#home_button");
    home_button.addEventListener("click", home);
    const advanced_button = document.querySelector("#advanced_button");
    advanced_button.addEventListener("click", advanced);
    const search_button = document.querySelector("#search_button");
    search_button.addEventListener("click", search);
    const home_button = document.querySelector("#score_button");
    score_button.addEventListener("click", score);
}

window.addEventListener("keypress", function(event) {    
    if (event.key == "Enter") {
        return search();
    }
})

function login() {
    location.href="https://scrabble-for-the-rabble.onrender.com/login";
}

function about() {
    location.href="https://scrabble-for-the-rabble.onrender.com/about";
}

function home() {
    location.href="https://scrabble-for-the-rabble.onrender.com/";
}

function score() {
    location.href="https://scrabble-for-the-rabble.onrender.com/user_score";
}

function advanced() {
    const filters = document.getElementById("advanced_filters");
    if (filters.style.maxHeight) {
        filters.style.maxHeight = null;
        this.style.color = "var(--cyan_after_dark)";
        this.textContent = "ADVANCED SEARCH +"
    } else {
        filters.style.maxHeight = filters.scrollHeight + "px";
        this.style.color = "var(--spinach)";
        this.textContent = "ADVANCED SEARCH -"
    }
}

function search() {
    const search_word = document.getElementById("search_bar").value.toUpperCase();
    const allow_anagrams = document.querySelector(".checkbox").checked;
    const min_letters = document.getElementById("min_letters").value;
    const max_letters = document.getElementById("max_letters").value;
    const starts_with = document.getElementById("start_box").value.toUpperCase();
    const ends_with = document.getElementById("end_box").value.toUpperCase();
    const contains = document.getElementById("contain_box").value.toUpperCase();
    const fixed_letters = document.getElementById("fixed_box").value.toUpperCase();
    
    location.href = "https://scrabble-for-the-rabble.onrender.com/search_results?search_word="+search_word+
        "&allow_anagrams="+allow_anagrams+
        "&min_letters="+min_letters+
        "&max_letters="+max_letters+
        "&starts_with="+starts_with+
        "&ends_with="+ends_with+
        "&contains="+contains+
        "&fixed_letters="+fixed_letters;
}
