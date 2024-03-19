# CreateMultipartUploadUrlsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | A unique identifier for the whole upload process. | [optional] [default to '']
**starting_part_number** | **int** | Determines the starting position of the requested parts among all the parts associated with this upload. The default value is 1. | [optional] [default to 1]
**number_of_parts** | **int** | The value must be in the range [1, 100], meaning that in each call to the CreateMultipartUploadUrls api, a maximum of 100 Upload URLs can be requested. Further, each file chunk written to an Upload URL should be at least 5 MB. There is no minimum size limit for the last chunk. | 
**file_name** | **str** | The name of the file to be uploaded. The file extension in the name will be used as the extension of the imported entry. | [optional] 
**mime_type** | **str** | The mime-type of the file to be uploaded. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

