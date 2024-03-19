# CreateEntryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entry. | 
**auto_rename** | **bool** | Indicates if the entry should be automatically renamed if an entry already exists with the given name in the folder. The default value is false. | [optional] [default to False]
**entry_type** | **OneOfCreateEntryRequestEntryType** | The type of the entry. | 
**target_id** | **int** | The TargetId is only needed for creating a shortcut. This will be the entry ID of the shortcut target. | [optional] 
**volume_name** | **str** | The name of the volume to use. Will use the default parent entry volume if not specified. This is ignored in Laserfiche Cloud. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

