# Field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | [optional] 
**field_type** | **OneOfFieldFieldType** | The type of the field. The possible field types are listed below. | [optional] 
**id** | **int** | The ID of the field. | [optional] 
**is_multi_value** | **bool** | A boolean indicating if the represented field supports multiple values. | [optional] 
**is_required** | **bool** | A boolean indicating if the represented field must have a value set on entries assigned to a template that the field is a member of. | [optional] 
**has_more_values** | **bool** | A boolean indicating if there are more field values. | [optional] 
**group_id** | **int** | The group id of the multi value field group. If the field is not a part of a multi value field group, then there is no group id. | [optional] 
**values** | **list[str]** | The values assigned to the field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

