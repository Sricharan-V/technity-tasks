document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const passwordInput = document.getElementById("password");
    const passToggleBtn = document.getElementById("pass-toggle-btn");

    const showError = (field, errorText) => {
        field.classList.add("error");
        const errorElement = document.createElement("small");
        errorElement.classList.add("error-text");
        errorElement.innerText = errorText;
        field.closest(".form-group").appendChild(errorElement);
    }

    const handleFormData = (e) => {
        e.preventDefault();

        const fullnameInput = document.getElementById("fullname");
        const emailInput = document.getElementById("email");
        const dateInput = document.getElementById("date");
        const genderInput = document.getElementById("gender");

        const fullname = fullnameInput.value.trim();
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();
        const date = dateInput.value;
        const gender = genderInput.value;

        const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
        const passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        document.querySelectorAll(".form-group .error").forEach(field => field.classList.remove("error"));
        document.querySelectorAll(".error-text").forEach(errorText => errorText.remove());

        if (fullname === "") {
            showError(fullnameInput, "Enter your full name");
        }
        if (!emailPattern.test(email)) {
            showError(emailInput, "Enter a valid email address");
        }
        if (password === "") {
            showError(passwordInput, "Enter your password");
        } else if (!passwordPattern.test(password)) {
            showError(passwordInput, "Password must contain at least 8 characters, including 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special symbol");
        }
        if (date === "") {
            showError(dateInput, "Select your date of birth");
        }
        if (gender === "") {
            showError(genderInput, "Select your gender");
        }

        const errorInputs = document.querySelectorAll(".form-group .error");
        if (errorInputs.length > 0) return;

        form.submit();
    }

    passToggleBtn.addEventListener('click', () => {
        passToggleBtn.classList.toggle("fa-eye-slash");
        const inputType = passwordInput.type === "password" ? "text" : "password";
        passwordInput.type = inputType;
    });

    form.addEventListener("submit", handleFormData);
});