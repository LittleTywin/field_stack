$("#btn").click(function(){

    var station = $("#station_select")[0].value;
    var csrf = getCookie('csrftoken');
    console.log(csrf);
    data = {'stationid':station};
    console.log(data);
    $.ajax('/visual/', 
    {
        type: "POST",
        headers: {'X-CSRFToken': csrf},
        mode: 'same-origin',
        data: data,
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
    var a = $("#station_select")[0].value;
    console.log(a);

});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
