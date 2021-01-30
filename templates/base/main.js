var endpointGET = '/api/chart/data/'
var endpointPOST = '/api/test/run/'
var defaultData = []
var labels = []

$(".run-button").click(function (e) {
    e.preventDefault();
    console.log('button-pressed')
    $(".run-button").attr("disabled", true).text("Test running...");
    $.ajax({
        type: "POST",
        url: endpointPOST,
        success: function (result) {
            setChartAsync();
            $(".run-button").attr("disabled", false).text("Run again");
        },
        error: function (result) {
            alert('error - please reload page');
        }
    });
});

function setChartAsync() {
    $.ajax({
        type: 'GET',
        url: endpointGET,
        success: function (responseData) {
            labels = responseData.labels
            defaultData = responseData.default
            setChart(labels, defaultData)
        },
        error: function (responseData) {
            console.log('error')
            console.log(responseData)
        }
    });
}


function setChart(labels, data) {
    console.log(data);
    var efficiency = [];
    var coloR = [];

    var dynamicColors = function () {
        var r = Math.floor(Math.random() * 255);
        var g = Math.floor(Math.random() * 255);
        var b = Math.floor(Math.random() * 255);
        return "rgb(" + r + "," + g + "," + b + ", 0.4)";
    };

    for (var i in data) {
        efficiency.push(data[i].efficiency);
        coloR.push(dynamicColors());
    }

    var chartData = {
        labels: labels,
        datasets: [{
            label: 'Download speed in Mb/s',
            backgroundColor: coloR,
            borderColor: 'rgba(200, 200, 200, 0.75)',
            hoverBorderColor: 'rgba(200, 200, 200, 1)',
            borderWidth: 1,
            data: data
        }]
    };

    var ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
setChartAsync();