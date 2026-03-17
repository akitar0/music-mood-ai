// ---------------------------
// 🎯 PREDICT MOOD FUNCTION
// ---------------------------
async function predictMood() {

    document.getElementById("result").innerText = "Predicting...";

    const data = {
        tempo: parseFloat(document.getElementById("tempo").value),
        danceability: parseFloat(document.getElementById("danceability").value),
        energy: parseFloat(document.getElementById("energy").value),
        key: parseFloat(document.getElementById("key").value),
        loudness: parseFloat(document.getElementById("loudness").value),
        speechiness: parseFloat(document.getElementById("speechiness").value),
        acousticness: parseFloat(document.getElementById("acousticness").value),
        instrumentalness: parseFloat(document.getElementById("instrumentalness").value),
        liveness: parseFloat(document.getElementById("liveness").value),
        valence: parseFloat(document.getElementById("valence").value)
    };

    // 🚫 prevent empty inputs
    if (Object.values(data).some(v => isNaN(v))) {
        document.getElementById("result").innerText = "Enter all values";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const result = await response.json();

        document.getElementById("result").innerText =
            `🎵 Mood: ${result.mood}`;

        document.getElementById("reason").innerText =
            `📊 Insight: ${result.reason}`;

        document.getElementById("recommendation").innerText =
            `🎧 Recommendation: ${result.recommendation}`;

        document.getElementById("playlist").innerHTML =
            result.playlist.map(song => `<li>${song}</li>`).join('');

    } catch (error) {
        document.getElementById("result").innerText = "Error predicting";
        console.error(error);
    }
}


// ---------------------------
// 📊 LOAD CLUSTER GRAPH
// ---------------------------
async function loadClusters() {
    try {
        const response = await fetch("http://127.0.0.1:5000/clusters");
        const data = await response.json();

        const points = data.map(d => ({
            x: d.energy,
            y: d.valence
        }));

        const ctx = document.getElementById('clusterChart').getContext('2d');

        // 🔥 destroy old chart (important)
        if (window.clusterChart) {
            window.clusterChart.destroy();
        }

        window.clusterChart = new Chart(ctx, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Songs',
                    data: points,
                    pointRadius: 4
                }]
            },
            options: {
                responsive: true,
                interaction: {
                    mode: 'nearest',
                    intersect: false
                },
               plugins: {
                    zoom: {
                        pan: {
                            enabled: true,
                            mode: 'xy'
                        },
                        zoom: {
                            wheel: {
                                enabled: true
                            },
                            pinch: {
                                enabled: true
                            },
                            mode: 'xy'
                        }
                    }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Energy' }
                    },
                    y: {
                        title: { display: true, text: 'Valence' }
                    }
                }
            }
        });

    } catch (error) {
        console.error("Cluster load error:", error);
    }
}


// ---------------------------
// ⚡ REAL-TIME INPUT LISTENER
// ---------------------------
document.querySelectorAll("input").forEach(input => {
    input.addEventListener("input", predictMood);
});


// ---------------------------
// 🚀 LOAD GRAPH ON PAGE LOAD
// ---------------------------
window.onload = () => {
    loadClusters();
};