import pytest

from twitter import Twitter


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter

def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']

def test_tweet_long_message():
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []

def test_tweet_with_hashtag():
    twitter = Twitter()
    massage = 'Test #first massage'
    twitter.tweet(massage)
    print(twitter.tweets)
    assert 'first' in twitter.find_hashtags(twitter.tweets[0])

def test_tweet_with_hashtag_on_beginning():
    twitter = Twitter()
    massage = '#first test massage'
    twitter.tweet(massage)
    print(twitter.tweets)
    assert 'first' in twitter.find_hashtags(twitter.tweets[0])

