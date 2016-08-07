$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var gamesock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host);

    gamesock.onmessage = function(message) {
        //var data = JSON.parse(message.data);
        //var game = $("#game")
        console.log(message);
        //game.append(ele)
    };

    $("#gameform").on("submit", function(event) {
//        var message = {
//            handle: $('#color').val(),
//            message: $('#name').val(),
//        }
        gamesock.send(JSON.stringify(message));
        //$("#message").val('').focus();
        return false;
    });
});