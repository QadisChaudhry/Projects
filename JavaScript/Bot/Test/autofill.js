let url = window.location.href;
// let re = new RegExp("https:(\/\/)www.supremenewyork.com(\/)shop($|\/$|\/.{25}([a-zA-Z]|[\d]))");
let contact_page = new RegExp("(_ga=)");
let shipping_page = new RegExp("(\bstep=shipping_method\b)$");
let payment_page = new RegExp("(\bpayment_method\b)");

profile = {
  "name": "John Smith",
  "email": "Smith@gmail.com",
  "phone": "123-123-1234",
  "address": "1234 aeuo St",
  "zip": "11222",
  "card": "4111 1111 1111 1111",
  "month": "03",
  "year": "2024",
  "cvv": "211"
};

function contact_kith() {
    document.getElementById("checkout_email").value = profile["email"];
    
    let first_name = profile.name.split(" ")[0];
    let last_name = profile.name.split(" ")[1]
    
    document.getElementById("checkout_shipping_address_first_name").value = first_name;
    document.getElementById("checkout_shipping_address_last_name").value = last_name;
    document.getElementById("checkout_shipping_address_address1").value = profile["address"];
    document.getElementById("checkout_shipping_address_city").value = "Brooklyn";
    document.getElementById("checkout_shipping_address_province").value = "NY";
    document.getElementById("checkout_shipping_address_zip").value = profile["zip"];
    document.getElementById("checkout_shipping_address_phone").value = profile["phone"];
    document.getElementById("continue_button").click()
};

function shipping_kith() {
    document.getElementById("continue_button").click()
};

function payment_kith() {
    document.getElementById("number").value = profile["card"];
    document.getElementById("name").value = profile["name"];
    document.getElementById("expiry").value = profile["month"] + profile["year"];
    document.getElementById("verification_value").value = profile["cvv"];
};

function autofill_supreme() {
    document.getElementById("order_billing_name").value = profile["name"];
    document.getElementById("order_email").value = profile["email"];
    document.getElementById("order_tel").value = profile["phone"];
    document.getElementById("bo").value = profile["address"];
    document.getElementById("order_billing_city").value = "Brooklyn";
    document.getElementById("order_billing_state").value = "NY";
    document.getElementById("order_billing_zip").value = profile["zip"];
    document.getElementById("rnsnckrn").value = profile["card"];
    document.getElementById("credit_card_month").value = profile["month"];
    document.getElementById("credit_card_year").value = profile["year"];
    document.getElementById("orcer").value = profile["cvv"];
    document.getElementsByClassName("iCheck-helper")[1].click();
    // document.getElementsByName("commit")[0].click();
};

if (url == "https://www.supremenewyork.com/checkout") {
    autofill_supreme();
};

if (contact_page.test(url)) {
    contact_kith();
};

if (shipping_page.test(url)) {
    shipping_kith();
};

if (payment_page.test(url)) {
    payment_kith();
};
