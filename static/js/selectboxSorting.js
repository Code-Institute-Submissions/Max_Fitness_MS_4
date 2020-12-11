// Select Box Sorting Logic
$("#sort-selector").change(function (){
    let selector = $(this);
    let currentUrl = new URL(window.location);

    let selectorVal = selector.val();
    if (selectorVal != "reset"){
        let sort = selectorVal.split("_")[0];
        let direction = selectorVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
    }
});