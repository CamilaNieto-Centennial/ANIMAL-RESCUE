"use strict";


function formValidation() {

    var emailRegex = /^[A-Za-z0-9._]*\@[A-Za-z]*\.[A-Za-z]{2,5}$/; // Expression for validating email

    var fname = document.registration.FName.value;
    var lname = document.registration.LName.value;
    var email = document.registration.email.value;


    if (fname == "") {
        alert('Enter the first name!');
        document.registration.FName.focus();
        return false;
    }

    if (lname == "") {
        document.registration.LName.focus();
        alert('Enter the last name!');
        return false;
    }

    if (email == "") {
        document.registration.email.focus();
        alert('Enter the email!');
        return false;
    }

    if (!emailRegex.test(email)) {
        alert('Re-enter the valid email in this format: [abc@abc.com]');
        document.registration.email.focus();
        return false;
    }



    if (fname != '' && lname != '' && email != '') // condition for check mandatory all fields
    {
        let confirmation = "Once you submit this form, you can't go back \nAre you sure you want to leave this page?";
        if (confirm(confirmation) == true) {
            const dict_values = {fname, lname, email} //Pass the javascript variables to a dictionary.
            const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
            console.log(s); // Prints the variables to console window, which are in the JSON format


            //Passing the data to Python (into "/educateForm" page) ⏬
            $.ajax({
                url:"/educateForm",
                type:"POST",
                contentType: "application/json",
                data: JSON.stringify(s)});


            //Get the URL
            var urlPath = window.location.origin+window.location.pathname;
            console.log(urlPath);

            //Using response status
            fetch(urlPath)
                .then(response => {
                    console.log('response.status: ', response.status); // 👉️ 200 (from "GET")
                    console.log(response);
                    if(response.status == 200) {
                        window.location.href = "/educateForm2";
                    }
                })
                .catch(err => {
                    console.log(err);
                    alert('Form not valid');
                });

        }
    }

}

function setUpPage(){
    formValidation();
}


window.addEventListener("load", setUpPage, false);