# Email Automation

It simple email automation project made using python. This project mainly consits of 6 files.

#### 1. main.py
This is the main file that needs to be executed using Python Interpreter.
```
python3 main.py
```

#### 2. message.py
This file contains the functions that are required for main.py to execute successfully.

#### 3. message.txt
The message to be sent goes to this file. In this file, words wrapped with curly braces are treated as variables that will receive values when sending mail.

#### 4. message_conf.json
This file contains the dictionary object that will be used to give value to some of the variables declared in message.txt

#### 5. temp.json
This file contains previously sent email addresses. When the main.py crashes due to an error, this file automatically updates with the email addresses to be excluded in the next run.

#### 6. data.csv
This file contains two columns named `Email Address` and `Full Name`.

### Requirements
This project requires:-
1. Python 3 interpreter
2. A valid email account from which the email will be sent.
3. You must also create an environment variable called `MAIL_PASS`, which is the password used to authenticate your email.  
**OR**
3. You can replace the code `os.environ.get('MAIL_PASS')` with your password in the file message.py.
