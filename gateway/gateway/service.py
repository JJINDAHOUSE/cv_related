import json

from marshmallow import ValidationError
from nameko import config
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.entrypoints import http
from gateway.exceptions import CounterNotFound

class GatewayService:
    """
    Service acts as a gateway to other services over http.
    """
    name = 'gateway'

    region_counter_rpc = RpcRpoxy('region_counter')

    @http(
            "GET", "/counters/<string:counter_id>",
            expected_exceptions = CounterNotFound
    )
    def get_counter(self):
        """
        Gets counter
        """
        pass

    @http(
            "POST", "/counters/<string:source_address>",
            expected_exceptions = (ValidationError, BadRequest)
    )
    def create_counter(self):
        """
        Create a new region counter
        """
        pass
