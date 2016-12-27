import datetime
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    email = models.EmailField()


def __unicode__(self):
    return self.user_name + ' with email - ' + self.email


class UserRequest(models.Model):
    REQUEST_RECEIVED = 'Request received'
    REQUEST_SENT_TO_DU = 'Request sent to datausa'
    ANSWER_RECEIVED_FROM_DU = 'Answer received from datausa'
    ERROR = 'Error'
    ANSWER_DELIVERED_TO_USER = 'Answer to request delivered to the user'
    STATUS_CHOICES = (
                        (REQUEST_RECEIVED, REQUEST_RECEIVED),
                        (REQUEST_SENT_TO_DU, REQUEST_SENT_TO_DU),
                        (ANSWER_RECEIVED_FROM_DU, ANSWER_RECEIVED_FROM_DU),
                        (ERROR, ERROR),
                        (ANSWER_DELIVERED_TO_USER, ANSWER_DELIVERED_TO_USER),

                    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_id = models.UUIDField(blank=True, primary_key=True)
    update_time = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=REQUEST_RECEIVED)
    data = models.TextField()

    def __unicode__(self):
        return self.request_id + ' has status of - ' + self.status