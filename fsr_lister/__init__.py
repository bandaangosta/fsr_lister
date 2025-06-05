import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.update(
    dict(
        TOKEN="define in instance/application.cfg",
        API_CALL_URL="define in instance/application.cfg",
        SECRET_KEY="define in instance/application.cfg",
    )
)
app.config.from_pyfile("application.cfg", silent=True)

import fsr_lister.views
