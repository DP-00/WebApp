function hamburgerFunction(){
    const menu = document.getElementById("menu-list");
    const logo = document.getElementById("logo");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}