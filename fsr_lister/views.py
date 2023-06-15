from flask import render_template
from datetime import datetime
from fsr_lister import app
from fsr_lister.lib.shiftlog import getData


@app.route("/")
def index():
    data = getData()
    return render_template("index.html", rows=data, now=datetime.utcnow())
