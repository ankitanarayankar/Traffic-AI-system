let countdownTimer;

function startCountdown(seconds) {
    clearInterval(countdownTimer);
    let t = seconds;
    document.getElementById("countdown").innerText = t;

    countdownTimer = setInterval(() => {
        t--;
        document.getElementById("countdown").innerText = t;
        if (t <= 0) clearInterval(countdownTimer);
    }, 1000);
}

function updateSignal(density) {
    document.querySelectorAll(".light")
        .forEach(l => l.classList.remove("active"));

    if (density === "High")
        document.querySelector(".green").classList.add("active");
    else if (density === "Medium")
        document.querySelector(".yellow").classList.add("active");
    else
        document.querySelector(".red").classList.add("active");
}

function loadTraffic() {
    fetch("http://127.0.0.1:5000/traffic")
        .then(r => r.json())
        .then(d => {
            document.getElementById("vehicles").innerText = d.vehicle_count;
            document.getElementById("density").innerText = d.traffic_density;
            document.getElementById("time").innerText = d.signal_time;

            const densityEl = document.getElementById("density");
            densityEl.className = d.traffic_density.toLowerCase();

            updateSignal(d.traffic_density);
            startCountdown(d.signal_time);
        })
        .catch(err => console.error("FETCH ERROR", err));
}

loadTraffic();
setInterval(loadTraffic, 10000);
