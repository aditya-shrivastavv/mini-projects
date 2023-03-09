const hamburgerIcon = document.querySelector(".hamburger");
const mobileMenu = document.querySelector("#menu");

hamburgerIcon.addEventListener('click' ,function toggleClasses() {
  hamburgerIcon.classList.toggle('open');
  mobileMenu.classList.toggle('hidden');
})