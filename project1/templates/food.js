function calculateTotal() {
  let totalPrice = 0;

  // Calculate main course total
  totalPrice +=
    document.getElementById("chicken-thali-quantity").value *
    250 +
    document.getElementById("mutton-thali-quantity").value *
    350 +
    document.getElementById("panner-makhanwala-quantity").value *
    250 +
    document.getElementById("chicken-malvani-quantity").value *
    280 +
    document.getElementById("mutton-malvani-quantity").value *
    400 +
    document.getElementById("palak-paneer-quantity").value *
    300 +
    document.getElementById("shole-puri-quantity").value *
    250 +
    document.getElementById("veg-kolhapuri-quantity").value *
    350 +
    document.getElementById("mutton-biryani-quantity").value *
    450;

  // Calculate desserts total
  totalPrice +=
    document.getElementById("gulab-jamun-quantity").value * 50 +
    document.getElementById("gajar-ka-halwa-quantity").value * 80 +
    document.getElementById("sandesh-quantity").value * 150 +
    document.getElementById("modak-quantity").value * 50 +
    document.getElementById("aam-shrikhand-quantity").value * 80 +
    document.getElementById("payasam-quantity").value * 180 +
    document.getElementById("thandai-mousse-quantity").value * 300 +
    document.getElementById("carrot-pudding-quantity").value * 250 +
    document.getElementById("basundi-quantity").value * 300;

  // Update total price
  document.getElementById("total-price").textContent = totalPrice;
}
