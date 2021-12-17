# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.item import Item  # noqa: E501
from swagger_server.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_add_item(self):
        """Test case for add_item

        Add a new item to the store
        """
        body = Item()
        response = self.client.open(
            '/v2/item',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_item(self):
        """Test case for get_item

        Returns Item info
        """
        response = self.client.open(
            '/v2/item/{itemId}'.format(itemId=10),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_item(self):
        """Test case for update_item

        Update an existing item
        """
        body = Item()
        response = self.client.open(
            '/v2/item',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
    
    def test_delete_item(self):
        """Test case for delete_item

        Delete item by ID
        """
        response = self.client.open(
            '/v2/item'.format(itemId=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
