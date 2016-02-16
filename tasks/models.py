from django.db import models
from django.core.urlresolvers import reverse

class TaskList(models.Model):
    name = models.CharField(max_length=50)
    #rest of your model here

    def __str__(self):
        return self.name #??

    def get_absolute_url(self):
        return reverse('tasklist_edit', kwargs={'pk': self.pk})

class Task(models.Model):
    HIGH = 1
    NORMAL = 2
    LOW = 3
    PRIORITY_CHOICES = (
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
    )
    tasklist = models.ForeignKey(TaskList, null=False)
    name = models.CharField(max_length=100)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=NORMAL)
    #rest of your model here

    def __str__(self):
        return self.name #??

    def get_absolute_url(self):
        return reverse('task_edit', kwargs={'pk': self.pk})

    class Meta:
        order_with_respect_to = 'tasklist'
