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
    
    const filters_used = document.getElementById("filters_used");
    
    const allow_anagrams = search_parameters.get("allow_anagrams");
    if (allow_anagrams == "true") {
        filters_used.innerHTML += "Anagrams allowed: <span>YES</span><br>";
    } else {
        filters_used.innerHTML += "Anagrams allowed: <span>NO</span><br>";
    }
    
    const min_letters = search_parameters.get("min_letters");
    const max_letters = search_parameters.get("max_letters");
    if (min_letters == max_letters) {
        filters_used.innerHTML += "<span>" + min_letters + "</span> letter words<br>";
    } else {
        filters_used.innerHTML += "<span>" + Math.min(parseInt(min_letters), parseInt(max_letters)) + "</span> to <span>" + Math.max(parseInt(min_letters), parseInt(max_letters)) + "</span> letter words<br>";
    }
    
    const starts_with = search_parameters.get("starts_with");
    const ends_with = search_parameters.get("ends_with");
    if (starts_with != "" || ends_with != "") {
        filters_used.innerHTML += "<span>" + starts_with + "</span>______<span>" + ends_with + "</span><br>";
    }
    
    const contains = search_parameters.get("contains");
    if (contains != "") {
        filters_used.innerHTML += "Contains: <span>" + contains + "</span><br>";
    }
    
    const fixed_letters = search_parameters.get("fixed_letters");
    if (fixed_letters != "") {
        filters_used.innerHTML += "Letters with fixed positions: ";
        for (const letter of fixed_letters) {
            if (letter == "*") {
                filters_used.innerHTML += "_ ";
            } else {
                filters_used.innerHTML += "<span>" + letter + "</span> ";
            }
        }
        filters_used.innerHTML += "</span><br>";
    }
}
