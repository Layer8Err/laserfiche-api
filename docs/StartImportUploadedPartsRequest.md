# StartImportUploadedPartsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | The UploadId received when calling the CreateMultipartUploadUrls API to request upload URLs. | 
**part_e_tags** | **list[str]** | The array of the ETag values received when writing the file chunks into the upload URLs. The ETag values should be in the order of their associated upload URLs, i.e. {eTag received when writing to the first URL}, {eTag received when writing to the second URL}, ... | 
**name** | **str** | The name for the imported entry. | 
**auto_rename** | **bool** | Indicates if the entry should be automatically renamed if an entry already exists with the given name in the folder. The default value is false. | [optional] [default to False]
**pdf_options** | **OneOfStartImportUploadedPartsRequestPdfOptions** | The options applied when importing a PDF. | [optional] 
**import_as_electronic_document** | **bool** | Indicates if the document should be imported as an electronic document (true) or as image pages (false). The default value is false. This option is only applicable when importing the following document types: txt, tif, tiff, bmp, pcx, jpg, jpeg, gif, png. | [optional] [default to False]
**metadata** | **OneOfStartImportUploadedPartsRequestMetadata** | The metadata that will be assigned to the entry. | [optional] 
**volume_name** | **str** | The name of the volume to use. Will use the default parent entry volume if not specified. This is ignored in Laserfiche Cloud. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

