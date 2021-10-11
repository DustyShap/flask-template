import datetime
import json
import os

from flask import (Flask, session,
                   render_template, url_for, redirect, request, jsonify)
from flask_session import Session
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker

from models import db, User
from create import create_app



app = create_app()
app.app_context().push()


# Routes

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
