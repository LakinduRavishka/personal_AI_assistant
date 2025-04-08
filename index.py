from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import json

app = Flask(__name__)

bot = ChatBot("Bot", read_only=False,
              logic_adapters=[
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "Sorry I don't have an answer.",
                      "maximum_similarity_threshold": 0.9
                  }
              ])

# Train using ListTrainer from JSON
list_trainer = ListTrainer(bot)
with open("about_me.json", "r") as file:
    data = json.load(file)
    for convo in data["conversations"]:
        list_trainer.train(convo)

# Also train with default ChatterBot corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
