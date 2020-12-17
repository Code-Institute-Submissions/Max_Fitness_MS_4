
/* Setting up Stripe logic for checkout app */


// Get relevant keys from template
let stripePublicKey = $("#id_stripe_public_key").text().slice(1,-1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);

// Set up Stripe using public_key
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

// Get Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrfToken = getCookie('csrftoken');


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
    let errorDiv = document.getElementById("card-errors");
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

let form = document.getElementById("payment-form");

// Handle submit event of Stripe/Order Form 
form.addEventListener("submit", function(event) {
    // Prevent default action
    event.preventDefault();
    card.update({"disabled": true});
    $("#loading-overlay").fadeToggle(100);
    $("#submit-button").attr("disabled", true);
    
    // Get data and send it to view to get stored
    // as metadata under current Intent id
    let saveInfo = Boolean($("#id-save-info").attr("checked"));
    let postData = {
        "csrfmiddlewaretoken": csrfToken,
        "client_secret": clientSecret,
        "save_info": saveInfo,
    }

    let url = '/checkout/cache_checkout_data/'

    $.post(url, postData).done(function(){
        // Confirm card payment
        // Includes intent information fields 
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
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
                console.log(response.error);
                $(errorDiv).html(html);
                $('#loading-overlay').fadeToggle(100);
                card.update({'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (response.paymentIntent.status === "succeeded"){
                    // Handle successful payment here
                    form.submit();
               } 
            }
        });
    }).fail(function(){
        //Reloads the page to show the user error message 
        location.reload();
    })
});