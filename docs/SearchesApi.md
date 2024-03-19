# laserfiche_api.SearchesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_search_context_hits**](SearchesApi.md#list_search_context_hits) | **GET** /v2/Repositories/{repositoryId}/Searches/{taskId}/Results/{rowNumber}/ContextHits | Returns the context hits associated with a search result entry.
[**list_search_results**](SearchesApi.md#list_search_results) | **GET** /v2/Repositories/{repositoryId}/Searches/{taskId}/Results | Returns the results listing associated with a search task.
[**start_search_entry**](SearchesApi.md#start_search_entry) | **POST** /v2/Repositories/{repositoryId}/Searches/SearchAsync | Starts an asynchronous search task.

# **list_search_context_hits**
> SearchContextHitCollectionResponse list_search_context_hits(repository_id, task_id, row_number, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the context hits associated with a search result entry.

- Returns the context hits associated with a search result entry. - Given a taskId, and rowNumber associated with a search entry in the listing, return the context hits for that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2 Authorization Code Flow
configuration = laserfiche_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = laserfiche_api.SearchesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
task_id = 'task_id_example' # str | The requested task ID.
row_number = 56 # int | The search result listing row number to get context hits for.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the context hits associated with a search result entry.
    api_response = api_instance.list_search_context_hits(repository_id, task_id, row_number, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->list_search_context_hits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **task_id** | **str**| The requested task ID. | 
 **row_number** | **int**| The search result listing row number to get context hits for. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**SearchContextHitCollectionResponse**](SearchContextHitCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_search_results**
> EntryCollectionResponse list_search_results(repository_id, task_id, group_by_entry_type=group_by_entry_type, refresh=refresh, fields=fields, format_field_values=format_field_values, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the results listing associated with a search task.

- Returns a search result listing if the search is completed. - Search results expire after 5 minutes, but can be refreshed by retrieving the results again. - Optional query parameter: groupByOrderType (default false). This query parameter decides whether or not results are returned in groups based on their entry type. - Optional query parameter: refresh (default false). If the search listing should be refreshed to show updated values. - Optionally returns field values for the entries in the folder. Each field name needs to be specified in the request. Maximum limit of 10 field names. If field values are requested, only the first value is returned if it is a multi value field. The remaining field values can be retrieved via the GET fields route. Null or Empty field values should not be used to determine if a field is assigned to the entry. - Default page size: 150. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. OData $OrderBy syntax should follow: \"PropertyName direction,PropertyName2 direction\". sort order can be either \"asc\" or \"desc\". - When OData Select query option is used, 'entryType' is always included in the result. - Required OAuth scope: repository.Read

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2 Authorization Code Flow
configuration = laserfiche_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = laserfiche_api.SearchesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
task_id = 'task_id_example' # str | The requested task ID.
group_by_entry_type = false # bool | Indicates if the result should be grouped by entry type or not. The default value is false. (optional) (default to false)
refresh = false # bool | Indicates if the search listing should be refreshed to show updated values. The default value is false. (optional) (default to false)
fields = ['fields_example'] # list[str] | Optional array of field names. Field values corresponding to the given field names will be returned for each search result.  (optional)
format_field_values = false # bool | Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false. (optional) (default to false)
prefer = 'prefer_example' # str | An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the results listing associated with a search task.
    api_response = api_instance.list_search_results(repository_id, task_id, group_by_entry_type=group_by_entry_type, refresh=refresh, fields=fields, format_field_values=format_field_values, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->list_search_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **task_id** | **str**| The requested task ID. | 
 **group_by_entry_type** | **bool**| Indicates if the result should be grouped by entry type or not. The default value is false. | [optional] [default to false]
 **refresh** | **bool**| Indicates if the search listing should be refreshed to show updated values. The default value is false. | [optional] [default to false]
 **fields** | [**list[str]**](str.md)| Optional array of field names. Field values corresponding to the given field names will be returned for each search result.  | [optional] 
 **format_field_values** | **bool**| Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false. | [optional] [default to false]
 **prefer** | **str**| An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**EntryCollectionResponse**](EntryCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_search_entry**
> StartTaskResponse start_search_entry(body, repository_id)

Starts an asynchronous search task.

- Runs a search operation on the repository. - The status for search operations must be checked via the Tasks route. - For datetime search criteria that relate to time zone like CreateDate and ModifiedDate, the value should be in UTC time. - Optional body parameters: FuzzyType: (default none), which can be used to determine what is considered a match by number of letters or percentage. FuzzyFactor: integer value that determines the degree to which a search will be considered a match (integer value for NumberOfLetters, or int value representing a percentage). - Required OAuth scope: repository.Read

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2 Authorization Code Flow
configuration = laserfiche_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = laserfiche_api.SearchesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.StartSearchEntryRequest() # StartSearchEntryRequest | The Laserfiche search command to run, optionally include fuzzy search settings.
repository_id = 'repository_id_example' # str | The requested repository ID.

try:
    # Starts an asynchronous search task.
    api_response = api_instance.start_search_entry(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->start_search_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartSearchEntryRequest**](StartSearchEntryRequest.md)| The Laserfiche search command to run, optionally include fuzzy search settings. | 
 **repository_id** | **str**| The requested repository ID. | 

### Return type

[**StartTaskResponse**](StartTaskResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

