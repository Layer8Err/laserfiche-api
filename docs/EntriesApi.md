# laserfiche_api.EntriesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_entry**](EntriesApi.md#copy_entry) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Folder/Copy | Copies a new child entry in a folder.
[**create_entry**](EntriesApi.md#create_entry) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Folder/Children | Creates a new child entry in a folder.
[**create_multipart_upload_urls**](EntriesApi.md#create_multipart_upload_urls) | **POST** /v2/Repositories/{repositoryId}/Entries/CreateMultipartUploadUrls | Requests Upload URLs to upload a large file in chunks.
[**delete_electronic_document**](EntriesApi.md#delete_electronic_document) | **DELETE** /v2/Repositories/{repositoryId}/Entries/{entryId}/Document/Edoc | Deletes the edoc associated with an entry.
[**delete_pages**](EntriesApi.md#delete_pages) | **DELETE** /v2/Repositories/{repositoryId}/Entries/{entryId}/Document/Pages | Deletes the pages associated with an entry.
[**export_entry**](EntriesApi.md#export_entry) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Export | Exports an entry.
[**get_entry**](EntriesApi.md#get_entry) | **GET** /v2/Repositories/{repositoryId}/Entries/{entryId} | Returns a single entry object.
[**get_entry_by_path**](EntriesApi.md#get_entry_by_path) | **GET** /v2/Repositories/{repositoryId}/Entries/ByPath | Returns a single entry object using the entry path.
[**import_entry**](EntriesApi.md#import_entry) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Folder/Import | Imports a file into a folder (max length: 100 MB).
[**list_dynamic_field_values**](EntriesApi.md#list_dynamic_field_values) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Fields/GetDynamicFieldLogicValue | Returns the dynamic field logic values assigned to an entry.
[**list_entries**](EntriesApi.md#list_entries) | **GET** /v2/Repositories/{repositoryId}/Entries/{entryId}/Folder/Children | Returns the children entries of a folder.
[**list_fields**](EntriesApi.md#list_fields) | **GET** /v2/Repositories/{repositoryId}/Entries/{entryId}/Fields | Returns the fields assigned to an entry.
[**list_links**](EntriesApi.md#list_links) | **GET** /v2/Repositories/{repositoryId}/Entries/{entryId}/Links | Returns the links assigned to an entry.
[**list_tags**](EntriesApi.md#list_tags) | **GET** /v2/Repositories/{repositoryId}/Entries/{entryId}/Tags | Returns the tags assigned to an entry.
[**remove_template**](EntriesApi.md#remove_template) | **DELETE** /v2/Repositories/{repositoryId}/Entries/{entryId}/Template | Removes the currently assigned template from an entry.
[**set_fields**](EntriesApi.md#set_fields) | **PUT** /v2/Repositories/{repositoryId}/Entries/{entryId}/Fields | Updates the field values assigned to an entry.
[**set_links**](EntriesApi.md#set_links) | **PUT** /v2/Repositories/{repositoryId}/Entries/{entryId}/Links | Assigns links to an entry.
[**set_tags**](EntriesApi.md#set_tags) | **PUT** /v2/Repositories/{repositoryId}/Entries/{entryId}/Tags | Assigns tags to an entry.
[**set_template**](EntriesApi.md#set_template) | **PUT** /v2/Repositories/{repositoryId}/Entries/{entryId}/Template | Assigns a template to an entry.
[**start_copy_entry**](EntriesApi.md#start_copy_entry) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Folder/CopyAsync | Starts an asynchronous copy task to copy an entry into a folder.
[**start_delete_entry**](EntriesApi.md#start_delete_entry) | **DELETE** /v2/Repositories/{repositoryId}/Entries/{entryId} | Starts an asynchronous delete task to delete an entry.
[**start_export_entry**](EntriesApi.md#start_export_entry) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/ExportAsync | Starts an asynchronous export task to export an entry.
[**start_import_uploaded_parts**](EntriesApi.md#start_import_uploaded_parts) | **POST** /v2/Repositories/{repositoryId}/Entries/{entryId}/Folder/ImportUploadedParts | Starts an asynchronous import task to import a document into a folder.
[**update_entry**](EntriesApi.md#update_entry) | **PATCH** /v2/Repositories/{repositoryId}/Entries/{entryId} | Update an entry. (Move and/or Rename)

# **copy_entry**
> Entry copy_entry(body, repository_id, entry_id, culture=culture)

Copies a new child entry in a folder.

- Copy a new child entry in the designated folder. - Provide the parent folder ID, and based on the request body, copy a child entry of the designated folder. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.CopyEntryRequest() # CopyEntryRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The folder ID that the entry will be created in.
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. (optional)

try:
    # Copies a new child entry in a folder.
    api_response = api_instance.copy_entry(body, repository_id, entry_id, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->copy_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyEntryRequest**](CopyEntryRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The folder ID that the entry will be created in. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entry**
> Entry create_entry(body, repository_id, entry_id, culture=culture)

Creates a new child entry in a folder.

- Create a new child entry in the designated folder. - Provide the parent folder ID, and based on the request body, create a folder/shortcut as a child entry of the designated folder. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.CreateEntryRequest() # CreateEntryRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The folder ID that the entry will be created in.
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. (optional)

try:
    # Creates a new child entry in a folder.
    api_response = api_instance.create_entry(body, repository_id, entry_id, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->create_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntryRequest**](CreateEntryRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The folder ID that the entry will be created in. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multipart_upload_urls**
> CreateMultipartUploadUrlsResponse create_multipart_upload_urls(body, repository_id)

Requests Upload URLs to upload a large file in chunks.

- Requests Upload URLs to upload a large file in chunks. - Returns an UploadId and an array of URLs to which the file chunks should be written in the same order. - To request a new batch of Upload URLs for the same file, set the value of UploadId to the one returned when the first batch of Upload URLs was requested. For requesting the first batch of Upload URLs, leave UploadId empty or null. - Example: if a file is going to be uploaded in 10 chunks, the 10 Upload URLs can be retrieved by two successive calls to this api, each call requesting 5 Upload URLs. For this, the first call should have StartingPartNumber=1 and NumberOfParts=5, and the second call should have StartingPartNumber=6 and NumberOfParts=5, along with UploadId returned in the first call. - Each Upload URL expires after 15 minutes. - Each file chunk written to an Upload URL should be at least 5 MB and at most 5 GB. There is no minimum size limit for the last chunk. - The value of NumberOfParts must be in the range [1, 100], meaning that in each call to this api, a maximum of 100 Upload URLs can be requested.  - The total number of Upload URLs for a single file is 1000, which means (StartingPartNumber + NumberOfParts) should be less than or equal to 1001. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.CreateMultipartUploadUrlsRequest() # CreateMultipartUploadUrlsRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.

try:
    # Requests Upload URLs to upload a large file in chunks.
    api_response = api_instance.create_multipart_upload_urls(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->create_multipart_upload_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMultipartUploadUrlsRequest**](CreateMultipartUploadUrlsRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 

### Return type

[**CreateMultipartUploadUrlsResponse**](CreateMultipartUploadUrlsResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_electronic_document**
> Entry delete_electronic_document(repository_id, entry_id)

Deletes the edoc associated with an entry.

- Delete the edoc associated with the provided entry ID. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested document ID.

try:
    # Deletes the edoc associated with an entry.
    api_response = api_instance.delete_electronic_document(repository_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->delete_electronic_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested document ID. | 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages**
> Entry delete_pages(repository_id, entry_id, page_range=page_range)

Deletes the pages associated with an entry.

- Delete the pages associated with the provided entry ID. If no pageRange is specified, all pages will be deleted. - Optional parameter: pageRange (default empty). The value should be a comma-separated string which contains non-overlapping single values, or page ranges. Ex: \"1,2,3\", \"1-3,5\", \"2-7,10-12.\" - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested document ID.
page_range = 'page_range_example' # str | The pages to be deleted. (optional)

try:
    # Deletes the pages associated with an entry.
    api_response = api_instance.delete_pages(repository_id, entry_id, page_range=page_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->delete_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested document ID. | 
 **page_range** | **str**| The pages to be deleted. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_entry**
> ExportEntryResponse export_entry(body, repository_id, entry_id, page_range=page_range)

Exports an entry.

- Export an entry. - The export may time out if it takes longer than 60 seconds. This value is subject to change at anytime. Use the long operation asynchronous export if you run into this restriction. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.ExportEntryRequest() # ExportEntryRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The ID of entry to export.
page_range = 'page_range_example' # str | A comma-separated range of pages to include. Ex: 1,3,4 or 1-3,5-7,9. This value is ignored when exporting as Edoc. (optional)

try:
    # Exports an entry.
    api_response = api_instance.export_entry(body, repository_id, entry_id, page_range=page_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->export_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportEntryRequest**](ExportEntryRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The ID of entry to export. | 
 **page_range** | **str**| A comma-separated range of pages to include. Ex: 1,3,4 or 1-3,5-7,9. This value is ignored when exporting as Edoc. | [optional] 

### Return type

[**ExportEntryResponse**](ExportEntryResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entry**
> Entry get_entry(repository_id, entry_id, select=select)

Returns a single entry object.

- Returns a single entry object. - Provide an entry ID, and get the entry associated with that ID. Useful when detailed information about the entry is required, such as metadata, path information, etc. - If the entry is a subtype (Folder, Document, or Shortcut), the entry will automatically be converted to include those model-specific properties. - Allowed OData query options: Select. - When OData Select query option is used, 'entryType' is always included in the result. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
select = 'select_example' # str | Limits the properties returned in the result. (optional)

try:
    # Returns a single entry object.
    api_response = api_instance.get_entry(repository_id, entry_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **select** | **str**| Limits the properties returned in the result. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entry_by_path**
> GetEntryByPathResponse get_entry_by_path(repository_id, full_path, fallback_to_closest_ancestor=fallback_to_closest_ancestor)

Returns a single entry object using the entry path.

- Returns a single entry object using the entry path. - Optional query parameter: fallbackToClosestAncestor. Use the fallbackToClosestAncestor query parameter to return the closest existing ancestor if the initial entry path is not found. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
full_path = 'full_path_example' # str | The requested entry path.
fallback_to_closest_ancestor = false # bool | An optional query parameter used to indicate whether or not the closest ancestor in the path should be returned if the initial entry path is not found. The default value is false. (optional) (default to false)

try:
    # Returns a single entry object using the entry path.
    api_response = api_instance.get_entry_by_path(repository_id, full_path, fallback_to_closest_ancestor=fallback_to_closest_ancestor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entry_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **full_path** | **str**| The requested entry path. | 
 **fallback_to_closest_ancestor** | **bool**| An optional query parameter used to indicate whether or not the closest ancestor in the path should be returned if the initial entry path is not found. The default value is false. | [optional] [default to false]

### Return type

[**GetEntryByPathResponse**](GetEntryByPathResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_entry**
> Entry import_entry(repository_id, entry_id, file=file, request=request, culture=culture)

Imports a file into a folder (max length: 100 MB).

- Import a new document in the specified folder, and optionally assigns metadata. - The import may fail if the file is greater than 100 MB or time out if it takes longer than 60 seconds. These values are subject to change at anytime. Use the long operation asynchronous import if you run into these restrictions. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The entry ID of the folder that the document will be created in.
file = 'file_example' # str |  (optional)
request = laserfiche_api.ImportEntryRequest() # ImportEntryRequest |  (optional)
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. (optional)

try:
    # Imports a file into a folder (max length: 100 MB).
    api_response = api_instance.import_entry(repository_id, entry_id, file=file, request=request, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->import_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The entry ID of the folder that the document will be created in. | 
 **file** | **str**|  | [optional] 
 **request** | [**ImportEntryRequest**](.md)|  | [optional] 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dynamic_field_values**
> dict(str, list[str]) list_dynamic_field_values(body, repository_id, entry_id)

Returns the dynamic field logic values assigned to an entry.

- Returns dynamic field logic values with the current values of the fields in the template. - Provide an entry ID and field values in the JSON body to get dynamic field logic values. - Independent and non-dynamic fields in the request body will be ignored, and only related dynamic field logic values for the assigned template will be returned. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.ListDynamicFieldValuesRequest() # ListDynamicFieldValuesRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.

try:
    # Returns the dynamic field logic values assigned to an entry.
    api_response = api_instance.list_dynamic_field_values(body, repository_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->list_dynamic_field_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListDynamicFieldValuesRequest**](ListDynamicFieldValuesRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 

### Return type

**dict(str, list[str])**

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entries**
> EntryCollectionResponse list_entries(repository_id, entry_id, group_by_entry_type=group_by_entry_type, fields=fields, format_field_values=format_field_values, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the children entries of a folder.

- Returns the children entries of a folder in the repository. - Provide an entry ID (must be a folder), and get a paged listing of entries in that folder. Used as a way of navigating through the repository. - Entries returned in the listing are not automatically converted to their subtype (Folder, Shortcut, Document), so clients who want model-specific information should request it via the GET entry by ID route. - Optional query parameters: groupByEntryType (bool). This query parameter decides if results are returned in groups based on their entry type.  - Optionally returns field values for the entries in the folder. Each field name needs to be specified in the request. Maximum limit of 10 field names. If field values are requested, only the first value is returned if it is a multi value field. The remaining field values can be retrieved via the GET fields route. Null or Empty field values should not be used to determine if a field is assigned to the entry. - Default page size: 150. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. OData $OrderBy syntax should follow: \"PropertyName direction,PropertyName2 direction\". Sort order can be either value \"asc\" or \"desc\". - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The folder ID.
group_by_entry_type = false # bool | Indicates if the result should be grouped by entry type or not. The default value is false. (optional) (default to false)
fields = ['fields_example'] # list[str] | Optional array of field names. Field values corresponding to the given field names will be returned for each entry. (optional)
format_field_values = false # bool | Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false. (optional) (default to false)
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the children entries of a folder.
    api_response = api_instance.list_entries(repository_id, entry_id, group_by_entry_type=group_by_entry_type, fields=fields, format_field_values=format_field_values, prefer=prefer, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->list_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The folder ID. | 
 **group_by_entry_type** | **bool**| Indicates if the result should be grouped by entry type or not. The default value is false. | [optional] [default to false]
 **fields** | [**list[str]**](str.md)| Optional array of field names. Field values corresponding to the given field names will be returned for each entry. | [optional] 
 **format_field_values** | **bool**| Indicates if field values should be formatted. Only applicable if Fields are specified. The default value is false. | [optional] [default to false]
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
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

# **list_fields**
> FieldCollectionResponse list_fields(repository_id, entry_id, prefer=prefer, format_field_values=format_field_values, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the fields assigned to an entry.

- Returns the fields assigned to an entry. - Provide an entry ID, and get a paged listing of all fields assigned to that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
format_field_values = false # bool | An optional query parameter used to indicate if the field values should be formatted. The default value is false. (optional) (default to false)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the fields assigned to an entry.
    api_response = api_instance.list_fields(repository_id, entry_id, prefer=prefer, format_field_values=format_field_values, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->list_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **format_field_values** | **bool**| An optional query parameter used to indicate if the field values should be formatted. The default value is false. | [optional] [default to false]
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting. The value should be a standard language tag. The formatFieldValues query parameter must be set to true, otherwise culture will not be used for formatting. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**FieldCollectionResponse**](FieldCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_links**
> LinkCollectionResponse list_links(repository_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the links assigned to an entry.

- Returns the links assigned to an entry. - Provide an entry ID, and get a paged listing of links assigned to that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
prefer = 'prefer_example' # str | An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the links assigned to an entry.
    api_response = api_instance.list_links(repository_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->list_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **prefer** | **str**| An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**LinkCollectionResponse**](LinkCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> TagCollectionResponse list_tags(repository_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)

Returns the tags assigned to an entry.

- Returns the tags assigned to an entry. - Provide an entry ID, and get a paged listing of tags assigned to that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Returns the tags assigned to an entry.
    api_response = api_instance.list_tags(repository_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**TagCollectionResponse**](TagCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_template**
> Entry remove_template(repository_id, entry_id)

Removes the currently assigned template from an entry.

- Remove the currently assigned template from the specified entry. - Provide an entry ID to clear template value on. - If the entry does not have a template assigned, no change will be made. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The ID of the entry that will have its template removed.

try:
    # Removes the currently assigned template from an entry.
    api_response = api_instance.remove_template(repository_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->remove_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The ID of the entry that will have its template removed. | 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_fields**
> FieldCollectionResponse set_fields(body, repository_id, entry_id, culture=culture)

Updates the field values assigned to an entry.

- Update the field values assigned to an entry. - Provide the new field values to assign to the entry, and remove/reset all previously assigned field values. - This is an overwrite action. The request body must include all desired field values, including any existing field values that should remain assigned to the entry. Field values that are not included in the request will be deleted from the entry. If the field value that is not included is part of a template, it will still be assigned (as required by the template), but its value will be reset. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.SetFieldsRequest() # SetFieldsRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The entry ID of the entry that will have its fields updated.
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. (optional)

try:
    # Updates the field values assigned to an entry.
    api_response = api_instance.set_fields(body, repository_id, entry_id, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->set_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetFieldsRequest**](SetFieldsRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The entry ID of the entry that will have its fields updated. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. | [optional] 

### Return type

[**FieldCollectionResponse**](FieldCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_links**
> LinkCollectionResponse set_links(body, repository_id, entry_id)

Assigns links to an entry.

- Assign links to an entry. - Provide an entry ID and a list of links to assign to that entry. - This is an overwrite action. The request must include all links to assign to the entry, including existing links that should remain assigned to the entry. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.SetLinksRequest() # SetLinksRequest | The request body.
repository_id = 'repository_id_example' # str | The request repository ID.
entry_id = 56 # int | The requested entry ID.

try:
    # Assigns links to an entry.
    api_response = api_instance.set_links(body, repository_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->set_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetLinksRequest**](SetLinksRequest.md)| The request body. | 
 **repository_id** | **str**| The request repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 

### Return type

[**LinkCollectionResponse**](LinkCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tags**
> TagCollectionResponse set_tags(body, repository_id, entry_id)

Assigns tags to an entry.

- Assign tags to an entry. - Provide an entry ID and a list of tags to assign to that entry. - This is an overwrite action. The request must include all tags to assign to the entry, including existing tags that should remain assigned to the entry. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.SetTagsRequest() # SetTagsRequest | The tags to add.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.

try:
    # Assigns tags to an entry.
    api_response = api_instance.set_tags(body, repository_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->set_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetTagsRequest**](SetTagsRequest.md)| The tags to add. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 

### Return type

[**TagCollectionResponse**](TagCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_template**
> Entry set_template(body, repository_id, entry_id, culture=culture)

Assigns a template to an entry.

- Assign a template to an entry. - Provide an entry ID, template name, and a list of template fields to assign to that entry. - Only template values will be modified. Any existing independent fields on the entry will not be modified, nor will they be added if included in the request. The only modification to fields will only occur on templated fields. If the previously assigned template includes common template fields as the newly assigned template, the common field values will not be modified. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.SetTemplateRequest() # SetTemplateRequest | The template and template fields that will be assigned to the entry.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The ID of entry that will have its template updated.
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. (optional)

try:
    # Assigns a template to an entry.
    api_response = api_instance.set_template(body, repository_id, entry_id, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->set_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetTemplateRequest**](SetTemplateRequest.md)| The template and template fields that will be assigned to the entry. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The ID of entry that will have its template updated. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_copy_entry**
> StartTaskResponse start_copy_entry(body, repository_id, entry_id, culture=culture)

Starts an asynchronous copy task to copy an entry into a folder.

- Copy a new child entry in the designated folder async, and potentially return a taskId. - Provide the parent folder ID, and copy an entry as a child of the designated folder. - The status of the operation can be checked via the Tasks route. - Token substitution in the name of the copied entry is not supported. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.StartCopyEntryRequest() # StartCopyEntryRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The folder ID that the entry will be created in.
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. (optional)

try:
    # Starts an asynchronous copy task to copy an entry into a folder.
    api_response = api_instance.start_copy_entry(body, repository_id, entry_id, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->start_copy_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartCopyEntryRequest**](StartCopyEntryRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The folder ID that the entry will be created in. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. | [optional] 

### Return type

[**StartTaskResponse**](StartTaskResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_delete_entry**
> StartTaskResponse start_delete_entry(repository_id, entry_id, body=body)

Starts an asynchronous delete task to delete an entry.

- Begins a task to delete an entry, and returns a taskId. - Provide an entry ID, and queue a delete task to remove it from the repository (includes nested objects if the entry is a Folder type). The entry will not be deleted immediately. - Optionally include an audit reason ID and comment in the JSON body. This route returns a taskId, and will run as an asynchronous operation. Check the progress via the Tasks route. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
body = laserfiche_api.StartDeleteEntryRequest() # StartDeleteEntryRequest | The submitted audit reason. (optional)

try:
    # Starts an asynchronous delete task to delete an entry.
    api_response = api_instance.start_delete_entry(repository_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->start_delete_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **body** | [**StartDeleteEntryRequest**](StartDeleteEntryRequest.md)| The submitted audit reason. | [optional] 

### Return type

[**StartTaskResponse**](StartTaskResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_export_entry**
> StartTaskResponse start_export_entry(body, repository_id, entry_id, page_range=page_range)

Starts an asynchronous export task to export an entry.

- Starts an asynchronous export operation to export an entry. - If successful, it returns a taskId which can be used to check the status of the export operation or download the export result, otherwise, it returns an error. - Required OAuth scope: repository.Read

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.StartExportEntryRequest() # StartExportEntryRequest | The request body.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The ID of entry to export.
page_range = 'page_range_example' # str | A comma-separated range of pages to include. Ex: 1,3,4 or 1-3,5-7,9. This value is ignored when part=Edoc. (optional)

try:
    # Starts an asynchronous export task to export an entry.
    api_response = api_instance.start_export_entry(body, repository_id, entry_id, page_range=page_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->start_export_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartExportEntryRequest**](StartExportEntryRequest.md)| The request body. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The ID of entry to export. | 
 **page_range** | **str**| A comma-separated range of pages to include. Ex: 1,3,4 or 1-3,5-7,9. This value is ignored when part&#x3D;Edoc. | [optional] 

### Return type

[**StartTaskResponse**](StartTaskResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_uploaded_parts**
> StartTaskResponse start_import_uploaded_parts(repository_id, entry_id, body=body, culture=culture)

Starts an asynchronous import task to import a document into a folder.

- Imports a new file in the specified folder. The file should be already written (in chunks) to the upload URLs obtained by calling the Upload api. The maximum file size allowed is 64 GB. - This route does not support partial success. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The entry ID of the folder that the document will be created in.
body = laserfiche_api.StartImportUploadedPartsRequest() # StartImportUploadedPartsRequest | The request body. (optional)
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. (optional)

try:
    # Starts an asynchronous import task to import a document into a folder.
    api_response = api_instance.start_import_uploaded_parts(repository_id, entry_id, body=body, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->start_import_uploaded_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The entry ID of the folder that the document will be created in. | 
 **body** | [**StartImportUploadedPartsRequest**](StartImportUploadedPartsRequest.md)| The request body. | [optional] 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. This may be used when setting field values with tokens. | [optional] 

### Return type

[**StartTaskResponse**](StartTaskResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entry**
> Entry update_entry(body, repository_id, entry_id, culture=culture)

Update an entry. (Move and/or Rename)

- Update an entry. (Move and/or Rename) - Move an entry to a new folder by setting the ParentId in the request body. - Rename an entry by setting the Name in the request body. - Required OAuth scope: repository.Write

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
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
body = laserfiche_api.UpdateEntryRequest() # UpdateEntryRequest | The request containing the folder ID that the entry will be moved to and the new name the entry will be renamed to.
repository_id = 'repository_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
culture = '' # str | An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. (optional)

try:
    # Update an entry. (Move and/or Rename)
    api_response = api_instance.update_entry(body, repository_id, entry_id, culture=culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->update_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEntryRequest**](UpdateEntryRequest.md)| The request containing the folder ID that the entry will be moved to and the new name the entry will be renamed to. | 
 **repository_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used. The value should be a standard language tag. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

