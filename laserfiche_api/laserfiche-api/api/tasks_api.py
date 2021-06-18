# coding: utf-8

"""
    Laserfiche API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>561590</p>  # noqa: E501

    OpenAPI spec version: 1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from laserfiche-api.api_client import ApiClient


class TasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_operation(self, repo_id, operation_token, **kwargs):  # noqa: E501
        """cancel_operation  # noqa: E501

        - Cancels an operation. - Provide an operationToken to cancel the operation, if possible. Should be used if an operation was created in error, or is no longer necessary. - Rollbacks must be done manually. For example, if a copy operation is started and is halfway complete when canceled, the client application is responsible for cleaning up the files that were successfully copied before the operation was canceled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_operation(repo_id, operation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str operation_token: The operation token  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_operation_with_http_info(repo_id, operation_token, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_operation_with_http_info(repo_id, operation_token, **kwargs)  # noqa: E501
            return data

    def cancel_operation_with_http_info(self, repo_id, operation_token, **kwargs):  # noqa: E501
        """cancel_operation  # noqa: E501

        - Cancels an operation. - Provide an operationToken to cancel the operation, if possible. Should be used if an operation was created in error, or is no longer necessary. - Rollbacks must be done manually. For example, if a copy operation is started and is halfway complete when canceled, the client application is responsible for cleaning up the files that were successfully copied before the operation was canceled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_operation_with_http_info(repo_id, operation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str operation_token: The operation token  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'operation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_operation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `cancel_operation`")  # noqa: E501
        # verify the required parameter 'operation_token' is set
        if ('operation_token' not in params or
                params['operation_token'] is None):
            raise ValueError("Missing the required parameter `operation_token` when calling `cancel_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501
        if 'operation_token' in params:
            path_params['operationToken'] = params['operation_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1-alpha/Repositories/{repoId}/Tasks/{operationToken}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_operation_status_and_progress(self, repo_id, operation_token, **kwargs):  # noqa: E501
        """get_operation_status_and_progress  # noqa: E501

        - Returns the status of an operation. - Provide an operationToken (returned in other asynchronous routes) to get the operation status, progress, and any errors that may have occurred. When the operation is completed, the Location header can be inspected as a link to the modified resources (if relevant). - OperationStatus can be one of the following values: NotStarted, InProgress, Completed, or Failed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_status_and_progress(repo_id, operation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str operation_token: The operation token. (required)
        :return: OperationProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_operation_status_and_progress_with_http_info(repo_id, operation_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_operation_status_and_progress_with_http_info(repo_id, operation_token, **kwargs)  # noqa: E501
            return data

    def get_operation_status_and_progress_with_http_info(self, repo_id, operation_token, **kwargs):  # noqa: E501
        """get_operation_status_and_progress  # noqa: E501

        - Returns the status of an operation. - Provide an operationToken (returned in other asynchronous routes) to get the operation status, progress, and any errors that may have occurred. When the operation is completed, the Location header can be inspected as a link to the modified resources (if relevant). - OperationStatus can be one of the following values: NotStarted, InProgress, Completed, or Failed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_status_and_progress_with_http_info(repo_id, operation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str operation_token: The operation token. (required)
        :return: OperationProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'operation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operation_status_and_progress" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `get_operation_status_and_progress`")  # noqa: E501
        # verify the required parameter 'operation_token' is set
        if ('operation_token' not in params or
                params['operation_token'] is None):
            raise ValueError("Missing the required parameter `operation_token` when calling `get_operation_status_and_progress`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501
        if 'operation_token' in params:
            path_params['operationToken'] = params['operation_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1-alpha/Repositories/{repoId}/Tasks/{operationToken}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationProgress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
