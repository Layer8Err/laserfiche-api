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
from laserfiche-api.api.tasks_api import TasksApi  # noqa: E501
from laserfiche-api.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_operation(self):
        """Test case for cancel_operation

        """
        pass

    def test_get_operation_status_and_progress(self):
        """Test case for get_operation_status_and_progress

        """
        pass


if __name__ == '__main__':
    unittest.main()
