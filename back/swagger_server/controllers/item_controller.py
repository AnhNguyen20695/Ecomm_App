import connexion
import six

from swagger_server.models.item import Item
from swagger_server import util


def get_item(itemId):
    """Returns item info by item id


    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def add_item(body):
    """Returns whether the item has been added


    :rtype: Bool
    """
    return 'do some magic!'


def update_item(body):
    """Returns whether the item has been updated


    :rtype: Bool
    """
    return 'do some magic!'


def delete_item(itemId):
    """Deletes the item by item id


    :rtype: Bool
    """
    return 'do some magic!'
