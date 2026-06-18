const featuresMap = {
   heart: [
    "Age",
    "Gender (0=Female, 1=Male)",
    "Chest Pain Type (0=ATA, 1=NAP, 2=ASY, 3=TA)",
    "Resting Blood Pressure",
    "Cholesterol",
    "Maximum Heart Rate"
],
   diabetes: [
    "Age",
    "BMI",
    "Blood Pressure",
    "Cholesterol",
    "Glucose",
    "Insulin",
    "Weight",
    "Height",
    "Physical Activity",
    "Family History Score"
],
   cancer: [
    "Tumor Size",
    "Cell Texture",
    "Tumor Perimeter",
    "Tumor Area",
    "Cell Smoothness",
    "Tumor Density",
    "Cell Concavity",
    "Concave Points",
    "Cell Symmetry",
    "Fractal Dimension"
]
};

function updateInputs() {
    let disease = document.getElementById("disease").value;
    let box = document.getElementById("inputsBox");

    box.innerHTML = "";

    featuresMap[disease].forEach(f => {
        let div = document.createElement("div");
        div.className = "input-group";

        div.innerHTML = `
            <label>${f}</label>
            <input type="number" class="featureInput" placeholder="Enter ${f}">
        `;

        box.appendChild(div);
    });

    document.getElementById("result").innerText = "";
}

function predict() {
    let inputs = document.querySelectorAll(".featureInput");
    let values = [];

    inputs.forEach(i => values.push(Number(i.value || 0)));

    let disease = document.getElementById("disease").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            disease: disease,
            features: values
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    });
}

window.onload = updateInputs;