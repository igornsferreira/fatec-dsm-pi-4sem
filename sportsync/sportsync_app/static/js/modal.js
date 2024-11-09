document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('button[data-bs-toggle="modal"]');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            // Pega o id e o nome da quadra do botão
            const quadraId = this.getAttribute('data-quadra-id');
            const nomeQuadra = this.getAttribute('data-nome-quadra');
            
            // Atribui os valores ao modal
            document.getElementById('quadraId').value = quadraId;
            document.getElementById('local').value = nomeQuadra;
        });
    });
});
