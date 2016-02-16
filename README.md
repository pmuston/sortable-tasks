# Tasks
Simple demo of using Django 1.9 order_with_respect_to and jQuery sortable.

steps:

    pip install -r requirements.txt
    createdb -Upostgres tasks
    python manage.py migrate
    python manage.py bower install

important code

model.py

    class Task(models.Model):
        tasklist = models.ForeignKey(TaskList, null=False)
    ...
        class Meta:
            order_with_respect_to = 'tasklist'

tasklist.html

    <ul id="sortable">
        {% for task in tasks %}
        <li id="task_{{task.id}}"><i class="fa fa-sort"></i> {{ task.name }}
        <a href="{% url "task_edit" task.id %}">edit</a>
        <a href="{% url "task_delete" task.id %}">delete</a>
        </li>
        {% endfor %}
    </ul>

urls.py

    url(r'^(?P<pk>\d+)/task_sort$', views.task_sort, name='task_sort'),

view.html

    def task_sort(request, pk, template_name=None):
        task_list = get_object_or_404(TaskList, pk=pk)
        tasks = Task.objects.filter(tasklist=task_list)
        if request.method=='POST':
            new_order = request.POST.getlist("task[]")
            new_order = [int(x) for x in new_order]
            print("New Order",new_order)
            print("Existing Order", task_list.get_task_order())
            task_list.set_task_order(new_order)
        return HttpResponse(status=200)

base.html

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