from message import create_message, authenticate
from csv import DictReader
import json


def main():
    subject = input("Enter the subject: ")

    #Loading the message text form message.txt
    with open('message.txt') as file:
        message_text = file.read()

    #Loading values to be placed in message
    with open('message_conf.json') as file:
        conf = json.load(file)

    #Loading previously sent email addresses
    with open('temp.json') as file:
        send = set(json.load(file))

    count = len(send) + 1
    server = authenticate('sender@gmail.com')

    with open('data.csv') as fp:
        for user in DictReader(fp):
            email = user['Email Address']
            name = user['Full Name']
            if email not in send:
                print(f'Sending a mail to {email}')
                msg = message_text.format(name=name, **conf)
                message = create_message('sender@gmail.com', email, subject, msg, html_msg=True)
                try:
                    server.send_message(message)
                except BaseException as e:
                    print(f"An error occurred: {e}")
                    with open('temp.json', 'w') as file:
                        file.write(json.dumps(list(send)))
                    break
                send.add(email)
                print(f'Mails sent {count}\n')
                count += 1
        else:
            with open('temp.json', 'w') as file:
                file.write(json.dumps([]))


if __name__ == '__main__':
    main()
