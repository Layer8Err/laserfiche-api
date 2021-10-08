# coding: utf-8

"""
    Laserfiche API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>650780</p>  # noqa: E501

    OpenAPI spec version: 1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from laserfiche_api.api_client import ApiClient


class SimpleSearchesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_simple_search_operation(self, repo_id, **kwargs):  # noqa: E501
        """create_simple_search_operation  # noqa: E501

        - Runs a \"simple\" search operation on the repository. - Returns a truncated search result listing. - Search result listing may be truncated, depending on number of results. Additionally, searches may time out if they take too long. Use the other search route to run full searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_simple_search_operation(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param SimpleSearchRequest body: The Laserfiche search command to run.
        :return: ODataValueOfIListOfEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_simple_search_operation_with_http_info(repo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_simple_search_operation_with_http_info(repo_id, **kwargs)  # noqa: E501
            return data

    def create_simple_search_operation_with_http_info(self, repo_id, **kwargs):  # noqa: E501
        """create_simple_search_operation  # noqa: E501

        - Runs a \"simple\" search operation on the repository. - Returns a truncated search result listing. - Search result listing may be truncated, depending on number of results. Additionally, searches may time out if they take too long. Use the other search route to run full searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_simple_search_operation_with_http_info(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param SimpleSearchRequest body: The Laserfiche search command to run.
        :return: ODataValueOfIListOfEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_simple_search_operation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `create_simple_search_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501

        query_params = []

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
            '/v1-alpha/Repositories/{repoId}/SimpleSearches', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIListOfEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
