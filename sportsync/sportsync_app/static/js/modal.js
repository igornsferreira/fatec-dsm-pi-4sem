document.addEventListener('DOMContentLoaded', function () {
    // Adiciona o evento de clique para o modal quando um botão é pressionado
    const buttons = document.querySelectorAll('button[data-bs-toggle="modal"]');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            // Agora `this` deve referir-se ao botão clicado
            const nomeQuadra = this.getAttribute('data-nome-quadra');
            console.log(nomeQuadra); // Verifica se está capturando o nome corretamente
            setLocal(nomeQuadra);
        });
    });
});

function setLocal(nomeQuadra) {
    document.getElementById('local').value = nomeQuadra;
}

document.getElementById('agendamentoForm').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Agendamento confirmado!');
    // Fechar o modal
    var modal = bootstrap.Modal.getInstance(document.getElementById('agendamentoModal'));
    if (modal) {
        modal.hide();
    }
});
