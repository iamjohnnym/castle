import unittest
import castle

class TestClient(unittest.TestCase):
    def setUp(self):
        self.castle = castle
        self.player = self.castle.players[0]

    def test_get_players(self):
        self.assertEquals(3, len(self.castle.players))

    def test_get_name(self):
        self.assertEquals('aimbotd', self.castle.get_name(self.player))

    def test_get_constitution(self):
        self.assertEquals(5, self.castle.get_constitution(self.player))

    def test_get_strength(self):
        self.assertEquals(6, self.castle.get_strength(self.player))

    def test_get_agility(self):
        self.assertEquals(4, self.castle.get_agility(self.player))

    def test_player(self):
        


if __name__ == '__main__':
    unittest.main()
