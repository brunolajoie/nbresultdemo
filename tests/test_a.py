from nbresult import ChallengeResultTestCase

class TestA(ChallengeResultTestCase):

    def test_x(self):
        self.assertEqual(self.result.x, 1)

