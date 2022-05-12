from nbresult import ChallengeResultTestCase

class TestC(ChallengeResultTestCase):

    def test_x(self):
        self.assertEqual(self.result.x, 1)

