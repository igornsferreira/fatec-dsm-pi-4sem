document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('button[data-bs-toggle="modal"]');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const quadraId = this.getAttribute('data-quadra-id');
            const nomeQuadra = this.getAttribute('data-nome-quadra');
            document.getElementById('quadraId').value = quadraId;
            setLocal(nomeQuadra);
        });
    });

    const form = document.getElementById('agendamentoForm');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            alert('Agendamento confirmado!');

            const modalElement = document.getElementById('agendamentoModal');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            if (modalInstance) {
                modalInstance.hide();
            }
        });
    }
});

function setLocal(nomeQuadra) {
    const localField = document.getElementById('local');
    if (localField) {
        localField.value = nomeQuadra;
    }
}
