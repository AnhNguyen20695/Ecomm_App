import connexion
import six

from swagger_server.models.store import Store
from swagger_server import util


def get_inventory():
    """Returns store inventory


    :rtype: Dict[str, int]
    """
    return 'do some magic!'
