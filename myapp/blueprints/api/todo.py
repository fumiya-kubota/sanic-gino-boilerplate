from sanic import Blueprint, response
from sanic.views import HTTPMethodView
from myapp.models import Todo

todo = Blueprint('todo_api', url_prefix='/todo')


class TodoView(HTTPMethodView):
    async def get(self, request):
        todos = await Todo.query.gino.all()
        return response.json({'todo_list': [todo.to_dict() for todo in todos]})

    async def post(self, request):
        data = request.json
        await Todo.create(name=data['name'])
        return response.json({'result': 'OK'}, status=201)


@todo.route('/<todo_id>', methods=['DELETE'])
async def delete_todo(request, todo_id):
        await Todo.delete.where(Todo.id == int(todo_id)).gino.status()
        return response.json({'result': 'OK'})


todo.add_route(TodoView.as_view(), '')
