function searchProjects() {
    const placeName = document.getElementById('placeInput').value;
    const searchUrl = `https://www.google.com/search?q=${placeName} real estate projects under construction`;
    window.open(searchUrl, '_blank');
}