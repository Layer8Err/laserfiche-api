# laserfiche_api.AttributesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attribute**](AttributesApi.md#get_attribute) | **GET** /v2/Repositories/{repositoryId}/Attributes/{attributeKey} | Returns an attribute object associated with the authenticated user.
[**list_attributes**](AttributesApi.md#list_attributes) | **GET** /v2/Repositories/{repositoryId}/Attributes | Returns the attribute key value pairs associated with the authenticated user.

# **get_attribute**
> Attribute get_attribute(repository_id, attribute_key, everyone=everyone)

Returns an attribute object associated with the authenticated user.

- Returns the attribute associated with the key. Alternatively, return the attribute associated with the key within \"Everyone\" group. - Optional query parameters: everyone (bool, default false). When true, the server only searches for the attribute value with the given key upon the authenticated users attributes. If false, only the authenticated users attributes will be queried. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.AttributesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
attribute_key = 'attribute_key_example' # str | The requested attribute key.
everyone = false # bool | Indicates if attributes associated with the \"Everyone\" group or the currently authenticated user is returned. The default value is false. (optional) (default to false)

try:
    # Returns an attribute object associated with the authenticated user.
    api_response = api_instance.get_attribute(repository_id, attribute_key, everyone=everyone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **attribute_key** | **str**| The requested attribute key. | 
 **everyone** | **bool**| Indicates if attributes associated with the \&quot;Everyone\&quot; group or the currently authenticated user is returned. The default value is false. | [optional] [default to false]

### Return type

[**Attribute**](Attribute.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attributes**
> AttributeCollectionResponse list_attributes(repository_id, everyone=everyone, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the attribute key value pairs associated with the authenticated user.

- Returns the attribute key value pairs associated with the authenticated user. Alternatively, return only the attribute key value pairs that are associated with the \"Everyone\" group. - Attribute keys can be used with subsequent calls to get specific attribute values. - Optional query parameters: everyone (bool, default false). When true, this route does not return the attributes that are tied to the currently authenticated user, but rather the attributes assigned to the \"Everyone\" group. Note when this is true, the response does not include both the \"Everyone\" groups attribute and the currently authenticated user, but only the \"Everyone\" groups. - Default page size: 100. Allowed OData query options: Select, Count, OrderBy, Skip, Top, SkipToken, Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.AttributesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
everyone = false # bool | Indicates if attributes associated with the \"Everyone\" group or the currently authenticated user is returned. The default value is false. (optional) (default to false)
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the attribute key value pairs associated with the authenticated user.
    api_response = api_instance.list_attributes(repository_id, everyone=everyone, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->list_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **everyone** | **bool**| Indicates if attributes associated with the \&quot;Everyone\&quot; group or the currently authenticated user is returned. The default value is false. | [optional] [default to false]
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**AttributeCollectionResponse**](AttributeCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

