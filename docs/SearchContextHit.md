# SearchContextHit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_type** | **OneOfSearchContextHitHitType** | The type of context hit this instance represents. | [optional] 
**is_annotation_hit** | **bool** | A boolean indicating if this context hit occurs on an annotation. | [optional] 
**annotation_id** | **int** | The ID of the annotation that the context hit is in. | [optional] 
**page_number** | **int** | The page number in the document of the search hit&#x27;s context. | [optional] 
**page_offset** | **int** | The offset from the beginning of the page of the starting character of the search hit&#x27;s context line. | [optional] 
**context** | **str** | The line of context for the search hit. | [optional] 
**highlight1_offset** | **int** | The character offset from the beginning of the context line of the start of the first highlight. | [optional] 
**highlight1_length** | **int** | The length of the first highlight in characters. | [optional] 
**highlight2_offset** | **int** | The character offset from the beginning of the context line of the start of the second highlight. | [optional] 
**highlight2_length** | **int** | The length of the second highlight in characters. | [optional] 
**hit_width** | **int** | The number of words in the context hit. | [optional] 
**edoc_hit_count** | **int** | The number of hits in the electronic document. | [optional] 
**field_hit_count** | **int** | The number of hits in the template. | [optional] 
**field_name** | **str** | The name of a template field containing the hit. | [optional] 
**hit_number** | **int** | The hit number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

