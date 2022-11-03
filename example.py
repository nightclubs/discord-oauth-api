from wrapper import *; import flask; from flask import *


lol = api

app = Flask(__name__)
@app.route('/callback')
def callback():
  code = request.args.get('code'); token = lol.oauth(client_id, 'client_secret', 'redirect_url', code)
  return redirect('https://github.com/accusable/discord-oauth-api')


    
app.run("0.0.0.0", 80)
 
