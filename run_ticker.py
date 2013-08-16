from config import web_opts, base_url, run_opts
import webbrowser
from FussiWeb import app
import bottle

# Run the browser
# This should go in a separate script!!!
webbrowser.open(base_url, **web_opts)

# Run the app
bottle.run(app=app, **run_opts)

