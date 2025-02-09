function setupNavbar() {
  const navbarLinks = document.querySelectorAll('.navbar a');

  navbarLinks.forEach(link => {
    link.addEventListener('click', function() {
      navbarLinks.forEach(link => {
        link.classList.remove('active');
      });
      this.classList.add('active');
    });
  });
}

// Call the setupNavbar function when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
  setupNavbar();
});
