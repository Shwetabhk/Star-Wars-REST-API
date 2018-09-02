const card_template = UnderscoreTemplate(
    '<div class="col-sm-4" style="padding:3px">\
        <div class="card placard">\
        <img class="card-img-top card-image" src="<%- image %>" >\
            <div class="card-body">\
                <div class="card-title card-text">\
                    <h4 class="mt-2"> <%- name %></h4>\
                </div>\
            </div>\
        </div>\
    </div>'
);



$(document).ready(function () {
    var targetDiv = document.getElementById("planets");
    targetDiv.innerHTML = "";
    $.get('/get_user_planets?', function (data) {
        for (var i = 0; i < data.length; i++) {
            targetDiv.innerHTML += card_template(data[i])
        }
    });
});