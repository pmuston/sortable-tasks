$(document).foundation();
$(function () {
    var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $("#sortable").sortable({
        axis: "y",
        cursor: "move",
        update: function (event, ui) {
            var order = $('#sortable').sortable('serialize');
            //$("#showmsg").text(order);
            //order = order.replace(/\[\]/gi, "");
            console.log("reorder",order);
            var path = window.location.pathname;
            path = path + "/task_sort";
            $.post(path, order, null);
        }
    });
    $("#sortable").disableSelection();
});
