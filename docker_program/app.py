from flask import Flask,
request,
render-template #type :ignore
#import the necessasary components from the flask framework
# -Flask:the main class for creatng the web application
#  -request:used to handle data sent by the client(like form data)
# -render_template:used to render HTML templates
#the comment "#type:ignore" is used to suppress type-checking warnings from tools like MyPy
app =Flask(__name__) #create a flask application
@app.route('/register',methods=['GET','POST']) #defines aroute for the URL "/register" that accepts both GET  and POST request
#GET 
# this is used to display the registration form to the user
#when someone visists/register in their browser ,a GET request is sent,and your code should return an HTML form.
# POST 
#this is use dto process the submitted
def register():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')