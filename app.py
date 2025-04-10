from flask import Flask ,redirect,url_for, render_template, request

app = Flask(__name__)


'''GET method is used to request/get data from a server. It's like saying, "Hey, server, give me this information.
Example: If you visit a webpage or click on a link, you're using a GET request.

 The POST method is used to send data to the server. It's like saying, "Hey, server, here’s some data I want to give you."
Example: When you submit a form on a website, you're using a POST request.
"'''
@app.route(rule='/' , methods = ["GET"])
def welcome():
    return "<h1>welcome to the channel</h1>"

@app.route(rule='/index' , methods = ["GET"])
def index():
    return "<h1>welcome to the index page</h1>"
# i can also return html content


# variable rule
@app.route('/success/<int:score>')
def success(score):
    return "person has pass and the score is :" + str(score)

# variable rule
@app.route('/fail/<int:score>')
def fail(score):
    return "person has fail and the score is :" + str(score)

# variable rule
@app.route(rule='/addition/<int:a>/<int:b>')
def addition(a,b):
    return "sum is " + str(a + b)

# url_for() : to redirect user to diff page
@app.route(rule='/result/<int:mark>')
def result(mark ):
    if mark > 50:
        return redirect(url_for('success' , score = mark))
    else:
        return redirect(url_for('fail' , score = mark))
    
# render_template to renter html file
# make html file in templates folder
@app.route(rule='/hello')
def hello():
    return render_template('hello.html')

# @app.route(rule='/form' , methods=["GET" , "POST"] )
# def form():
#     if request.method == "GET":
#         return render_template('form.html')    # create another folder template in that create form.html file





if __name__ == '__main__':
    app.run(debug=True)