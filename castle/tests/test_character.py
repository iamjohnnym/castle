import unittest
import castle

class TestClient(unittest.TestCase):
    def setUp(self):
        self.castle = castle
        self.player = self.castle.players[0].copy()
    
    def tearDown(self):
        del self.player

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

    def test_fresh_character_sheet(self):
        character_sheet = {
            "name":"string",
            "stats":{}
            }
        self.assertEquals(character_sheet.keys(), self.player.keys())

    def test_get_current_stats(self):
        current_stats_template = {
            "health": self.castle.set_health(self.player)
        }
        current_stats = self.castle.get_current_stats(self.player)

    def test_build_character(self):
        character_sheet = {
            "name":"string",
            "stats":{},
            "current_stats":{}
        }
        player = self.player
        player.update({"current_stats": self.castle.get_current_stats(player)})
        self.assertEquals(character_sheet.keys(), player.keys())
        self.assertEquals(player['current_stats']['health'], self.castle.set_health(player))

    def test_load_players(self):
        contenders = self.castle.load_players(self.castle.players)
        player_sheet = ['name', 'stats', 'current_stats']
        current_stats = ['health']
        stats = ['strength', 'constitution', 'agility']
        self.assertEquals(player_sheet.sort(), contenders[0].keys().sort())
        self.assertEquals(stats.sort(), contenders[0]['stats'].keys().sort())
        self.assertEquals(current_stats.sort(), contenders[0]['current_stats'].keys().sort())


if __name__ == '__main__':
    unittest.main()
