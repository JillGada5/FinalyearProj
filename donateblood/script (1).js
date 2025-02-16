document.getElementById('donationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    if (!fullName || !email || !phone) {
        alert('Please fill in all required fields.');
        return;
    }

    const phonePattern = /^[0-9]{10}$/;
    if (!phonePattern.test(phone)) {
        alert('Please enter a valid 10-digit phone number.');
        return;
    }

    alert('Form submitted successfully!');
    this.reset();
});

// Highlight selected checkboxes
document.querySelectorAll('.dropdown-content input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        if (this.checked) {
            this.parentElement.style.backgroundColor = '#f0f0f0'; // Highlight selected checkbox
        } else {
            this.parentElement.style.backgroundColor = ''; // Remove highlight
        }
    });
});