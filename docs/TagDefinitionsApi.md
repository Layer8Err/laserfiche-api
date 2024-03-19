# laserfiche_api.TagDefinitionsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_definition**](TagDefinitionsApi.md#get_tag_definition) | **GET** /v2/Repositories/{repositoryId}/TagDefinitions/{tagId} | Returns a single tag definition object.
[**list_tag_definitions**](TagDefinitionsApi.md#list_tag_definitions) | **GET** /v2/Repositories/{repositoryId}/TagDefinitions | Returns the tag definitions associated with a repository.

# **get_tag_definition**
> TagDefinition get_tag_definition(repository_id, tag_id, culture=culture, select=select)

Returns a single tag definition object.

- Returns a single tag definition. - Provide a tag definition ID, and get the single tag definition associated with that ID. Useful when another route provides a minimal amount of details, and more information about the specific tag is needed. - Allowed OData query options: Select - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.TagDefinitionsApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
tag_id = 56 # int | The requested tag definition ID.
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)

try:
    # Returns a single tag definition object.
    api_response = api_instance.get_tag_definition(repository_id, tag_id, culture=culture, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagDefinitionsApi->get_tag_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **tag_id** | **int**| The requested tag definition ID. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 

### Return type

[**TagDefinition**](TagDefinition.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tag_definitions**
> TagDefinitionCollectionResponse list_tag_definitions(repository_id, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the tag definitions associated with a repository.

- Returns all tag definitions in the repository. - Provide a repository ID and get a paged listing of tag definitions available in the repository. Useful when trying to display all tag definitions available, not only tags assigned to a specific entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.TagDefinitionsApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the tag definitions associated with a repository.
    api_response = api_instance.list_tag_definitions(repository_id, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagDefinitionsApi->list_tag_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**TagDefinitionCollectionResponse**](TagDefinitionCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

