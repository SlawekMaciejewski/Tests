import re


class Twitter(object):
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) > 160:
            raise Exception('Massage too long.')
        self.tweets.append(message)

    def find_hashtags(self, massage):
        return re.findall('#(\w+)', massage)


if __name__ == '__main__':
    twitter = Twitter()
    print(twitter.version, twitter.tweets)
    twitter.tweet('This is a test message')
    twitter.tweet('This is a test message2')
    twitter.tweet('#car #bus This is a test message with hashtag')
    print(twitter.tweets)
    print(twitter.find_hashtags(twitter.tweets[2]))
    print(twitter.find_hashtags(twitter.tweets[1]))
