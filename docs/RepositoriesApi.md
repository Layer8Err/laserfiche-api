# laserfiche_api.RepositoriesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_repositories**](RepositoriesApi.md#list_repositories) | **GET** /v2/Repositories | Returns the list of repositories accessible to the user.

# **list_repositories**
> RepositoryCollectionResponse list_repositories()

Returns the list of repositories accessible to the user.

- Returns the repository resource list that current user has access to. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.RepositoriesApi(laserfiche_api.ApiClient(configuration))

try:
    # Returns the list of repositories accessible to the user.
    api_response = api_instance.list_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->list_repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RepositoryCollectionResponse**](RepositoryCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

