import pytest

from twitter import Twitter


@pytest.fixture
def backend(tmpdir):
    temp_file = tmpdir.join('test.txt')
    temp_file.write('')  # initialization empty temp_file
    return temp_file


@pytest.fixture(params=['list', 'backend'], name='twitter')
def fixture_twitter(backend, request):
    if request.param == 'list':
        twitter = Twitter()
    elif request.param == 'backend':
        twitter = Twitter(backend=backend)
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


def test_initialize_two_twitter_calsses(backend):
    # When
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    # Given
    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')

    # Then
    assert twitter2.tweets == ['Test 1', 'Test 2']


@pytest.mark.parametrize('massage, expected', (
        ('Test #first massage', ['first']),
        ('#first test massage', ['first']),
        ('#FIRST test massage', ['first']),
        ('Test massage #first', ['first']),
        ('Test message with #first and #second hashtags', ['first', 'second'])
))
def test_tweet_with_hashtag(twitter, massage, expected):
    assert twitter.find_hashtags(massage) == expected
