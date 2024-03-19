# TaskProgress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The task ID of the task associated with this TaskProgress. | [optional] 
**task_type** | **OneOfTaskProgressTaskType** | The type of the task associated with this TaskProgress. | [optional] 
**percent_complete** | **int** | Determines what percentage of the execution of the associated task is completed. | [optional] 
**status** | **OneOfTaskProgressStatus** | The status of the task associated with this TaskProgress. | [optional] 
**errors** | [**list[ProblemDetails]**](ProblemDetails.md) | The list of errors occurred during the execution of the associated task. | [optional] 
**result** | **OneOfTaskProgressResult** | The result of the execution of the associated task. | [optional] 
**start_time** | **datetime** | The time representing when the associated task&#x27;s execution started. | [optional] 
**last_update_time** | **datetime** | The time representing when the associated task&#x27;s status last changed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

