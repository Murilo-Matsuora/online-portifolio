window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

document.getElementById('copyEmail').addEventListener('click', function() {
    const email = this.getAttribute('data-email');
    const icon = document.getElementById('emailIcon');

    navigator.clipboard.writeText(email).then(() => {
        
        icon.classList.replace('bi-envelope-at', 'bi-check-lg');
        icon.style.color = '#28a745';

        setTimeout(() => {
            icon.classList.replace('bi-check-lg', 'bi-envelope-at');
            icon.style.color = '';
        }, 2000);

    }).catch(err => {
        console.error('Erro ao copiar: ', err);
    });
});