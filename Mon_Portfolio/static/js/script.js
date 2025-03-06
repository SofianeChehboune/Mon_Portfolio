document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    themeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
        
        // Si le mode sombre est activé, changer la couleur du texte de plusieurs éléments en blanc
        if (document.body.classList.contains("dark-mode")) {
            document.querySelectorAll("p, h1, h2, h3, a, li, span, div").forEach(el => {
                el.style.color = "white";
            });
        } else {
            // Sinon, réinitialiser la couleur du texte (pour revenir aux styles par défaut définis dans le CSS)
            document.querySelectorAll("p, h1, h2, h3, a, li, span, div").forEach(el => {
                el.style.color = "";
            });
        }
    });
});
