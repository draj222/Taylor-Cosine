document.getElementById('cosine-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const angleType = document.getElementById('angle_type').value;
    const angleInput = document.getElementById('angle_input').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `angle_type=${angleType}&angle_input=${encodeURIComponent(angleInput)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').textContent = `Error: ${data.error}`;
        } else {
            document.getElementById('result').textContent = `Result: ${data.result}`;
        }
    })
    .catch(error => {
        document.getElementById('result').textContent = `Error: ${error}`;
    });
});
