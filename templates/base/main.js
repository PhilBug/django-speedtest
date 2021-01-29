var endpoint = '/api/chart/data/'
var defaultData = []
var labels = []

$(".run-button").click(function(e) {
    e.preventDefault();
    console.log('button-pressed')
    $(".run-button").attr("disabled", true).text("Test running...");
    $.ajax({
        type: "POST",
        url: "/api/test/run/",
        success: function(result) {
            setChartAsync();
            $(".run-button").attr("disabled", false).text("Run again");
        },
        error: function(result) {
            alert('error - please reload page');
        }
    });
});

function setChartAsync() {
    $.ajax({
        type: 'GET',
        url: endpoint,
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
    var ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Download speed in Mb/s',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
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