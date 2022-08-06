"use strict";

    function formValidation() {

        var houseType = document.registration.houseType.value;//select
        var adultsNo = document.registration.adultsNo.value;//number
        var minorsText = document.registration.minorsText.value;
        var frequency = document.registration.frequency.value;//select

        //More Information
        var petsBeforeText = document.registration.petsBeforeText.value;
        var petsCurrentText = document.registration.petsCurrentText.value;
        //--------------------
        var visit = document.registration.visit.value;
        var whenAdopt = document.registration.whenAdopt.value;



        if (houseType == "Default") {

            alert('Select your Housing Type from the list!');

            document.registration.houseType.focus();

            return false;

        }

        if (adultsNo == "") {
            alert('Enter the Number of adults in your home!');

            document.registration.adultsNo.focus();

            return false;

        }


        //Type the Number of Minors and their Ages
        if (minorsText == "") {
            alert('Type the Number of Minors and their Ages!');

            document.registration.minorsText.focus();

            return false;
        }


        if (frequency == "Default") {

            alert('Select the Frequency that someone is at home from the list!');

            document.registration.frequency.focus();

            return false;

        }


        //More Information

        if (petsBeforeText == "") {
            alert('Type which pet(s) you had before!');

            document.registration.petsBeforeText.focus();

            return false;
        }




        //Type information about your current pet(s)
        if (petsCurrentText == "") {
            alert('Type information about your current pet(s)!');

            document.registration.petsCurrentText.focus();

            return false;
        }

        //----------------

        if (visit == "") {
            alert('Select Yes/No, Are you planning to visit the location to adopt?!');

            document.registration.visitY.focus();

            return false;

        }


        if (whenAdopt == "Default") {

            alert('Select your Housing Type from the list!');

            document.registration.whenAdopt.focus();

            return false;

        }


        //minorsText
        //petsBeforeText
        //petsCurrentText

        var commentText = document.registration.commentText.value;

        //houseType, adultsNo, minorsNo, frequency, petsBefore, petsCurrently, visit, whenAdopt, minorsText, petsBeforeText, petsCurrentText
        if (houseType != '' && adultsNo != '' && minorsText != '' && frequency != '' && petsBeforeText != '' && petsCurrentText != '' && visit != '' && whenAdopt != '') // condition for check mandatory all fields

        {
            let confirmation = "Once you submit this form, you can't go back \nAre you sure you want to leave this page?";
            if (confirm(confirmation) == true) {
                const dict_values = {houseType, adultsNo, minorsText, frequency, petsBeforeText, petsCurrentText, visit, whenAdopt, commentText} //Pass the javascript variables to a dictionary.
                const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
                console.log(s); // Prints the variables to console window, which are in the JSON format


                //Passing the data to Python (into "/educateForm" page) ⏬
                $.ajax({
                    url:"/adoptForm2",
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
                            window.location.href = "/resultsForm";
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