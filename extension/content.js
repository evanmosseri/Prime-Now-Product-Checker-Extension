var zip = "11234";
var t = new Date().getTime();

function checkAvailability(productID) {
    var baseURL = "https://primenow.amazon.com/gp/product/";
    $.ajax({
        url: baseURL + productID,
        cache: false,
        success: function (response) {
            var parsed = $($.parseHTML(response));
            var price = parsed.find("#priceblock_ourprice").text();
            var unavailable = parsed.find(".a-box-inner span:contains('Currently Unavailable')").length;
            console.log(baseURL + productID)

        },
        error: function (err) {
            console.log(err);
        }
    })
}

function checkPrime(zip, productID) {
    var match;
    $.ajax({
        url: "https://primenow.amazon.com/",
        cache: false,qu
        success: function (response) {
            match = response.match(/"offerSwappingToken":".*?"/);
            if (match.length) {
                offerToken = match[0].substring("offerSwappingToken: \"".length + 1, match[0].length - 1);
                var change_zip_url = "https://primenow.amazon.com/cart/initiatePostalCodeUpdate?" +
                    "newPostalCode=" + zip +
                    "&offer-swapping-token=" + offerToken +
                    "&noCartUpdateRequiredUrl=%2Fhome&" +
                    "allCartItemsSwappableUrl=%2Fhome&" +
                    "someCartItemsUnswappableUrl=%2Fhome";
                $.ajax({
                    url: change_zip_url,
                    cache: false,
                    success: function () {
                        checkAvailability(productID);
                    },
                })
            }
        }
    });
}

if (window.location.href.indexOf("primenow") == -1) {
    if (window.location.href.indexOf("/dp/") != -1 || window.location.href.indexOf("/gp/")) {
        window.addEventListener("load", function () {
            var product_id = window.location.href.split("/")[5];
            checkAvailability(product_id);
            // console.log(chrome.extension.getURL("jquery-3.2.1.min.js"))
            // checkPrime(zip, product_id)
        });
    }
}



