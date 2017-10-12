#character

# stats
# # weapon dmg
# # speed
# # health
# # name

# battle
# # Player Character
# # NonPlayerCharacter or PC
# # Round
# # Damage

players = [
    {
        "name":"aimbotd",
        "stats":{
            "strength":6,
            "constitution":5,
            "agility":4
        }
    },
    {
        "name":"dedrea",
        "stats":{
            "strength":6,
            "constitution":5,
            "agility":4
        }
    },
    {
        "name":"ouro",
        "stats":{
            "strength":2,
            "constitution":6,
            "agility":7
        }
    }
]

def load_players(players):
    for player in players:
        pass


def get_stat(player, stat, stat_type='stats'):
    return player[stat_type][stat]

def get_strength(player):
    return get_stat(player, 'strength')

def get_constitution(player):
    return get_stat(player, 'constitution')

def get_agility(player):
    return get_stat(player, 'agility')

def get_name(player):
    return player['name']

def set_health(player, modifier=3):
    constitution = get_constitution(player)
    return constitution * modifier

def get_current_stats(player):
    if player.has_key('current_stats'):
        return player['current_stats']
    current_stats = player['current_stats'] = {}


def build_character(player):
    stats = dict(
        strength = get_strength(player),
        constitution = get_constitution(player),
        agility = get_agility(player)
        )
    
    name = get_name(player)
    current_stats = get_current_stats(player)

    character = dict(
        stats = stats,
        name = name,
        current_stats = current_stats
    )
    return character

def name():
    pass

def run():
    while True:
        try:
            input = raw_input()
        except (KeyboardInterrupt, SystemExit):
            raise


if __name__ == "__main__":
    run()
