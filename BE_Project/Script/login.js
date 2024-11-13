
// Toggle Password Visibility
function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const toggleBtn = passwordField.nextElementSibling;
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleBtn.textContent = 'Hide';
    } else {
        passwordField.type = 'password';
        toggleBtn.textContent = 'Show';
    }
}

// Basic Form Validation
document.getElementById('studentLoginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validateLogin('studentUsername', 'studentPassword', 'student');
});

document.getElementById('facultyLoginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validateLogin('facultyUsername', 'facultyPassword', 'faculty');
});

document.getElementById('industryLoginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validateLogin('industryUsername', 'industryPassword', 'industry');
});

function validateLogin(usernameId, passwordId, userType) {
    const username = document.getElementById(usernameId).value;
    const password = document.getElementById(passwordId).value;

    if (username === '' || password === '') {
        alert('Please fill out both fields.');
    } else {
        // Simulate login success
        alert(`Welcome, ${username}! Redirecting to your dashboard...`);

        // Redirect to the dashboard page upon successful login
        window.location.href = '../Dashboard/dashboard.html';

    }
}
