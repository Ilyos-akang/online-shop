// Navbar shadow on scroll
window.addEventListener("scroll", () => {
    const nav = document.querySelector("nav");
    if(window.scrollY > 20){
        nav.style.boxShadow = "0 2px 15px rgba(0,0,0,0.15)";
    } else {
        nav.style.boxShadow = "none";
    }
});

// Contact form submit
function sendForm(){
    alert("Xabaringiz yuborildi! Tez orada siz bilan bog‘lanamiz.");
}
