# coding: utf-8

"""
    Laserfiche Repository API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p>Visit the changelog for the list of changes: <a href=\"/repository/v2/changelog\">/repository/v2/changelog</a></p><p><strong>Build# : </strong>41a7347c0662989661d7ab8105a70d36cb42518e_.20240124.4</p>  # noqa: E501

    OpenAPI spec version: 2
    
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

    def search_entry(self, body, repository_id, **kwargs):  # noqa: E501
        """Runs a \"simple\" search operation.  # noqa: E501

        - Runs a \"simple\" search operation on the repository. - Returns a truncated search result listing. - Search result listing may be truncated, depending on number of results. Additionally, searches may time out if they take too long. Use the other search route to run full searches. - For datetime search criteria that relate to time zone like CreateDate and ModifiedDate, the value should be in UTC time. - Optionally returns field values for the entries in the folder. Each field name needs to be specified in the request. Maximum limit of 10 field names. If field values are requested, only the first value is returned if it is a multi value field. The remaining field values can be retrieved via the GET fields route. Null or Empty field values should not be used to determine if a field is assigned to the entry. - When OData Select query option is used, 'entryType' is always included in the result. - Required OAuth scope: repository.Read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_entry(body, repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchEntryRequest body: The Laserfiche search command to run. (required)
        :param str repository_id: The requested repository ID. (required)
        :param list[str] fields: Optional array of field names. Field values corresponding to the given field names will be returned for each search result. 
        :param bool format_field_values: Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false.
        :param str culture: An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: EntryCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_entry_with_http_info(body, repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.search_entry_with_http_info(body, repository_id, **kwargs)  # noqa: E501
            return data

    def search_entry_with_http_info(self, body, repository_id, **kwargs):  # noqa: E501
        """Runs a \"simple\" search operation.  # noqa: E501

        - Runs a \"simple\" search operation on the repository. - Returns a truncated search result listing. - Search result listing may be truncated, depending on number of results. Additionally, searches may time out if they take too long. Use the other search route to run full searches. - For datetime search criteria that relate to time zone like CreateDate and ModifiedDate, the value should be in UTC time. - Optionally returns field values for the entries in the folder. Each field name needs to be specified in the request. Maximum limit of 10 field names. If field values are requested, only the first value is returned if it is a multi value field. The remaining field values can be retrieved via the GET fields route. Null or Empty field values should not be used to determine if a field is assigned to the entry. - When OData Select query option is used, 'entryType' is always included in the result. - Required OAuth scope: repository.Read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_entry_with_http_info(body, repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchEntryRequest body: The Laserfiche search command to run. (required)
        :param str repository_id: The requested repository ID. (required)
        :param list[str] fields: Optional array of field names. Field values corresponding to the given field names will be returned for each search result. 
        :param bool format_field_values: Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false.
        :param str culture: An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: EntryCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'repository_id', 'fields', 'format_field_values', 'culture', 'select', 'orderby', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `search_entry`")  # noqa: E501
        # verify the required parameter 'repository_id' is set
        if ('repository_id' not in params or
                params['repository_id'] is None):
            raise ValueError("Missing the required parameter `repository_id` when calling `search_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryId'] = params['repository_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'format_field_values' in params:
            query_params.append(('formatFieldValues', params['format_field_values']))  # noqa: E501
        if 'culture' in params:
            query_params.append(('culture', params['culture']))  # noqa: E501
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('$orderby', params['orderby']))  # noqa: E501
        if 'count' in params:
            query_params.append(('$count', params['count']))  # noqa: E501

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
        auth_settings = ['Authorization', 'OAuth2 Authorization Code Flow']  # noqa: E501

        return self.api_client.call_api(
            '/v2/Repositories/{repositoryId}/SimpleSearches', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntryCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
