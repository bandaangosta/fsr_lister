import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.update(
    dict(
        TOKEN="define in instance/application.cfg",
        API_CALL_URL="https://asa.alma.cl/webslt/service/api/entries",
        SECRET_KEY="N563gGabaQlav1gsKn",
    )
)
app.config.from_pyfile("application.cfg", silent=True)

import fsr_lister.views
