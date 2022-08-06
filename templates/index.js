"use strict";

    function formValidation() {

        var emailRegex = /^[A-Za-z0-9._]*\@[A-Za-z]*\.[A-Za-z]{2,5}$/; // Expression for validating email
        var phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/; // Expression for validating phone number


        var fname = document.registration.FName.value;
        var lname = document.registration.LName.value;
        var phone = document.registration.phone.value;;
        var email = document.registration.email.value;
        var age = document.registration.age.value;
        var address = document.registration.Address.value;
        var city = document.registration.city.value;
        var postal = document.registration.postal.value;
        var province2 = document.registration.province2.value;
        var country = document.registration.country.value;

        var petType = document.registration.petType.value;
        var PName = document.registration.PName.value;




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



        if (phone == "") {

            document.registration.phone.focus();

            alert('Enter the phone!');

            return false;

        }

        else if (!phoneRegex.test(phone)) {

            alert('Re-enter the valid phone in this format: [xxx-xxx-xxxx, xxx.xxx.xxxx, xxx xxx xxxx]');

            document.registration.phone.focus();

            return false;

        }

        if (email == "") {

            document.registration.email.focus();

            alert('Enter the email!');

            return false;

        }

        else if (!emailRegex.test(email)) {

            alert('Re-enter the valid email in this format: [abc@abc.com]');

            document.registration.email.focus();

            return false;

        }


        //age, address, city, postal, province
        if (age == "") {
            alert('Enter the age!');

            document.registration.age.focus();

            return false;
        }
        else if (age < "18") {
            alert('You can not be under 18 years, sorry');

            document.registration.age.focus();

            return false;
        }


        if (address == "") {
            alert('Enter the address!');

            document.registration.Address.focus();

            return false;

        }

        if (city == "") {
            alert('Enter the city!');

            document.registration.city.focus();

            return false;

        }

        if (postal == "") {
            alert('Enter the postal!');

            document.registration.postal.focus();

            return false;

        }


        if (province2 == "") {
            alert('Type the province!');

            document.registration.province2.focus();

            return false;
        }


        if (country == "Default") {
            alert('Select your country from the list!');

            document.registration.country.focus();

            return false;
        }

        if (petType == "Default") {
            alert('Select the pet type from the list!');

            document.registration.petType.focus();

            return false;
        }

        if (PName == "") {
            alert('Enter the name of the pet!');

            document.registration.PName.focus();

            return false;

        }



        /*if (province == "other") {*/


            //age, address, city, postal, province, province2, country
            if (fname != '' && lname != '' && phone != '' && email != '' && age != '' && address != '' && city != '' && postal != '' && province2 != '' && country != '' && petType != '' && PName != '') // condition for check mandatory all fields

            {
                let confirmation = "Once you submit this form, you can't go back \nAre you sure you want to leave this page?";
                if (confirm(confirmation) == true) {
                    const dict_values = {fname, lname, phone, email, age, address, city, postal, province2, country, petType, PName} //Pass the javascript variables to a dictionary.
                    const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
                    console.log(s); // Prints the variables to console window, which are in the JSON format


                    //Passing the data to Python (into "/fosterForm" page) ⏬
                    $.ajax({
                        url:"/adoptForm",
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
                                window.location.href = "/adoptForm2";
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