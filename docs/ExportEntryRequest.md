# ExportEntryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_reason_id** | **int** | The reason id for this audit event. | [optional] 
**audit_reason_comment** | **str** | The comment for this audit event. | [optional] [default to '']
**part** | **OneOfExportEntryRequestPart** | The part of the document to export. Options include: Image, Text, Edoc. | 
**image_options** | **OneOfExportEntryRequestImageOptions** | The options applied when exporting as Image. | [optional] 
**text_options** | **OneOfExportEntryRequestTextOptions** | The options applied when exporting as Text. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

