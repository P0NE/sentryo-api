from flask import request, json, Response, Blueprint
from ..models.people import PeopleModel, PeopleSchema


people_api = Blueprint('people', __name__)
people_schema = PeopleSchema()


@people_api.route('/', methods=['GET'])
def get_all():
    peoples = PeopleModel.get_all_peoples()
    ser_peoples = people_schema.dump(peoples, many=True).data
    return custom_response(ser_peoples, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
