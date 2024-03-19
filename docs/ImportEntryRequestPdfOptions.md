# ImportEntryRequestPdfOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generate_text** | **bool** | Indicates if the import operation should generate text. The default value is false. | [optional] [default to False]
**generate_pages** | **bool** | Indicates if the import operation should generate image pages. The default value is false. | [optional] [default to False]
**generate_pages_image_type** | **OneOfImportEntryRequestPdfOptionsGeneratePagesImageType** | The image type used when generating image pages. The default value is StandardColor. This option is only applicable when GeneratePages is true. | [optional] 
**keep_pdf_after_import** | **bool** | Indicates if the PDF file should be retained as an electronic document after generating image pages. The default value is true. This option is only applicable when GeneratePages is true. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

