
from flask import Flask, render_template, request

app = Flask(__name__)

#######################
##### Page acueil #####
#######################
@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")


######################
##### question 1 #####
######################
@app.route('/question1',methods=['POST','GET'])
def question1():
    return render_template("question1.html")


######################
##### question 2 #####
######################
@app.route('/question2',methods=['POST','GET'])
def question2():
    return render_template("question2.html")


######################
##### question 3 #####
######################
@app.route('/question3',methods=['POST','GET'])
def question3():
    return render_template("question3.html")


######################
##### question 4 #####
######################
@app.route('/question4',methods=['POST','GET'])
def question4():
    return render_template("question4.html")


######################
##### question 5 #####
######################
@app.route('/question5',methods=['POST','GET'])
def question5():
    return render_template("question5.html")


##################
##### Perdue #####
##################
@app.route('/game_over',methods=['POST','GET'])    
def game_over():
    return render_template("game_over.html")


#################
##### Gagné #####
#################
@app.route('/win',methods=['POST','GET'])    
def win():
    return render_template("win.html")

#########################
##### Régle et aide #####
#########################
@app.route('/rules',methods=['POST','GET'])
def rules():
    return render_template("rules.html")

app.run(host="0.0.0.0",debug=True)