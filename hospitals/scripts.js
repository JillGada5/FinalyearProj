function searchHospitals() {
    const location = document.getElementById("locationInput").value.toLowerCase();
    const resultsDiv = document.getElementById("results");

    // Clear previous results
    resultsDiv.innerHTML = '';

    // Complete list of hospitals for Mumbai
    const mumbaiHospitals = [
        { name: "Kokilaben Dhirubhai Ambani Hospital", address: "Four Bungalows, Andheri West, Mumbai", phone: "+91 22 4269 6969" },
        { name: "Breach Candy Hospital", address: "Breach Candy Road, Mumbai", phone: "+91 22 2363 1001" },
        { name: "Lilavati Hospital", address: "A-791, Bandra West, Mumbai", phone: "+91 22 6677 2277" },
        { name: "Siddhivinayak Hospital", address: "Shivaji Park, Dadar, Mumbai", phone: "+91 22 2446 1852" },
        { name: "Hiranandani Hospital", address: "Hiranandani Gardens, Powai, Mumbai", phone: "+91 22 2576 7033" },
        { name: "Jaslok Hospital", address: "Dr. G Deshmukh Marg, Mumbai", phone: "+91 22 6657 2222" },
        { name: "Global Hospital", address: "L.B.S. Road, Goregaon West, Mumbai", phone: "+91 22 6700 6700" },
        { name: "SevenHills Hospital", address: "Marol Naka, Andheri East, Mumbai", phone: "+91 22 6776 2222" },
        { name: "Sion Hospital", address: "Sion, Mumbai", phone: "+91 22 2407 5741" },
        { name: "Rajawadi Hospital", address: "Ghatkopar East, Mumbai", phone: "+91 22 2510 7467" },
        { name: "Nair Hospital", address: "Dr. A.L. Nair Road, Mumbai", phone: "+91 22 2307 4272" },
        { name: "KEM Hospital", address: "Acharya Donde Marg, Parel, Mumbai", phone: "+91 22 2410 7000" },
        { name: "Holy Family Hospital", address: "Hill Road, Bandra West, Mumbai", phone: "+91 22 2642 1345" },
        { name: "Cumballa Hill Hospital", address: "Cumballa Hill, Mumbai", phone: "+91 22 2380 5536" },
        { name: "Fortis Hospital", address: "Mulund West, Mumbai", phone: "+91 22 6121 6000" },
        { name: "Wockhardt Hospital", address: "South Mumbai, Mumbai", phone: "+91 22 6650 3000" },
        { name: "Nightingale Hospital", address: "Andheri West, Mumbai", phone: "+91 22 2631 1067" },
        { name: "Bhatia Hospital", address: "Tardeo, Mumbai", phone: "+91 22 6660 5050" }
    ];

    // Check if the user searched for 'Mumbai'
    if (location === 'mumbai') {
        mumbaiHospitals.forEach(function(hospital) {

            const resultItem = document.createElement("div");
            resultItem.classList.add('result-item');
            resultItem.innerHTML = `
                <div class="result-title">
                    <strong>${hospital.name}</strong>
                </div>
                <div class="result-address">${hospital.address}</div>
                <div class="result-phone">Phone: ${hospital.phone}</div>
            `;
            resultsDiv.appendChild(resultItem);
        });
    } else {
        resultsDiv.innerHTML = "<p>No hospitals found for this location.</p>";
    }
}
