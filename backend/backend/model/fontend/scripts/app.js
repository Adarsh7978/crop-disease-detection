async function predict() {
    const file = document.getElementById("upload").files[0];
    let formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        body: formData,
    });

    const data = await res.json();
    document.getElementById("result").innerText = "Prediction: " + data.prediction;
}

