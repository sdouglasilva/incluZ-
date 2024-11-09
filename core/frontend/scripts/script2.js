const apiUrl = 'http://localhost:8000';  // Altere conforme o seu backend

// Função para carregar usuários
const loadUsers = async () => {
    const response = await fetch(`${apiUrl}/users/`);
    const users = await response.json();
    
    const usersList = document.getElementById('users');
    usersList.innerHTML = '';
    
    users.forEach(user => {
        const userItem = document.createElement('li');
        userItem.textContent = `${user.first_name} ${user.last_name} - ${user.date_of_birth}`;
        userItem.onclick = () => showUserDetails(user.id);
        usersList.appendChild(userItem);
    });
};

// Função para mostrar detalhes de um usuário
const showUserDetails = async (userId) => {
    const response = await fetch(`${apiUrl}/users/${userId}/`);
    const user = await response.json();

    document.getElementById('user-id').value = user.id;
    document.getElementById('update-first-name').value = user.first_name;
    document.getElementById('update-last-name').value = user.last_name;
    document.getElementById('update-date-of-birth').value = user.date_of_birth;
};

// Função para criar um novo usuário
const createUser = async (e) => {
    e.preventDefault();

    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const dateOfBirth = document.getElementById('date-of-birth').value;

    const response = await fetch(`${apiUrl}/users/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            date_of_birth: dateOfBirth,
        }),
    });

    if (response.ok) {
        alert('Usuário criado com sucesso!');
        loadUsers();
    }
};

// Função para atualizar um usuário
const updateUser = async (e) => {
    e.preventDefault();

    const userId = document.getElementById('user-id').value;
    const firstName = document.getElementById('update-first-name').value;
    const lastName = document.getElementById('update-last-name').value;
    const dateOfBirth = document.getElementById('update-date-of-birth').value;

    const response = await fetch(`${apiUrl}/users/${userId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            date_of_birth: dateOfBirth,
        }),
    });

    if (response.ok) {
        alert('Usuário atualizado com sucesso!');
        loadUsers();
    }
};

// Adicionando eventos aos formulários
document.getElementById('create-user-form').addEventListener('submit', createUser);
document.getElementById('update-user-form').addEventListener('submit', updateUser);

// Carregar usuários ao iniciar
loadUsers();