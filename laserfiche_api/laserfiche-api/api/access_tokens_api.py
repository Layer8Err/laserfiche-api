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


class AccessTokensApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_access_token(self, repo_id, **kwargs):  # noqa: E501
        """create_access_token  # noqa: E501

        - Creates an access token for use with the Laserfiche API. - Provides credentials and uses the access token returned with subsequent API calls as a means of authorization. - Adding createCookie=true as a query parameter results a response that includes a Set-Cookie header containing an authToken value. The default value for createCookie is false.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_access_token(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param CreateConnectionRequest body: The username and password used to create the session connection.
        :param bool create_cookie: An optional query parameter used to indicate whether a Set-Cookie header containing             the authToken is returned in the response.
        :param str customer_id: The Laserfiche Cloud account ID to use when using username and password to create a session connection.
        :return: SessionKeyInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_access_token_with_http_info(repo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_access_token_with_http_info(repo_id, **kwargs)  # noqa: E501
            return data

    def create_access_token_with_http_info(self, repo_id, **kwargs):  # noqa: E501
        """create_access_token  # noqa: E501

        - Creates an access token for use with the Laserfiche API. - Provides credentials and uses the access token returned with subsequent API calls as a means of authorization. - Adding createCookie=true as a query parameter results a response that includes a Set-Cookie header containing an authToken value. The default value for createCookie is false.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_access_token_with_http_info(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param CreateConnectionRequest body: The username and password used to create the session connection.
        :param bool create_cookie: An optional query parameter used to indicate whether a Set-Cookie header containing             the authToken is returned in the response.
        :param str customer_id: The Laserfiche Cloud account ID to use when using username and password to create a session connection.
        :return: SessionKeyInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'body', 'create_cookie', 'customer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_access_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `create_access_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501

        query_params = []
        if 'create_cookie' in params:
            query_params.append(('createCookie', params['create_cookie']))  # noqa: E501
        if 'customer_id' in params:
            query_params.append(('customerId', params['customer_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1-alpha/Repositories/{repoId}/AccessTokens/Create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SessionKeyInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invalidate_access_token(self, repo_id, **kwargs):  # noqa: E501
        """invalidate_access_token  # noqa: E501

        - Invalidates the access token. - Acts as a \"logout\" operation, and invalidates the session associated with the provided access token. This method should be used when the client wants to clean up the current session.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invalidate_access_token(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :return: ODataValueOfBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.invalidate_access_token_with_http_info(repo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.invalidate_access_token_with_http_info(repo_id, **kwargs)  # noqa: E501
            return data

    def invalidate_access_token_with_http_info(self, repo_id, **kwargs):  # noqa: E501
        """invalidate_access_token  # noqa: E501

        - Invalidates the access token. - Acts as a \"logout\" operation, and invalidates the session associated with the provided access token. This method should be used when the client wants to clean up the current session.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invalidate_access_token_with_http_info(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :return: ODataValueOfBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidate_access_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `invalidate_access_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501

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
            '/v1-alpha/Repositories/{repoId}/AccessTokens/Invalidate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_access_token(self, repo_id, **kwargs):  # noqa: E501
        """refresh_access_token  # noqa: E501

        - Refreshes the session associated with the access token. - When a client application wants to keep an idle session alive, this route should be used to refresh the expiration timer associated with the access token. - Optionally, a Keep-Alive header can be included with the request to specify how long the session should be kept alive when idle. The maximum timeout value is 1 hour.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_access_token(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str keep_alive: An optional Keep-Alive header with timeout value can be used to specify how long the             session should be kept alive when idle. The maximum timeout value is 1 hour.
        :return: ODataValueOfDateTime
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_access_token_with_http_info(repo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_access_token_with_http_info(repo_id, **kwargs)  # noqa: E501
            return data

    def refresh_access_token_with_http_info(self, repo_id, **kwargs):  # noqa: E501
        """refresh_access_token  # noqa: E501

        - Refreshes the session associated with the access token. - When a client application wants to keep an idle session alive, this route should be used to refresh the expiration timer associated with the access token. - Optionally, a Keep-Alive header can be included with the request to specify how long the session should be kept alive when idle. The maximum timeout value is 1 hour.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_access_token_with_http_info(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str keep_alive: An optional Keep-Alive header with timeout value can be used to specify how long the             session should be kept alive when idle. The maximum timeout value is 1 hour.
        :return: ODataValueOfDateTime
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'keep_alive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_access_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `refresh_access_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'keep_alive' in params:
            header_params['Keep-Alive'] = params['keep_alive']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1-alpha/Repositories/{repoId}/AccessTokens/Refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfDateTime',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
