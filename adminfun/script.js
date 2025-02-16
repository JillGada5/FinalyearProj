// Toggle Dropdown visibility
function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}

// Show the specific form (Event, Hospital, Blood Bank)
function showForm(formId) {
    const forms = document.querySelectorAll('.container');
    forms.forEach(form => {
        if (form.id === formId) {
            form.style.display = 'block';
        } else {
            form.style.display = 'none';
        }
    });
}

// Validate phone number (custom function)
function validatePhoneNumber(phoneNumber) {
    // Regular expression for 10-digit phone numbers (numeric only)
    const phonePattern = /^\d{10}$/;
    return phonePattern.test(phoneNumber);
}

// Validation function for the forms
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    
    let valid = true;

    // Check each input element for empty fields
    inputs.forEach(input => {
        if (!input.value.trim()) {
            valid = false;
            alert(`${input.name} is required`);
        }
    });

    // Validate phone number for hospital form
    const hospitalContactInput = form.querySelector('#hospitalContact');
    if (hospitalContactInput && !validatePhoneNumber(hospitalContactInput.value.trim())) {
        valid = false;
        alert("Please enter a valid 10-digit phone number");
    }
    
    return valid;
}

// Event Form Submit handler
document.getElementById('eventFormSubmit')?.addEventListener('submit', function(e) {
    e.preventDefault();
    if (validateForm('eventForm')) {
        alert("Event added successfully!");
    }
});

// Hospital Form Submit handler
document.getElementById('hospitalFormSubmit')?.addEventListener('submit', function(e) {
    e.preventDefault();
    if (validateForm('hospitalForm')) {
        alert("Hospital added successfully!");
    }
});

// Blood Bank Form Submit handler
document.getElementById('bloodBankFormSubmit')?.addEventListener('submit', function(e) {
    e.preventDefault();
    if (validateForm('bloodBankForm')) {
        alert("Blood Bank added successfully!");
    }
});