import os
import re


class Twitter(object):
    version = '1.0'

    def __init__(self, backend=None):
        self.backend = backend
        self._tweets = []

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            self._tweets = [line.rstrip('\n') for line in self.backend.readlines()]
        return self._tweets

    def tweet(self, message):
        if len(message) > 160:
            raise Exception('Message too long.')
        self.tweets.append(message)
        if self.backend:
            self.backend.write('\n'.join(self.tweets))

    def find_hashtags(self, massage):
        return [m.lower() for m in re.findall("#(\w+)", massage)]


if __name__ == '__main__':
    twitter = Twitter(backend='tweets.txt')
    print(twitter.version, twitter.tweets)
    # twitter.tweet('This is a test message')
    # twitter.tweet('This is a test message2')
    # twitter.tweet('#cAr #Bus This is a test message with hashtag')
    # print(twitter.tweets)
    # print(twitter.find_hashtags(twitter.tweets[2]))
    # print(twitter.find_hashtags(twitter.tweets[1]))
