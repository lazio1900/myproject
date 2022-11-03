from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

# redirect(URL) - URL로 페이지를 이동
# url_for(라우팅 함수명) - 라우팅 함수에 매핑되어 있는 URL을 리턴
@bp.route('/')
def index():
    return redirect(url_for('question._list'))

