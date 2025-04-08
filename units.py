from chatterbot import ChatBot

bot = ChatBot("units", logic_adapters=['chatterbot.logic.UnitConversion'])

while True:
    user_text = input("Ask question (unit conversion): ")
    chatbot_response = str(bot.get_latest_response(user_text))
    print(chatbot_response)