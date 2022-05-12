from nbresult import ChallengeResultTestCase

class TestB(ChallengeResultTestCase):

    def test_x(self):
        self.assertEqual(self.result.x, 1)

