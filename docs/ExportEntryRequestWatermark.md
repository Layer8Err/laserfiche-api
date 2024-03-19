# ExportEntryRequestWatermark

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text of the watermark. The value must be a string with a length of at most 100 characters and must not be all whitespace characters. | [optional] [default to '']
**position** | **OneOfExportEntryRequestWatermarkPosition** | The position of the watermark. The default value is DeadCenter. | [optional] 
**rotation_angle** | **int** | The rotation angle of the watermark. The value must be between 0 and 360 (inclusive). The default value is 0. | [optional] [default to 0]
**page_span_percentage** | **int** | The percentage of the page that the watermark spans on. The value must be between 1 and 100 (inclusive). The default value is 50. | [optional] [default to 50]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

