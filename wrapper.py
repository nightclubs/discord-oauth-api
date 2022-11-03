import requests

class api:
  
    def oauth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, code):
     r = requests.post(
         'https://discord.com/api/oauth2/token', 
          headers  = {'Content-Type': 'application/x-www-form-urlencoded'},
          data     = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
          }
     )
     if 'Cloudflare' in r.text:
       return 'IP Blocked'
     else:
       return r.json()['access_token']
    
    def guild_pull(bot_token, token, guild_id, id):
     r = requests.put(
         f'https://discord.com/api/guilds/{guild_id}/members/{id}',
         headers = {
             'Authorization' : f'Bot {bot_token}',
             'Content-Type': 'application/json'
         }, 
         json    = {"access_token" : token}
     ).json()
     return r
    
    
    def get_userinfo(token):
     headers = {
        "Authorization" : f"Bearer {token}"
     }
     r = requests.get(f"https://discord.com/api/users/@me", headers = headers)
     return r.json()
