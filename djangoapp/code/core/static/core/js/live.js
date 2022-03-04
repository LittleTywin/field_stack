setInterval(getdata,5000);

function getdata(){
    $.ajax('/live/', 
    {
        type: "GET",
        dataType: 'json', // type of response data
        timeout: 500,     // timeout milliseconds
        success: function (data,status,xhr) {   // success callback function
            console.log("Success!!");
            console.log(data);
            $("#livediv").html(JSON.stringify(data));
        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log("Ajax error:" + errorMessage);
        }
    });
}