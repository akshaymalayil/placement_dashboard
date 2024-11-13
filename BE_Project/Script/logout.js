document.getElementById('logoutLink').addEventListener('click', function(event) {
    event.preventDefault(); 

    sessionStorage.clear();  
    localStorage.removeItem('authToken'); 

    window.location.href = "../Login/login.html";
});
