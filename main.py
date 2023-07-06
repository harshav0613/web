from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # instantiate the mail class

    # configuration of mail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'info.autoinnovationtech@gmail.com'
    app.config['MAIL_PASSWORD'] = 'dtoiyueowexrdenz'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msgBody = f"Name: {name} \nEmail: {email} \nsubject: {subject} \nMessage: {message}"
        msg = Message(subject=f"Enquiry from {name} {subject}", body=msgBody, sender='info.builtintech',
                      recipients=['kharsha06132002@gmail.com'])
        mail.send(msg)
        return render_template('index.html', message_sent=True)
    else:
        return render_template('index.html', message_sent=False)


if __name__ == '__main__':
    app.run(debug=True)
