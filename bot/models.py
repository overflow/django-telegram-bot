from django.db import models

# Create your models here.
class Update(models.Model):
    update_id = models.CharField(primary_key=True, max_length='40')

"""
{'ok': True, 'result': [{'update_id': 821066347, 'message': {'text': 'asd', 'message_id': 7, 'from': {'first_name': 'Orlando', 'last_name': 'Fiol', 'id': 61208967, 'username': 'overf1ow'}, 'chat': {'first_name': 'Orlando', 'last_name': 'Fiol', 'id': 61208967, 'username': 'overf1ow'}, 'date': 1438263658}}]}

{'ok': True, 'result': [{'update_id': 821066348, 'message': {'reply_to_message': {'text': 'Aaarghhh!!!', 'message_id': 8, 'from': {'first_name': 'asomaote', 'username': 'asomaoBot', 'id': 117225746}, 'chat': {'first_name': 'Orlando', 'last_name': 'Fiol', 'id': 61208967, 'username': 'overf1ow'}, 'date': 1438263660}, 'text': 'gay', 'message_id': 9, 'from': {'first_name': 'Orlando', 'last_name': 'Fiol', 'id': 61208967, 'username': 'overf1ow'}, 'date': 1438263667, 'chat': {'first_name': 'Orlando', 'last_name': 'Fiol', 'id': 61208967, 'username': 'overf1ow'}}}]}

"""

class User (models.Model):
    id = models.IntegerField(primary_key=True)
    username =  models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Chat (models.Model):
    pass


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    message = models.TextField()
    json = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()

class Response(models.Model):
    message = models.ForeignKey(Message)
    reply_to = models.ForeignKey(Message, related_name='reply_to')

    class Meta:

        unique_together = ('message', 'reply_to')

