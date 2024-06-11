document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    const data = {
        username: formData.get('username'),
        password: formData.get('password')
    };

    fetch('/myapp/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
      .then(data => {
          if (data.success) {
              window.location.href = '/';
          } else {
              // Handle error
              console.error(data.errors);
          }
      });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
