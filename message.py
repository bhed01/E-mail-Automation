from email.message import EmailMessage

import mimetypes
import os
import smtplib


def create_message(sender, to, subject, message_text, html_msg=False, file=None):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
        html_msg: If set true message_text is treated as html.
        file: The path to the file to be attached.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = EmailMessage()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    if html_msg:
        message.add_attachment(message_text, 'html')
    else:
        message.set_content(message_text)

    if file:
        filename = os.path.basename(file)
        mime_type, _ = mimetypes.guess_type(file)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(file, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=filename)

    return message


def authenticate(sender):
    """Authenticate User.
    Args:
        sender: Email address of sender

    Returns:
        A server object instance.
    """
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.login(sender, os.environ.get('MAIL_PASS'))
    return server
