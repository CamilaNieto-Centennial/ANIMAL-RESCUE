"use strict";

    function formValidation() {

        var petsCurrentText = document.registration.petsCurrentText.value;
        var minorsNo = document.registration.minorsNo.value;
        var houseType = document.registration.houseType.value;//select


        var fencedYard = document.registration.fencedYard.value;//y/n
        var addExpText = document.registration.addExpText.value;//text

        //More Information
        var selected = [];
        for (var option of document.getElementById('animalsFoster').options) {
            if (option.selected) {
                selected.push(option.value);
            }
        }
        var animalsFoster = document.registration.animalsFoster.value;



        //Type information about your current pet(s)
        if (petsCurrentText == "") {
            alert('Type information about your current pet(s)!');

            document.registration.petsCurrentText.focus();

            return false;
        }

        if (minorsNo == "") {
            alert('Select Yes/No, Are there minors in your home?!');

            document.registration.minorsNoY.focus();

            return false;

        }


        if (houseType == "Default") {

            alert('Select your Housing Type from the list!');

            document.registration.houseType.focus();

            return false;

        }

        if (fencedYard == "") {
            alert('Select Yes/No, Do you have fenced yard?!');

            document.registration.fencedYardY.focus();

            return false;

        }

        if (addExpText == "") {
            alert('Type any additional experience of value!');

            document.registration.addExpText.focus();

            return false;
        }


        if (animalsFoster == "") {
            alert('Select what type(s) of animals are you interested in fostering?!');

            document.registration.animalsFoster.focus();

            return false;

        }






        /*
    -->  petsCurrentText
         minorsNo
         houseType
         fencedYard
         addExpText


        animalsFoster
*/
        //petsCurrently:Yes -petsCurrentText

        var commentText = document.registration.commentText.value;



        //petsCurrently
        if (petsCurrentText != '' && minorsNo != '' && houseType != '' && fencedYard != '' && addExpText != '' && animalsFoster != '') // condition for check mandatory all fields

        {
            let confirmation = "Once you submit this form, you can't go back \nAre you sure you want to leave this page?";
            if (confirm(confirmation) == true) {
                const dict_values = {petsCurrentText, minorsNo, houseType, fencedYard, addExpText, selected, commentText} //Pass the javascript variables to a dictionary.
                const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
                console.log(s); // Prints the variables to console window, which are in the JSON format


                //Passing the data to Python (into "/educateForm" page) ⏬
                $.ajax({
                    url:"/fosterForm2",
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