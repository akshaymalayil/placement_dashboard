document.getElementById("profileForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const tenthAggregate = document.getElementById("tenthAggregate").value;
    const twelfthAggregate = document.getElementById("twelfthAggregate").value;
    const sgpa = {
        sem1: document.getElementById("sgpa1").value,
        sem2: document.getElementById("sgpa2").value,
        sem3: document.getElementById("sgpa3").value,
        sem4: document.getElementById("sgpa4").value,
        sem5: document.getElementById("sgpa5").value,
        sem6: document.getElementById("sgpa6").value,
        sem7: document.getElementById("sgpa7").value,
        sem8: document.getElementById("sgpa8").value
    };
    const courses = document.getElementById("courses").value;
    const certifications = document.getElementById("certifications").value;

    const profileData = {
        firstName: firstName,
        lastName: lastName,
        email: email,
        phone: phone,
        tenthAggregate: tenthAggregate,
        twelfthAggregate: twelfthAggregate,
        sgpa: sgpa,
        courses: courses,
        certifications: certifications
    };

    localStorage.setItem("profileData", JSON.stringify(profileData));

    alert("Profile data saved successfully!");
});

window.onload = function() {
    const savedData = localStorage.getItem("profileData");

    if (savedData) {
        const profileData = JSON.parse(savedData);

        document.getElementById("firstName").value = profileData.firstName;
        document.getElementById("lastName").value = profileData.lastName;
        document.getElementById("email").value = profileData.email;
        document.getElementById("phone").value = profileData.phone;
        document.getElementById("tenthAggregate").value = profileData.tenthAggregate;
        document.getElementById("twelfthAggregate").value = profileData.twelfthAggregate;
        document.getElementById("sgpa1").value = profileData.sgpa.sem1;
        document.getElementById("sgpa2").value = profileData.sgpa.sem2;
        document.getElementById("sgpa3").value = profileData.sgpa.sem3;
        document.getElementById("sgpa4").value = profileData.sgpa.sem4;
        document.getElementById("sgpa5").value = profileData.sgpa.sem5;
        document.getElementById("sgpa6").value = profileData.sgpa.sem6;
        document.getElementById("sgpa7").value = profileData.sgpa.sem7;
        document.getElementById("sgpa8").value = profileData.sgpa.sem8;
        document.getElementById("courses").value = profileData.courses;
        document.getElementById("certifications").value = profileData.certifications;
    }
};

