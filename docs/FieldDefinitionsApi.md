# laserfiche_api.FieldDefinitionsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_field_definition**](FieldDefinitionsApi.md#get_field_definition) | **GET** /v2/Repositories/{repositoryId}/FieldDefinitions/{fieldId} | Returns a single field definition object.
[**list_field_definitions**](FieldDefinitionsApi.md#list_field_definitions) | **GET** /v2/Repositories/{repositoryId}/FieldDefinitions | Returns the paged listing of the field definitions available in a repository.

# **get_field_definition**
> FieldDefinition get_field_definition(repository_id, field_id, culture=culture, select=select)

Returns a single field definition object.

- Returns a single field definition associated with the specified ID.  - Useful when a route provides a minimal amount of details and more information about the specific field definition is needed. - Allowed OData query options: Select - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.FieldDefinitionsApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
field_id = 56 # int | The requested field definition ID.
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)

try:
    # Returns a single field definition object.
    api_response = api_instance.get_field_definition(repository_id, field_id, culture=culture, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldDefinitionsApi->get_field_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **field_id** | **int**| The requested field definition ID. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 

### Return type

[**FieldDefinition**](FieldDefinition.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_field_definitions**
> FieldDefinitionCollectionResponse list_field_definitions(repository_id, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the paged listing of the field definitions available in a repository.

- Returns a paged listing of field definitions available in the specified repository. - Useful when trying to find a list of all field definitions available, rather than only those assigned to a specific entry/template. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.FieldDefinitionsApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the paged listing of the field definitions available in a repository.
    api_response = api_instance.list_field_definitions(repository_id, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldDefinitionsApi->list_field_definitions: %s\n" % e)
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

[**FieldDefinitionCollectionResponse**](FieldDefinitionCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

