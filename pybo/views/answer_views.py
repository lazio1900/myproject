from datetime import datetime

from flask import Blueprint, rul_for, request
from werkzerg.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

