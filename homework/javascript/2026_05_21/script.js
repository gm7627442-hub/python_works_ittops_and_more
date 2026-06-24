"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const TICK_PERIOD_MILLISECONDS = 500;
    const output = document.querySelector("#output");
    const buttonStart = document.querySelector("#button_start");
    const buttonPause = document.querySelector("#button_pause");
    const buttonReset = document.querySelector("#button_reset");

    let timerId = null;
    let counter = 0;
    let isPaused = false;

    function showCounter() {
        output.textContent = `${output.textContent} ${counter}`;
    }

    function tick() {
        counter++;
        showCounter();
    }

    function startTick() {
        if (timerId !== null) {
            return;
        }

        if (!isPaused) {
            counter = 0;
            output.textContent = "";
            showCounter();
        }

        isPaused = false;
        timerId = setInterval(tick, TICK_PERIOD_MILLISECONDS);
    }

    function pauseTick() {
        if (timerId === null || isPaused) {
            return;
        }

        clearInterval(timerId);
        timerId = null;
        isPaused = true;
    }

    function resetTick() {

        if (timerId !== null) {
            clearInterval(timerId);
            timerId = null;
        }
       
        counter = 0;
        
        isPaused = false;

        output.textContent = "";
        
        
    }

    buttonStart.addEventListener("click", startTick);
    buttonPause.addEventListener("click", pauseTick);
    buttonReset.addEventListener("click", resetTick);
});