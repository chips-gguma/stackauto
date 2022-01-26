import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-3007010903154-3009331608644-FwJCOGmN0HLk9UceeXdMBJrr"
 
post_message(myToken,"#stock","Hello World!")
