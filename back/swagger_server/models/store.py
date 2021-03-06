# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Store(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, status: str=None):
        """Store - a model defined in Swagger

        :param id: The id of this Store.
        :type id: int
        :param status: The status of this Store.
        :type status: str
        :param complete: The complete of this Store.
        :type complete: bool
        """
        self.swagger_types = {
            'id': int,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status'
        }

        self._id = id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Store':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Store of this Store.
        :rtype: Store
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Store.


        :return: The id of this Store.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Store.


        :param id: The id of this Store.
        :type id: int
        """

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this Store.

        Store Status

        :return: The status of this Store.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Store.

        Store Status

        :param status: The status of this Store.
        :type status: str
        """
        allowed_values = ["placed", "approved", "delivered"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
