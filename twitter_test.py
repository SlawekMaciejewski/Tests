import unittest

from twitter import Twitter


class TwitterTest(unittest.TestCase):
    def test_initialization(self):
        # Given
        twitter = Twitter()
        # Then
        self.assertTrue(twitter)

    def test_tweet_single(self):
        # Given
        twitter = Twitter()
        # When
        twitter.tweet('Test message')
        # then
        self.assertEqual(twitter.tweets, ['Test message'])


if __name__ == '__main__':
    unittest.main()
