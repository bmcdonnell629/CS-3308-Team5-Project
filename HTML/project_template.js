window.onload = function() {
    console.log("page is fully loaded");
    const login_button = document.querySelector("#login_button");
    login_button.addEventListener("click", login);
    const about_button = document.querySelector("#about_button");
    about_button.addEventListener("click", about);
    const home_button = document.querySelector("#home_button");
    home_button.addEventListener("click", home);
}

function login(){
    console.log("login clicked");
}

function about(){
    console.log("about clicked");
}

function home(){
    console.log("home clicked");
}