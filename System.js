function get_metrics() {
    var python = require("python-shell")
    var path = require("path")

    var options = {
        scriptPath: path.join(__dirname, '/../engine/'),
    }
    var metrics = new python('metrics1.py', options);

    metrics.on('message', function (message) {
        swal(message);
    })


}