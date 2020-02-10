import unittest

from twitter_for_unittest import Twitter


class TwitterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.twitter = Twitter()

    def test_initialization(self):
        # Then
        self.assertTrue(self.twitter)

    def test_tweet_single(self):
        # When
        self.twitter.tweet('Test message')
        # then
        self.assertEqual(self.twitter.tweets, ['Test message'])


if __name__ == '__main__':
    unittest.main()
