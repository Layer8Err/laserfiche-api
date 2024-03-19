# laserfiche_api.SimpleSearchesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_entry**](SimpleSearchesApi.md#search_entry) | **POST** /v2/Repositories/{repositoryId}/SimpleSearches | Runs a \&quot;simple\&quot; search operation.

# **search_entry**
> EntryCollectionResponse search_entry(body, repository_id, fields=fields, format_field_values=format_field_values, culture=culture, select=select, orderby=orderby, count=count)

Runs a \"simple\" search operation.

- Runs a \"simple\" search operation on the repository. - Returns a truncated search result listing. - Search result listing may be truncated, depending on number of results. Additionally, searches may time out if they take too long. Use the other search route to run full searches. - For datetime search criteria that relate to time zone like CreateDate and ModifiedDate, the value should be in UTC time. - Optionally returns field values for the entries in the folder. Each field name needs to be specified in the request. Maximum limit of 10 field names. If field values are requested, only the first value is returned if it is a multi value field. The remaining field values can be retrieved via the GET fields route. Null or Empty field values should not be used to determine if a field is assigned to the entry. - When OData Select query option is used, 'entryType' is always included in the result. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.SimpleSearchesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.SearchEntryRequest() # SearchEntryRequest | The Laserfiche search command to run.
repository_id = 'repository_id_example' # str | The requested repository ID.
fields = ['fields_example'] # list[str] | Optional array of field names. Field values corresponding to the given field names will be returned for each search result.  (optional)
format_field_values = false # bool | Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false. (optional) (default to false)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Runs a \"simple\" search operation.
    api_response = api_instance.search_entry(body, repository_id, fields=fields, format_field_values=format_field_values, culture=culture, select=select, orderby=orderby, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleSearchesApi->search_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchEntryRequest**](SearchEntryRequest.md)| The Laserfiche search command to run. | 
 **repository_id** | **str**| The requested repository ID. | 
 **fields** | [**list[str]**](str.md)| Optional array of field names. Field values corresponding to the given field names will be returned for each search result.  | [optional] 
 **format_field_values** | **bool**| Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false. | [optional] [default to false]
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**EntryCollectionResponse**](EntryCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

