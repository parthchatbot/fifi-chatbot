from flask import Flask,render_template,request 
from chatterbot import ChatBot                  
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)
FiFi = ChatBot("FiFi", storage_adapter="chatterbot.storage.SQLStorageAdapter") 

trainer = ChatterBotCorpusTrainer(FiFi)
trainer.train("chatterbot.corpus.english")
trainer.train("data") 

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/get")
def get_bot_response():
    userText=request.args.get("msg") 
    return str(FiFi.get_response(userText))

if __name__=="__main__":
    app.run(debug=True)