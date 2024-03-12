document.addEventListener('DOMContentLoaded', function() {
    // Ottenere il riferimento al modulo di prenotazione
    var bookingForm = document.getElementById('booking-form');

    // Aggiungi un ascoltatore per l'invio del modulo
    bookingForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita l'invio del modulo predefinito

        // Ottieni i dati dal modulo di prenotazione
        var username = bookingForm.elements['username'].value;
        var password = bookingForm.elements['password'].value;
        // Altre informazioni dal modulo di prenotazione

        // Creazione dell'oggetto FormData per inviare i dati al backend
        var formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        // Aggiungi altre informazioni al formData se necessario

        // Esegui una chiamata AJAX utilizzando Fetch API
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({username, password})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Errore durante l\'accesso');
            }
            return response.json();
        })
        .then(data => {
            // Gestisci la risposta dal backend se necessario
            console.log('Risposta dal backend:', data);
            // Esempio: Mostra un messaggio di conferma dopo l'invio del modulo
            var confirmationMessage = document.createElement('div');
            confirmationMessage.className = 'confirmation-message';
            confirmationMessage.textContent = 'accesso completato per ' + username + '!';
            bookingForm.appendChild(confirmationMessage);
            // Resetta il modulo dopo l'invio
            bookingForm.reset();
        })
        .catch(error => {
            console.error('Errore:', error);
            // Gestione degli errori durante la chiamata AJAXs
            // Esempio: Mostra un messaggio di errore
            alert('Si è verificato un errore durante l\'accesso');
        });
    });
});
