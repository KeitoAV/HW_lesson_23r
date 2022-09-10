from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from builder import build_query
from models import RequestParams, BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400

    res = None
    for query in params['queries']:
        res = build_query(
            cmd=query['cmd'],
            param=query['value'],
            data=res
        )

    # res = build_query(
    #     cmd=params['cmd1'],
    #     param=params['value1']
    # )

    return jsonify(res)
