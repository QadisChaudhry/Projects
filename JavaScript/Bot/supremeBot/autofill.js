profile = {
  "name": "Bryan Saldana",
  "email": "Habsaldana833@gmail.com",
  "phone": "347-666-7919",
  "address": "AB986 7807 20th Avenue",
  "zip": "11214",
  "card": "6011 0012 3854 7618",
  "month": "11",
  "year": "2025",
  "cvv": "375"
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
