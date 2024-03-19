# python to run the whole package

import os
from taskmanager import app

# how and where to run the application
# checks the name class = main string. if yes then the app is running and we take the 3 arguments host, port and debug (stored in the environmant variable)
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

#------------------------------------------------------------------------------
