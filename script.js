(function() {
  // Fill "Nom"
  const lastname = document.querySelector('#formly_5_input_lastname_0');
  if (lastname) {
    lastname.value = "Rakoto";
    lastname.dispatchEvent(new Event('input', { bubbles: true }));
    lastname.dispatchEvent(new Event('blur'));
  }

  // Fill "Prénom"
  const firstname = document.querySelector('#formly_5_input_firstname_1');
  if (firstname) {
    firstname.value = "Jean";
    firstname.dispatchEvent(new Event('input', { bubbles: true }));
    firstname.dispatchEvent(new Event('blur'));
  }

  // Fill "Téléphone"
  const phone = document.querySelector('#formly_7_input_telnumber_1');
  if (phone) {
    phone.value = "0321234567";
    phone.dispatchEvent(new Event('input', { bubbles: true }));
    phone.dispatchEvent(new Event('blur'));
  }

  // Fill "Email"
  const email = document.querySelector('#formly_9_input_email_0');
  if (email) {
    email.value = "jean.rakoto@example.com";
    email.dispatchEvent(new Event('input', { bubbles: true }));
    email.dispatchEvent(new Event('blur'));
  }

  // Fill "Ville"
  const town = document.querySelector('#formly_9_input_town_1');
  if (town) {
    town.value = "Antananarivo";
    town.dispatchEvent(new Event('input', { bubbles: true }));
    town.dispatchEvent(new Event('blur'));
  }

  // Optionally click "Continuer"
  const button = document.querySelector('button[form="dynamic-form"]');
  if (button) button.click();
})();
