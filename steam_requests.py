import requests

def get_steam_app_id(app_name):
    api_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

    try:
        response = requests.get(api_url)
        data = response.json()

        if "applist" in data and "apps" in data["applist"]:
            apps = data["applist"]["apps"]

            for app in apps:
                if  "name" in app and app["name"] == app_name:
                    return app["appid"]

            print(f"Error: app with the name {app_name} was not found.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_current_steam_players(app_name):
    app_id = get_steam_app_id(app_name)
    api_url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if "response" in data and "player_count" in data["response"]:
            return data["response"]["player_count"]
        
        print(f"couldn't find player count for {app_name}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None