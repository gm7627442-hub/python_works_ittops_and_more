"use strict";



document.addEventListener("DOMContentLoaded", () => {

    const btnCreate= document.querySelector("#create")

    function progresBar() {
        let tcik = 0 
        
        const container = document.createElement("div");
       
        container.style.width = "200px";
        container.style.height = "20px";
        container.style.backgroundColor = "#f0f0f0";
        container.style.borderRadius = "10px";
        container.style.overflow = "hidden";
        container.style.margin = "5px 0";

        const fill = document.createElement("div");
        fill.style.width = "100%";
        fill.style.height = "100%";
        fill.style.backgroundColor = "#4CAF50";
        fill.style.transition = "width 0.1s";

        container.appendChild(fill);
        document.body.appendChild(container);
        
        let progress = 100;
        
        const interval = setInterval(() => {
           
        if (progress <= 0) {
                clearInterval(interval);
                container.remove()
                return;
            }
            progress--;
            fill.style.width = progress + "%";
        }, 30);
    }


 btnCreate.addEventListener("click", progresBar)
})