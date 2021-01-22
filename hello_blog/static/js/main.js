
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