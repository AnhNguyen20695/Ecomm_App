# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Item(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, quantity: int=None, status: str=None):
        """Item - a model defined in Swagger

        :param id: The id of this Item.
        :type id: int
        :param item_id: The item_id of this Item.
        :type item_id: int
        :param quantity: The quantity of this Item.
        :type quantity: int
        :param status: The status of this Item.
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'quantity': int,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'quantity': 'quantity',
            'status': 'status',
        }

        self._id = id
        self._quantity = quantity
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item of this Item.
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Item.


        :return: The id of this Item.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Item.


        :param id: The id of this Item.
        :type id: int
        """

        self._id = id

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Item.


        :return: The quantity of this Item.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Item.


        :param quantity: The quantity of this Item.
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def status(self) -> str:
        """Gets the status of this Item.

        Item Status

        :return: The status of this Item.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Item.

        Item Status

        :param status: The status of this Item.
        :type status: str
        """
        allowed_values = ["placed", "approved", "delivered"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
