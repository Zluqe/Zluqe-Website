const isScrolling = () => {
    const headerEl = document.querySelector('.primary-header')
    const navItems = document.querySelector('.nitem')
    let windowPosition = window.scrollY > 780
    headerEl.classList.toggle('active', windowPosition)
    navItems.classList.toggle('active', windowPosition)
    
}
window.addEventListener('scroll', isScrolling)

// Agentseed's theme changer
const root = document.documentElement
var theme = localStorage.getItem("theme");
if(theme == 'dark') {
    setThemeDark();
} else if (theme == 'light'){
    setThemeLight();
}
function changeTheme() {
    if (theme == 'dark') {
        setThemeLight();
    } else if (theme == 'light') {
        setThemeDark();
    }
}
function setThemeDark() {
    root.style.setProperty('--background', 'url(dark.png)');
    localStorage.setItem("theme", "dark");
    theme = 'dark';
}
function setThemeLight() {
    root.style.setProperty('--background', 'url(light.png)');
    localStorage.setItem("theme", "light")
    theme = 'light';
}