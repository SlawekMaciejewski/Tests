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
        twitter.tweet('test' * 41)
    assert twitter.tweets == []


@pytest.mark.parametrize('massage, expected', (
        ('Test #first massage', ['first']),
        ('#first test massage', ['first']),
        ('#FIRST test massage', ['first']),
        ('Test massage #first', ['first']),
        ('Test message with #first and #second hashtags', ['first', 'second'])
))
def test_tweet_with_hashtag(massage, expected):
    twitter = Twitter()
    assert twitter.find_hashtags(massage) == expected
