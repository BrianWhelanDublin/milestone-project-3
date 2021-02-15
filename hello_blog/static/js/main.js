// code from stack overflow to stop safari using the cache
// code from stack overflow to stop safari using the cache
window.onpageshow = function (event) {
    if (event.persisted) {
        window.location.reload();
    }
};


// code inspired by tyler potts on youtube details in readme file.
window.onload = () => {
    document.body.classList.remove("preload");
    const transitionEl = document.querySelector(".transition");
    const anchors = document.querySelectorAll("a");
    const fadeElements = document.querySelectorAll(".fade");
    setTimeout(() => {
        transitionEl.classList.remove("is-active");
    }, 500);
    setTimeout(() => {
        fadeElements.forEach((fade) => {
            fade.classList.add("is-active");
        });
    }, 500);

    anchors.forEach(anchor => {
        anchor.addEventListener("click", e => {
            e.preventDefault();
            let target = e.target.href;
            // console.log(target)
            transitionEl.classList.add("is-active");
            setTimeout(() => {
                window.location.href = target;
            }, 500);
        });
    });
};

// code from my milestone 2 project for the navigation menu.
let menu = document.querySelector(".hamburger");
let navigation = document.querySelector(".navigation");
let link = document.querySelectorAll(".navigation-item");

/* Code for screen reader on nav button */
const changeAriaSettings = () => {
    if (navigation.classList.contains("change")) {
        menu.setAttribute("aria-expanded", true);
        menu.setAttribute("aria-label", "close navigation");
    } else {
        menu.setAttribute("aria-expanded", false);
        menu.setAttribute("aria-label", "open navigation");

    }
};

menu.addEventListener("click", () => {
    navigation.classList.toggle("change");
    changeAriaSettings();
});
/* Adds an event listener to each navigation item to close the navigation menu when the link is clicked*/
link.forEach((item) => {
    item.addEventListener("click", () => {
        navigation.classList.toggle("change");
        changeAriaSettings();
    });
});

// initialize materialize functions for  select form input
M.AutoInit();

// initialize the materialize form counter using jQuery
$(document).ready(function () {
    $('textarea#bio').characterCounter();
});