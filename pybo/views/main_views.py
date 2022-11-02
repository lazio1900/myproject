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
    # url_for : 라우팅 함수를 찾는다. question은 등록된 블루프린트 별칭, _list는 블루프린트에 등록된 함수명
    # _list 함수에 등록된 URL 매핑 규칙은 @bp.route('/list/')이므로 url_for('question._list')는
    # bp의 프리픽스 URL인 /question/과 /list/가 더해진 /question/list/ URL을 반환한다.
    return redirect(url_for('question._list'))
