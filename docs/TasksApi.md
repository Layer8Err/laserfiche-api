# laserfiche_api.TasksApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_tasks**](TasksApi.md#cancel_tasks) | **DELETE** /v2/Repositories/{repositoryId}/Tasks | Starts the cancellation for a set of one or more tasks.
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /v2/Repositories/{repositoryId}/Tasks | Returns the status of a set of one or more tasks.

# **cancel_tasks**
> CancelTasksResponse cancel_tasks(repository_id, task_ids=task_ids)

Starts the cancellation for a set of one or more tasks.

- Starts the cancellation for a set of one or more tasks. - Provide comma-separated list of task IDs to cancel. Should be used if an operation was created in error, or is no longer necessary. - Check the status of the task to determine if the task has been cancelled successfully. - Leave the taskIds query parameter empty, to cancel the list of all the task IDs associated with the current access token. - Rollbacks must be done manually. For example, if a copy operation is started and is halfway complete when canceled, the client application is responsible for cleaning up the files that were successfully copied before the operation was canceled. - Required OAuth scope: None

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
api_instance = laserfiche_api.TasksApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID
task_ids = ['task_ids_example'] # list[str] | An array of task IDs. Leave this parameter empty to cancel the list of all the tasks associated with the current access token. (optional)

try:
    # Starts the cancellation for a set of one or more tasks.
    api_response = api_instance.cancel_tasks(repository_id, task_ids=task_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->cancel_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID | 
 **task_ids** | [**list[str]**](str.md)| An array of task IDs. Leave this parameter empty to cancel the list of all the tasks associated with the current access token. | [optional] 

### Return type

[**CancelTasksResponse**](CancelTasksResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> TaskCollectionResponse list_tasks(repository_id, task_ids=task_ids)

Returns the status of a set of one or more tasks.

- Returns the status of a set of one or more tasks. - Provide a comma-separated list of task IDs to get the task status, progress, and any errors that may have occurred. - Leave the taskIds query parameter empty, to get the list of all the task IDs associated with the current access token. - TaskStatus can be one of the following values: NotStarted, InProgress, Completed, Cancelled, or Failed. - This API employs long polling technique and could return the result immediately (e.g. if the export operation is failed or completed successfully) or after at most 60 seconds. - Required OAuth scope: None

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
api_instance = laserfiche_api.TasksApi(laserfiche_api.ApiClient(configuration))
repository_id = 'repository_id_example' # str | The requested repository ID
task_ids = ['task_ids_example'] # list[str] | An array of task IDs. Leave this parameter empty to get the list of all the tasks associated with the current access token. (optional)

try:
    # Returns the status of a set of one or more tasks.
    api_response = api_instance.list_tasks(repository_id, task_ids=task_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The requested repository ID | 
 **task_ids** | [**list[str]**](str.md)| An array of task IDs. Leave this parameter empty to get the list of all the tasks associated with the current access token. | [optional] 

### Return type

[**TaskCollectionResponse**](TaskCollectionResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [OAuth2 Authorization Code Flow](../README.md#OAuth2 Authorization Code Flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

