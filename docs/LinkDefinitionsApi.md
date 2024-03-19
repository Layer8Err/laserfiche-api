# laserfiche_api.LinkDefinitionsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_link_definition**](LinkDefinitionsApi.md#get_link_definition) | **GET** /v2/Repositories/{repositoryId}/LinkDefinitions/{linkDefinitionId} | Returns a single link definition object.
[**list_link_definitions**](LinkDefinitionsApi.md#list_link_definitions) | **GET** /v2/Repositories/{repositoryId}/LinkDefinitions | Returns the link definitions associated with a repository.

# **get_link_definition**
> LinkDefinition get_link_definition(repository_id, link_definition_id, select=select)

Returns a single link definition object.

- Returns a single link definition associated with the specified ID. - Provide a link definition ID and get the associated link definition. Useful when a route provides a minimal amount of details and more information about the specific link definition is needed. - Allowed OData query options: Select - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.LinkDefinitionsApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
link_definition_id = 56 # int | The requested link definition ID.
select = 'select_example' # str | Limits the properties returned in the result. (optional)

try:
    # Returns a single link definition object.
    api_response = api_instance.get_link_definition(repository_id, link_definition_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkDefinitionsApi->get_link_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **link_definition_id** | **int**| The requested link definition ID. | 
 **select** | **str**| Limits the properties returned in the result. | [optional] 

### Return type

[**LinkDefinition**](LinkDefinition.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_link_definitions**
> LinkDefinitionCollectionResponse list_link_definitions(repository_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the link definitions associated with a repository.

- Returns the link definitions in the repository. - Provide a repository ID and get a paged listing of link definitions available in the repository. Useful when trying to display all link definitions available, not only links assigned to a specific entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.LinkDefinitionsApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the link definitions associated with a repository.
    api_response = api_instance.list_link_definitions(repository_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkDefinitionsApi->list_link_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**LinkDefinitionCollectionResponse**](LinkDefinitionCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

