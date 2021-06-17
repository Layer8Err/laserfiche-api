# coding: utf-8

"""
    Laserfiche API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>561590</p>  # noqa: E501

    OpenAPI spec version: 1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import laserfiche-api
from laserfiche-api.api.attributes_api import AttributesApi  # noqa: E501
from laserfiche-api.rest import ApiException


class TestAttributesApi(unittest.TestCase):
    """AttributesApi unit test stubs"""

    def setUp(self):
        self.api = AttributesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_trustee_attribute_key_value_pairs(self):
        """Test case for get_trustee_attribute_key_value_pairs

        Get the attribute key value pairs associated with the authenticated user.  # noqa: E501
        """
        pass

    def test_get_trustee_attribute_value_by_key(self):
        """Test case for get_trustee_attribute_value_by_key

        Get an attribute object by key associated with the authenticated user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
