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
const csrftoken = getCookie('csrftoken');

// Remove item and reload on click
$(".remove-item").click(function(event){
    let itemId = $(this).attr('id').split('remove_')[1];
    let subscriptionType= $(this).data('subscription_type');
    let url = "/bag/remove/" + itemId + '/';
    let data = {
        "csrfmiddlewaretoken": csrftoken,
        "subscriptionType": subscriptionType
    }

    $.post(url, data).done(function() { location.reload(); });
});