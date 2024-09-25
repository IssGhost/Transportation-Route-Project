document.getElementById('edgeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const from = document.getElementById('from').value;
    const to = document.getElementById('to').value;
    const cost = document.getElementById('cost').value;

    fetch('http://127.0.0.1:5000/add_edge', {  // Updated URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ from, to, cost })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('edgeForm').reset();
    })
    .catch(error => console.error('Error:', error));  // Added error handling
});

document.getElementById('getMST').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/mst')  // Updated URL
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));  // Added error handling
});
