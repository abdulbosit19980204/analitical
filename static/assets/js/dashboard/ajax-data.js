function sendFilter() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        var startDate = document.getElementById('start-date').value;
        var endDate = document.getElementById('end-date').value;
        // var week = document.getElementById('week').value;
        // var month = document.getElementById('month').value;
        var d = {
            'startDate': startDate, 'endDate': endDate, // 'week': week,
            // 'month': month
        };


        console.log(d);
    }

    xhttp.open("POST", "/ecommerce", true);
    xhttp.send();
}

