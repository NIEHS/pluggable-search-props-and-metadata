import time
import six
import logging

from werkzeug.exceptions import Unauthorized
from jose import JWTError, jwt
from swagger_server.api import api_utils

"""
util to to handle auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


class GridAuthUtil:
    def __init__(self):
        self.search_properties = api_utils.load_props()
        self.jwt_issuer = self.search_properties['jwt.issuer']
        self.jwt_secret = self.search_properties['jwt.secret']
        self.jwt_lifetime_seconds = self.search_properties['jwt.lifetime.seconds']
        self.jwt_algorithm = self.search_properties['jwt.algo']

    def check_bearer_auth(self, token):
        logger.debug('GridAuthUtil: check_bearer_auth()')
        logger.debug('args: \n token %s' % token)
        try:
            return jwt.decode(token, self.jwt_secret, algorithms=[self.jwt_algorithm])
        except JWTError as e:
            six.raise_from(Unauthorized, e)

    def generate_token(self, user_id):
        logger.debug('GridAuthUtil: generate_token()')
        logger.debug('args: \n token %s' % user_id)
        timestamp = self._current_timestamp()
        payload = {
            "iss": self.jwt_issuer,
            "iat": int(timestamp),
            "exp": int(timestamp + self.jwt_lifetime_seconds),
            "sub": str(user_id),
        }

        return jwt.encode(payload, self.jwt_secret, algorithm=self.jwt_algorithm)

    @staticmethod
    def get_secret(user, token_info) -> str:
        logger.debug('GridAuthUtil: get_secret()')
        return '''
        You are user_id {user} and the secret is 'xxx'.
        Decoded token claims: {token_info}.
        '''.format(user=user, token_info=token_info)

    @staticmethod
    def _current_timestamp() -> int:
        logger.debug('GridAuthUtil: _current_timestamp()')
        return int(time.time())

