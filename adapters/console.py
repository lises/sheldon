"""
# Config (valid YAML document) must be at __doc__.
name: console # Name of adapter, lowercase, match with
              # file or package name.
description: "Example adapter for testing bot."
config:                           # Config variable that needed to set
  - SHELDON_CONSOLE_PROMPT: '>>>' # in environment.
                                  # You can set default values after colon.
"""
from sheldon.adapter import IncomingMessage, Attachment
from random import randint
from os import getlogin

# Code running on adapter loading may be here


def get_messages(bot):
    while True:
        text = input('Enter message: ')

        attachments = []
        # For our example, attachment will be looking like:
        # '[type]_[path]'
        received_attachments = input(
            'Enter a comma-separated attachments'
            '(<type>_<path>):'
        ).split(',')

        # If user don't enter attachment,
        # message_attachments will be empty
        if received_attachments[0]:
            for attachment in received_attachments:
                # Parse incoming attachment:
                # attachment_data[0] will be attachment type
                # attachment_data[1] will be attachment path
                attachment_data = attachment.split('_')
                if len(attachment_data) < 2:
                    print('Incorrect attachment "{}"'.format(attachment))
                    continue
                attachments.append(Attachment(
                    attachment_type=attachment_data[0],
                    attachment_path=attachment_data[1:],
                    attachment_id=randint(1, 1000000000)  # Fake id
                ))

        yield IncomingMessage(sender=User(username=getlogin()), message_text=text,
                              message_attachments=attachments, variables={
                                  'console_id': randint(1, 1000000000)  # Fake id
                              })


def send_message(Message, bot):
    print('BOT: ', Message.text)
    print('Channel: ', Message.channel)
    print('Attachments:')
    for attachment in Message.attachments:
        print(attachment.id)
        print(attachment.type)
        print(attachment.path)
        print(attachment.text)


# Adapter must have implementation of User class.
class User:
    def __init__(self, username):
        """
        Create new User for console adapter

        :param username: name in bash session
        :return:
        """
        # Adapter object should have 'id' and 'username' params.
        self.id = hash(username)
        self.username = username
