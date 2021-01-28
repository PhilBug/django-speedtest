
var endpoint = '/api/data/'

var customersDjango = parseInt("{{ customers }}")

console.log(customersDjango)

$.ajax({
    type: "GET",
    url: endpoint,
    success: function (data) {
        console.log(data)
        console.log(data.customers * 234)
    },
    error: function (data) {
        console.log("error")
        console.log(data)
    }
});