
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