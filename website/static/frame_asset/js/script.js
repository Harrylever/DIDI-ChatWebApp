$(document).ready(function () {
    // alert($('#username').val())
    let socket = io.connect("http://localhost:5000")
    socket.on('connect', function() {
        socket.send("User connected!");
    });

    socket.on('message', function(data) {
        $('#messages_display').append($('<p>').text(data));
    });

    $('#sendBtn').on('click', function() {
        let formdata = new FormData()
        let message = $('#message').val();
        let username = $('#username').val();
        let letter = username + ": " + message
        formdata.append('letter', letter);

        if ($('#username').val() == "" || $('#message').val() == "") {
            alert("Enter message...")
        } else {
            socket.send($('#username').val() + ': ' + $('#message').val());
            $('#message').val('');

            $.ajax({
                url: "/chathome",
                type: "POST",
                data: formdata,
                processData: false,
                contentType: false,
                success: function (response) {
                    console.log("Awesome")
                },
                error: function() {
                    console.log(err);
                }
            });
        }

    });

});