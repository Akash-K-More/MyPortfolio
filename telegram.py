import requests
import login

def bot_sendtext(bot_message):
    bot_token = login.bot_token
    bot_chatID = login.bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=MarkdownV2&text=' + bot_message

    print(bot_message)
    response = requests.get(send_text)

    return response.json()


# bot_sendtext("HI")