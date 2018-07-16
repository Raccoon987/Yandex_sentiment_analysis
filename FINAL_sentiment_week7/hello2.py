#import main application class Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#Form class handles forms, represent the form and knows all about it fields, how to validate them
from flask_wtf import Form
#importing fields of the form - field for string - where name should be typed and submit button
from wtforms import StringField, SubmitField
#small validator classes that helps not no validate fields by yourself. Required - said that field is 
#required, so submiting empty field will raise validation error; length- restrict the length of the 
#content 
from wtforms.validators import Required, Length
import my_sentiment_classifier

app = Flask(__name__)
#encryption key that generate a token to prevent CSRF attack
app.config["SECRET_KEY"] = "top secret!"
bootstrap = Bootstrap(app)

#check is the text in latin  
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

#create a class for any form and tis class knows all about it fields and their validation
class NameForm(Form):
    #add more class fields - variables name, validators
    name = StringField("Put Your rewiev here", validators=[Required(), Length(1, 3000)])
    #Submit will be a label on the button and button require no validation
    submit = SubmitField("Submit")
    

#function index is assossiated with url "/" 
@app.route("/", methods=["GET", "POST"])
def index():
    #keep track on have on not have the name
    name = None
    #instansiate the form
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        #if is_ascii(name):
        #    cls_obj = my_sentiment_classifier.MySentimentClassifier()
        #    name = cls_obj.get_prediction_message(name)
        #else:
        #    name = None
        cls_obj = my_sentiment_classifier.MySentimentClassifier()
        name = cls_obj.get_prediction_message(name)
        
    return render_template("index.html", form=form, name=name)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
    

if __name__ == "__main__":
    #enables debugger from the broser - show all possible errors right in the broser 
    #window - as far as I can see...
    app.run(debug=True, port=8080)