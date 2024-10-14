// Captura o clique no botão "Reservar" para abrir o modal
 Modaldocument.querySelectorAll('.btn').forEach(button => {
   button.addEventListener('click', function() {
       const reservaModal = new bootstrap.Modal(document.getElementById('reservaModal'));
        reservaModal.show();
    });
});


