from sanic import Blueprint
from sanic import response

hello = Blueprint('hello_page', url_prefix='/hello')


@hello.route('/world')
async def hello_api(request):
    return response.text('Hello, World!!')
