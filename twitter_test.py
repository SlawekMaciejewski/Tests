import pytest

from twitter import Twitter


@pytest.fixture()
def twitter(request):
    # print(request.module)
    twitter = Twitter()

    def fin():
        twitter.delete()

    request.addfinalizer(fin)
    return twitter



def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_long_message(twitter):
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
def test_tweet_with_hashtag(twitter, massage, expected):
    assert twitter.find_hashtags(massage) == expected
