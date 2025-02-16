function searchBloodBanks() {
    const location = document.getElementById("locationInput").value.toLowerCase();
    const resultsDiv = document.getElementById("results");

    // Clear previous results
    resultsDiv.innerHTML = '';

    // Static list of blood banks for Mumbai
    const mumbaiBloodBanks = [
        { name: "Mumbai Blood Bank", address: "123, Mumbai Central, Mumbai", phone: "+91 123 456 7890" },
        { name: "Bharati Blood Bank", address: "456, Andheri West, Mumbai", phone: "+91 234 567 8901" },
        { name: "City Blood Bank", address: "789, Bandra, Mumbai", phone: "+91 345 678 9012" },
        { name: "Health Blood Bank", address: "321, Vile Parle, Mumbai", phone: "+91 456 789 0123" },
        { name: "Mumbai Red Cross Blood Bank", address: "654, Colaba, Mumbai", phone: "+91 567 890 1234" }
    ];

    // Check if the user searched for 'Mumbai'
    if (location === 'mumbai') {
        mumbaiBloodBanks.forEach(function(bloodBank) {
            const resultItem = document.createElement("div");
            resultItem.classList.add('result-item');
            resultItem.innerHTML = `
                <div class="result-title">
                    <strong>${bloodBank.name}</strong>
                </div>
                <div class="result-address">${bloodBank.address}</div>
                <div class="result-phone">Phone: ${bloodBank.phone}</div>
            `;
            resultsDiv.appendChild(resultItem);
        });
    } else {
        resultsDiv.innerHTML = "<p>No blood banks found for this location.</p>";
    }
}
