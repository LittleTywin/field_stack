$("#btn").click(function(){
    $.ajax('/visual', 
    {
        dataType: 'json', // type of response data
        timeout: 500,     // timeout milliseconds
        success: function (data,status,xhr) {   // success callback function
            console.log("Success!!");
            console.log(data['data']);
            $("#out").html(JSON.stringify(data['data']));
        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log("Ajax error:" + errorMessage);
        }
    });

});