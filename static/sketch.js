let plantHeight = 100; // Initial height of the plant
let mood = "neutral"; // Default mood
let growthRate = 0; // Growth rate based on mood

function setup() {
    createCanvas(400, 400);
    background(220);
    updatePlant();
}

function draw() {
    background(220);
    drawPlant();
    displayStatus();
}

function drawPlant() {
    stroke(0);
    fill(34, 139, 34); // Green color for the plant
    rect(200, 400 - plantHeight, 20, plantHeight); // Draw the plant trunk

    // Draw leaves based on plant height
    fill(0, 255, 0);
    ellipse(200, 400 - plantHeight, 50, 50); // Top leaf
}

function displayStatus() {
    const statusDiv = document.getElementById("plantStatus");
    statusDiv.innerHTML = `Plant Height: ${plantHeight}px`;
}

function updatePlant() {
    fetch('/get_mood_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ mood: mood })
    })
    .then(response => response.json())
    .then(data => {
        growthRate = data.growth;
        plantHeight += growthRate; // Update plant height
        plantHeight = constrain(plantHeight, 10, 400); // Constrain height
        displayStatus();
    });
}

function waterPlant() {
    mood = "happy"; // Assume watering the plant makes the user happy
    updatePlant();
}
