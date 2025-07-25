import requests

# Manual fallback metadata for known games
manual_game_data = {
    "Need For Speed Prostreet": {
        "name": "Need for Speed: ProStreet",
        "released": "2007-11-13",
        "rating": "7.2",
        "cover": "https://upload.wikimedia.org/wikipedia/en/1/16/NFS_ProStreet_cover.png"
    },
    "Pursuit Force": {
        "name": "Pursuit Force",
        "released": "2005-11-18",
        "rating": "7.5",
        "cover": "https://upload.wikimedia.org/wikipedia/en/8/89/Pursuit_Force.jpg"
    },
    "Pokemon Omega Ruby": {
        "name": "Pokémon Omega Ruby",
        "released": "2014-11-21",
        "rating": "8.6",
        "cover": "https://upload.wikimedia.org/wikipedia/en/f/f1/AlphaSapphire.jpg"
    }
}

def fetch_game_data(title):
    # Check manual fallback first
    if title in manual_game_data:
        return manual_game_data[title]

    # Otherwise try RAWG API
    try:
        res = requests.get(
            f"https://api.rawg.io/api/games?search={title}&page_size=1",
            headers={"User-Agent": "RetroAI"}
        )
        data = res.json()
        if data['results']:
            game = data['results'][0]
            return {
                "name": game['name'],
                "released": game.get('released', 'N/A'),
                "rating": game.get('rating', 'N/A'),
                "cover": game.get('background_image')
            }
    except:
        return None
