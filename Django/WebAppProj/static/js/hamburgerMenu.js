// behaviour of the collapsable menu
// which shows only when screen is to small for whole navigation bar

function hamburgerFunction(){
    const menu = document.getElementById("menu-list");

    // its activate when you click on the menu button
    // menu hiddes when it was displayed
    // and shows when it was not
    
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}
