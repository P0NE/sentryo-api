from flask import request, json, Response, Blueprint
from ..models.people import PeopleModel, PeopleSchema


people_api = Blueprint('people', __name__)
people_schema = PeopleSchema()


@people_api.route('/', methods=['GET'])
def get_all():
    """
    get all peoples
    """
    peoples = PeopleModel.get_all_peoples()
    ser_peoples = people_schema.dump(peoples, many=True).data
    return custom_response(ser_peoples, 200)


@people_api.route('/<int:people_id>', methods=['GET'])
def get_people(people_id):
    """
    get one people
    """
    people = PeopleModel.get_one_people(people_id)
    if not people:
        return custom_response({'error': 'people not found'}, 404)

    ser_people = people_schema.dump(people).data
    return custom_response(ser_people, 200)


@people_api.route('/<int:people_id>', methods=['DELETE'])
def delete_people(people_id):
    """
    delete one people
    """
    people = PeopleModel.get_one_people(people_id)
    if not people:
        return custom_response({'error': 'people not found'}, 404)
    people.delete()
    return custom_response({'message': 'people with id {} deleted'.format(people_id)}, 204)


@people_api.route('/<int:people_id>', methods=['PUT'])
def update_people(people_id):
    """
    update one people
    """
    req_data = request.get_json()
    data, error = people_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    people = PeopleModel.get_one_people(people_id)
    if not people:
        return custom_response({'error': 'people not found'}, 404)
    people.update(data)
    ser_people = people_schema.dump(people).data
    return custom_response(ser_people, 200)


@people_api.route('/', methods=['POST'])
def create_people():
    """
    create a people
    """
    req_data = request.get_json()
    data, error = people_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if people already exist in db
    people_in_db = PeopleModel.get_people_by_name(data.get('name'))
    if people_in_db:
        return custom_response({'error': 'People already exist with this name'}, 400)

    people = PeopleModel(data)
    people.save()
    return custom_response({'message': 'people successfuly created'}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
