from sanic import Blueprint, response

hello = Blueprint('hello_api', url_prefix='/hello')


@hello.route('/world')
async def hello_api(request):
    return response.json({'hello': 'world'})
