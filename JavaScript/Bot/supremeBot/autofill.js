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
