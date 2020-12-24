let checkbox = document.querySelector('input[type="checkbox"]');
let monthly = $("#checkbox-label1");
let yearly = $("#checkbox-label2");
let monthlyPrices = ['$20/mo', '$30/mo', '$18/mo'];
let yearlyPrices = ['$192/mo', '$288/mo', '$172/mo'];

checkbox.addEventListener('change', function () {
    if (checkbox.checked) {
        //Yearly
        monthly.removeClass("font-weight-bold");
        monthly.addClass("text-gray");
        yearly.removeClass("text-gray");
        yearly.addClass("font-weight-bold");

        $("#gym-price").html(yearlyPrices[0]);
        $("#swimming-price").html(yearlyPrices[1]);
        $("#pool-price").html(yearlyPrices[2]);
    } else {
        // Monthly
        yearly.removeClass("font-weight-bold");
        yearly.addClass("text-gray");
        monthly.removeClass("text-gray");
        monthly.addClass("font-weight-bold");


        $("#gym-price").html(monthlyPrices[0]);
        $("#swimming-price").html(monthlyPrices[1]);
        $("#pool-price").html(monthlyPrices[2]);
    }
});