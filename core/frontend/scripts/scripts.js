document.getElementById('student-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Cria um objeto com os dados do formulário
    const data = {
        first_name: document.getElementById('first-name').value,
        last_name: document.getElementById('last-name').value,
        date_of_birth: document.getElementById('birth-date').value,
        email: document.getElementById('email').value
    };
    
    // Envia os dados usando o fetch para o servidor local
    fetch('http://127.0.0.1:8000/students/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    console.log(data)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('message').textContent = `Error: ${data.error}`;
            document.getElementById('message').style.color = 'red';
        } else {
            document.getElementById('message').textContent = 'Student registered successfully!';
            document.getElementById('message').style.color = 'green';
            document.getElementById('student-form').reset(); // Limpa o formulário após o sucesso
        }
    })
    .catch(error => {
        document.getElementById('message').textContent = `Error: ${error}`;
        document.getElementById('message').style.color = 'red';
    });
});