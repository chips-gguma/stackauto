from slacker import Slacker

slack = Slacker('xoxb-3007010903154-3009331608644-66sM6PyTSfy36F5EUsdMZHJC')

# Send a message to #general channel
slack.chat.post_message('#stock', 'Hello fellow slackers!')