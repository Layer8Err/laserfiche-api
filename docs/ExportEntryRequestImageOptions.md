# ExportEntryRequestImageOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **OneOfExportEntryRequestImageOptionsFormat** | The image format to export as. Options include: MultiPageTIFF, SinglePageTIFF, PNG, PDF and JPEG. The default value is MultiPageTIFF. MultiPageTIFF format is a single multi-page TIFF file. SinglePageTIFF format is multiple single-page TIFF files (in a single zip file). | [optional] 
**j_peg_compression_level** | **int** | The quality level for JPEG compression when exporting images. The value must be between 0 and 100 (inclusive). The default value is 70. | [optional] [default to 70]
**include_annotations** | **bool** | Indicates if the annotations need to be included. The default value is true. | [optional] [default to True]
**convert_pdf_annotations** | **bool** | Indicates if the annotations on the image need to be converted to PDF annotations when exporting to PDF format. The default value is true. This option is only applicable when exporting to PDF format and IncludeAnnotations is true. | [optional] [default to True]
**page_prefix** | **str** | The page prefix of the individual files, when exporting to multi-file format (e.g.zip). The value must have a length of at most 10 characters and only valid characters that can be included in file names are allowed. The default value is \&quot;, Page \&quot;. | [optional] [default to ', Page ']
**include_redactions** | **bool** | Indicates if redactions are included. The default value is true. | [optional] [default to True]
**watermark** | **OneOfExportEntryRequestImageOptionsWatermark** | The watermark element added to each image. No watermark will be added by default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

