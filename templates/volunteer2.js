"use strict";

    function formValidation() {


        var whyVolunteer = document.registration.whyVolunteer.value;//select
        var selected = [];
        for (var option of document.getElementById('enjoy').options) {
            if (option.selected) {
                selected.push(option.value);
            }
        }
        var enjoy = document.registration.enjoy.value;//MULTIPLE
        var gainText = document.registration.gainText.value;//text
        var selected2 = [];
        for (var option of document.getElementById('daysWeek').options) {
            if (option.selected) {
                selected2.push(option.value);
            }
        }
        var daysWeek = document.registration.daysWeek.value;//MULTIPLE
        var selected3 = [];
        for (var option of document.getElementById('timesDay').options) {
            if (option.selected) {
                selected3.push(option.value);
            }
        }
        var timesDay = document.registration.timesDay.value;//MULTIPLE


        var selected4 = [];
        for (var option of document.getElementById('skillsTxt').options) {
            if (option.selected) {
                selected4.push(option.value);
            }
        }
        var skillsTxt = document.registration.skillsTxt.value;//MULTIPLE
        var experienceText = document.registration.experienceText.value;//text
        var currentOcp = document.registration.currentOcp.value;//select
        var yearsOcp = document.registration.yearsOcp.value;//select

        if (whyVolunteer == "Default") {

            alert('Select why do you want to volunteer? from the list!');

            document.registration.whyVolunteer.focus();

            return false;

        }



        if (enjoy == "") {

            alert('Select what do you enjoy?!');

            document.registration.enjoy.focus();

            return false;

        }




        if (gainText == "") {

            document.registration.gainText.focus();

            alert('Type what you hope to gain from your volunteer experience!');

            return false;

        }

        if (daysWeek == "") {

            alert('Select what days on the week you are available!');

            document.registration.daysWeek.focus();

            return false;

        }

        if (timesDay == "") {

            document.registration.timesDay.focus();

            alert('Select the times on the day when you are available!');

            return false;

        }



        if (skillsTxt == "") {
            alert('Select your skill(s)!');

            document.registration.skillsTxt.focus();

            return false;

        }




        if (experienceText == "") {
            alert('Type your experience with animals!');

            document.registration.experienceText.focus();

            return false;
        }



        if (currentOcp == "Default") {

            alert('Select your Current Ocupation from the list!');

            document.registration.currentOcp.focus();

            return false;

        }

        if (yearsOcp == "Default") {

            alert('Select your Years in Occupation from the list!');

            document.registration.yearsOcp.focus();

            return false;

        }



        var commentText = document.registration.commentText.value;

        if (whyVolunteer != '' && enjoy != '' && gainText != '' && daysWeek != '' && timesDay != '' && skillsTxt != '' && experienceText != '' && currentOcp != '' && yearsOcp != '') // condition for check mandatory all fields

        {
            let confirmation = "Once you submit this form, you can't go back \nAre you sure you want to leave this page?";
            if (confirm(confirmation) == true) {
                const dict_values = {whyVolunteer, selected, gainText, selected2, selected3, selected4, experienceText, currentOcp, yearsOcp, commentText} //Pass the javascript variables to a dictionary.
                const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
                console.log(s); // Prints the variables to console window, which are in the JSON format


                //Passing the data to Python (into "/educateForm" page) ⏬
                $.ajax({
                    url:"/volunteerForm2",
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

