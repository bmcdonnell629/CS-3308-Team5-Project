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
    
    var result_html = "";
    const result_list = {{ result_list|tojson }};
    let i = 0;

    while (i < result_list.length) {
        result_html = result_html + "<p class='result'>" + result_list[i][0] + "</p>";
        result_html = result_html + "<p class='score'>" + result_list[i][1] + "</p>";
        i++;
    }

    document.getElementById("results").innerHTML += result_html;
}
