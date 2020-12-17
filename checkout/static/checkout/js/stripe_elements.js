
/* Setting up Stripe logic for checkout app */


// Get relevant keys from template
let stripePublicKey = $("#id_stripe_public_key").text().slice(1,-1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);

// Set up Stripe using public_key
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();


// Set custom style
let style = {
    base: {
        color: "#000000",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "25px",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        color: "#dc3545",
        iconColor: "#dc3545"
    }
};

// Create card with custom style
let card = elements.create("card", {style: style});

// Mount stirpe card to div element
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener('change', function(event){
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert"> 
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;

        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

let form = document.getElementById('payment-form');

// Handle submit event of Stripe/Order Form 
form.addEventListener('submit', function(event) {
    // Prevent default action
    event.preventDefault();
    card.update({"disabled": true});

    $("#submit-button").attr('disabled', true);

    // Confirm card payment
    // Includes intent information fields 
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(response) {
        // Note: In future git version try to re-factor the code logic such that you 
        // use this statement:
        // if (response.paymentIntent && response.paymentIntent.status === 'succeeded')

        if (response.error) {
            // Handle unsuccessful, processing, or canceled payments and API errors here
            let errorDiv = document.getElementById('card-errors'); 
            let html = `
                <span class="icon" role="alert"> 
                    <i class="fas fa-times"></i>
                </span>
                <span>${response.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // Handle successful payment here
            form.submit();
        }
    });
})