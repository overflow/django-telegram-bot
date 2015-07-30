from django.core.management.base import BaseCommand

from bot.models import *

import urllib.request
import urllib.parse
import codecs
import json
import datetime
import time

class Command(BaseCommand):
    help = "Run telegram bot."
    token = ''
    url = 'https://api.telegram.org/bot' + token + '/'
    
    def _user(self, message):
        try:
            user = User.objects.get(id=format(message['from']['id']))
        except  User.DoesNotExist:
            first_name = ''
            last_name = ''
            if 'first_name' in message['from']:

                first_name = message['from']['first_name'] 

            if 'last_name' in message['from']:
                last_name = message['from']['last_name']
            user = User.objects.create(id=format(message['from']['id']), first_name=first_name, last_name=last_name)
            if ('username' in message['from']):
                user.username = message['from']['username']
                user.save()
        return user

    def _doBotStuff(self, updateId):
        try:
            data = urllib.parse.urlencode({'offset': format(updateId), 'limit': '100', 'timeout': '60'})
            response = urllib.request.urlopen(self.url + 'getUpdates', data.encode('utf-8'))
            reader = codecs.getreader("utf-8")
            data = json.load(reader(response))
            print (data)
        except Exception as e:
            #logging.warning('Something went wrong when fetching updates: ' + str(e))
            return updateId
        if data['ok'] == True:
            for update in data['result']:
                
                # take new update id
                updateId = update['update_id'] + 1
                message = update['message']
                
                # respond if this is a message containing text

                if 'text' in message:
                    messagetext = str(message['text'])

                    # skip any commands except "/start" because we don't do commands in zombieland
                    if messagetext.startswith('/') and not messagetext.startswith('/start'):
                        continue
                    user = self._user(message)
                    
                    messagesaved = Message.objects.filter(id=message['message_id'])
                    if not messagesaved.exists():
                        messagesaved = Message.objects.create(message=messagetext, user=user, json=str(data), id=message['message_id'], date=datetime.datetime.fromtimestamp(int(message['date'])).strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        messagesaved = messagesaved[0]
                    if 'reply_to_message' in message:
                        try:
                            messagereply = Message.objects.get(id=message['reply_to_message']['message_id'])
                        except Message.DoesNotExists:
                            messagereply = Message.objects.create(id=message['reply_to_message']['message_id'], message=message['reply_to_message']['text'], user=user, json=data, date=datetime.datetime.fromtimestamp(int(message['reply_to_message']['date'])).strftime('%Y-%m-%d %H:%M:%S'))

                        
                        Response.objects.get_or_create(message=messagesaved, reply_to=messagereply)

                    # compose and send a reply (in zombie language)
                    #chatId = message['chat']['id']
                    #text = random.choice(strings)
                    #sendSimpleMessage(chatId, text)
        return updateId

    def handle(self, *args, **options):
        # make sure the file exists and contains an integer
        update = Update.objects.all()
        if update.exists():
            updateId=update[0].update_id
        else:
            updateId=0
            Update.objects.create(update_id=0)
        
        # main program loop
        while True:

            # process updates
            newUpdateId = self._doBotStuff(updateId)

            # write the update ID to a file and sleep 3 seconds if we processed updates
            if newUpdateId != updateId or  (newUpdateId == updateId and updateId == 0):
                update[0].update_id = newUpdateId
                update[0].save()
                updateId = newUpdateId
                
            else:
                # otherwise, sleep 1 second; we can wait some more during long polling if we have to.
                print ('time')
                time.sleep(1)

