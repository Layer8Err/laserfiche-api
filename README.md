# laserfiche-api
Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>561590</p>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1-alpha
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import laserfiche-api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import laserfiche-api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.AccessTokensApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
body = laserfiche-api.CreateConnectionRequest() # CreateConnectionRequest | The username and password used to create the session connection. (optional)
create_cookie = true # bool | An optional query parameter used to indicate whether a Set-Cookie header containing             the authToken is returned in the response. (optional)
customer_id = 'customer_id_example' # str | The Laserfiche Cloud account ID to use when using username and password to create a session connection. (optional)

try:
    api_response = api_instance.create_access_token(repo_id, body=body, create_cookie=create_cookie, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)


# create an instance of the API class
api_instance = laserfiche-api.AccessTokensApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.

try:
    api_response = api_instance.invalidate_access_token(repo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->invalidate_access_token: %s\n" % e)


# create an instance of the API class
api_instance = laserfiche-api.AccessTokensApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
keep_alive = 'keep_alive_example' # str | An optional Keep-Alive header with timeout value can be used to specify how long the             session should be kept alive when idle. The maximum timeout value is 1 hour. (optional)

try:
    api_response = api_instance.refresh_access_token(repo_id, keep_alive=keep_alive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->refresh_access_token: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.laserfiche.com/repository*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessTokensApi* | [**create_access_token**](docs/AccessTokensApi.md#create_access_token) | **POST** /v1-alpha/Repositories/{repoId}/AccessTokens/Create | 
*AccessTokensApi* | [**invalidate_access_token**](docs/AccessTokensApi.md#invalidate_access_token) | **POST** /v1-alpha/Repositories/{repoId}/AccessTokens/Invalidate | 
*AccessTokensApi* | [**refresh_access_token**](docs/AccessTokensApi.md#refresh_access_token) | **POST** /v1-alpha/Repositories/{repoId}/AccessTokens/Refresh | 
*AttributesApi* | [**get_trustee_attribute_key_value_pairs**](docs/AttributesApi.md#get_trustee_attribute_key_value_pairs) | **GET** /v1-alpha/Repositories/{repoId}/Attributes | Get the attribute key value pairs associated with the authenticated user.
*AttributesApi* | [**get_trustee_attribute_value_by_key**](docs/AttributesApi.md#get_trustee_attribute_value_by_key) | **GET** /v1-alpha/Repositories/{repoId}/Attributes/{attributeKey} | Get an attribute object by key associated with the authenticated user.
*AuditReasonsApi* | [**get_audit_reasons**](docs/AuditReasonsApi.md#get_audit_reasons) | **GET** /v1-alpha/Repositories/{repoId}/AuditReasons | Get the audit reasons associated with the authenticated user.
*EntriesApi* | [**assign_entry_links**](docs/EntriesApi.md#assign_entry_links) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/links | 
*EntriesApi* | [**assign_field_values**](docs/EntriesApi.md#assign_field_values) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/fields | 
*EntriesApi* | [**assign_tags**](docs/EntriesApi.md#assign_tags) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/tags | 
*EntriesApi* | [**copy_entry_async**](docs/EntriesApi.md#copy_entry_async) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Folder/CopyAsync | 
*EntriesApi* | [**create_or_copy_entry**](docs/EntriesApi.md#create_or_copy_entry) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Folder/children | 
*EntriesApi* | [**delete_assigned_template**](docs/EntriesApi.md#delete_assigned_template) | **DELETE** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/template | 
*EntriesApi* | [**delete_entry_info**](docs/EntriesApi.md#delete_entry_info) | **DELETE** /v1-alpha/Repositories/{repoId}/Entries/{entryId} | 
*EntriesApi* | [**export_document**](docs/EntriesApi.md#export_document) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Document/edoc | 
*EntriesApi* | [**export_document_with_audit_reason**](docs/EntriesApi.md#export_document_with_audit_reason) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Document/GetEdocWithAuditReason | 
*EntriesApi* | [**get_document_content_type**](docs/EntriesApi.md#get_document_content_type) | **HEAD** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Document/edoc | 
*EntriesApi* | [**get_dynamic_field_values**](docs/EntriesApi.md#get_dynamic_field_values) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/fields/GetDynamicFieldLogicValue | 
*EntriesApi* | [**get_entry**](docs/EntriesApi.md#get_entry) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId} | 
*EntriesApi* | [**get_entry_listing**](docs/EntriesApi.md#get_entry_listing) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Folder/children | 
*EntriesApi* | [**get_field_values**](docs/EntriesApi.md#get_field_values) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/fields | 
*EntriesApi* | [**get_link_values_from_entry**](docs/EntriesApi.md#get_link_values_from_entry) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/links | 
*EntriesApi* | [**get_tags_assigned_to_entry**](docs/EntriesApi.md#get_tags_assigned_to_entry) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/tags | 
*EntriesApi* | [**import_document**](docs/EntriesApi.md#import_document) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{parentEntryId}/{fileName} | 
*EntriesApi* | [**move_or_rename_document**](docs/EntriesApi.md#move_or_rename_document) | **PATCH** /v1-alpha/Repositories/{repoId}/Entries/{entryId} | 
*EntriesApi* | [**write_template_value_to_entry**](docs/EntriesApi.md#write_template_value_to_entry) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/template | 
*FieldDefinitionsApi* | [**get_field_definition_by_id**](docs/FieldDefinitionsApi.md#get_field_definition_by_id) | **GET** /v1-alpha/Repositories/{repoId}/FieldDefinitions/{fieldDefinitionId} | 
*FieldDefinitionsApi* | [**get_field_definitions**](docs/FieldDefinitionsApi.md#get_field_definitions) | **GET** /v1-alpha/Repositories/{repoId}/FieldDefinitions | 
*SearchesApi* | [**cancel_or_close_a_search**](docs/SearchesApi.md#cancel_or_close_a_search) | **DELETE** /v1-alpha/Repositories/{repoId}/Searches/{searchToken} | Cancel or close an advanced search.
*SearchesApi* | [**create_search_operation**](docs/SearchesApi.md#create_search_operation) | **POST** /v1-alpha/Repositories/{repoId}/Searches | Run a search in the specified repository.
*SearchesApi* | [**get_search_context_hits**](docs/SearchesApi.md#get_search_context_hits) | **GET** /v1-alpha/Repositories/{repoId}/Searches/{searchToken}/Results/{rowNumber}/ContextHits | 
*SearchesApi* | [**get_search_results**](docs/SearchesApi.md#get_search_results) | **GET** /v1-alpha/Repositories/{repoId}/Searches/{searchToken}/Results | Get the search results listing of a search.
*SearchesApi* | [**get_search_status**](docs/SearchesApi.md#get_search_status) | **GET** /v1-alpha/Repositories/{repoId}/Searches/{searchToken} | Get the status of a search using a token.
*SimpleSearchesApi* | [**create_simple_search_operation**](docs/SimpleSearchesApi.md#create_simple_search_operation) | **POST** /v1-alpha/Repositories/{repoId}/SimpleSearches | 
*TagDefinitionsApi* | [**get_tag_definition_by_id**](docs/TagDefinitionsApi.md#get_tag_definition_by_id) | **GET** /v1-alpha/Repositories/{repoId}/TagDefinitions/{tagId} | 
*TagDefinitionsApi* | [**get_tag_definitions**](docs/TagDefinitionsApi.md#get_tag_definitions) | **GET** /v1-alpha/Repositories/{repoId}/TagDefinitions | 
*TasksApi* | [**cancel_operation**](docs/TasksApi.md#cancel_operation) | **DELETE** /v1-alpha/Repositories/{repoId}/Tasks/{operationToken} | 
*TasksApi* | [**get_operation_status_and_progress**](docs/TasksApi.md#get_operation_status_and_progress) | **GET** /v1-alpha/Repositories/{repoId}/Tasks/{operationToken} | 
*TemplateDefinitionsApi* | [**get_template_definition_by_id**](docs/TemplateDefinitionsApi.md#get_template_definition_by_id) | **GET** /v1-alpha/Repositories/{repoId}/TemplateDefinitions/{templateId} | 
*TemplateDefinitionsApi* | [**get_template_definitions**](docs/TemplateDefinitionsApi.md#get_template_definitions) | **GET** /v1-alpha/Repositories/{repoId}/TemplateDefinitions | 
*TemplateDefinitionsApi* | [**get_template_field_definitions**](docs/TemplateDefinitionsApi.md#get_template_field_definitions) | **GET** /v1-alpha/Repositories/{repoId}/TemplateDefinitions/{templateId}/fields | 

## Documentation For Models

 - [APIServerException](docs/APIServerException.md)
 - [AcceptedOperation](docs/AcceptedOperation.md)
 - [AdvancedSearchRequest](docs/AdvancedSearchRequest.md)
 - [Attribute](docs/Attribute.md)
 - [AuditReasons](docs/AuditReasons.md)
 - [ContextHit](docs/ContextHit.md)
 - [CopyAsyncRequest](docs/CopyAsyncRequest.md)
 - [CreateConnectionRequest](docs/CreateConnectionRequest.md)
 - [CreateEntryOperations](docs/CreateEntryOperations.md)
 - [CreateEntryResult](docs/CreateEntryResult.md)
 - [DeleteEntryWithAuditReason](docs/DeleteEntryWithAuditReason.md)
 - [Document](docs/Document.md)
 - [Edoc](docs/Edoc.md)
 - [Entry](docs/Entry.md)
 - [EntryCreate](docs/EntryCreate.md)
 - [EntryType](docs/EntryType.md)
 - [FieldToUpdate](docs/FieldToUpdate.md)
 - [FieldValue](docs/FieldValue.md)
 - [Folder](docs/Folder.md)
 - [FuzzyType](docs/FuzzyType.md)
 - [GetDynamicFieldLogicValueRequest](docs/GetDynamicFieldLogicValueRequest.md)
 - [GetEdocWithAuditReasonRequest](docs/GetEdocWithAuditReasonRequest.md)
 - [HitType](docs/HitType.md)
 - [LFColor](docs/LFColor.md)
 - [LinkToUpdate](docs/LinkToUpdate.md)
 - [ODataActionParameters](docs/ODataActionParameters.md)
 - [ODataValueOfBoolean](docs/ODataValueOfBoolean.md)
 - [ODataValueOfDateTime](docs/ODataValueOfDateTime.md)
 - [ODataValueOfIListOfContextHit](docs/ODataValueOfIListOfContextHit.md)
 - [ODataValueOfIListOfEntry](docs/ODataValueOfIListOfEntry.md)
 - [ODataValueOfIListOfFieldValue](docs/ODataValueOfIListOfFieldValue.md)
 - [ODataValueOfIListOfTemplateFieldInfo](docs/ODataValueOfIListOfTemplateFieldInfo.md)
 - [ODataValueOfIListOfWEntryLinkInfo](docs/ODataValueOfIListOfWEntryLinkInfo.md)
 - [ODataValueOfIListOfWFieldInfo](docs/ODataValueOfIListOfWFieldInfo.md)
 - [ODataValueOfIListOfWTagInfo](docs/ODataValueOfIListOfWTagInfo.md)
 - [ODataValueOfIListOfWTemplateInfo](docs/ODataValueOfIListOfWTemplateInfo.md)
 - [ODataValueOfListOfAttribute](docs/ODataValueOfListOfAttribute.md)
 - [OneOfAdvancedSearchRequestFuzzyType](docs/OneOfAdvancedSearchRequestFuzzyType.md)
 - [OneOfEntryEntryType](docs/OneOfEntryEntryType.md)
 - [OneOfFieldValueFieldType](docs/OneOfFieldValueFieldType.md)
 - [OneOfPostEntryChildrenRequestEntryType](docs/OneOfPostEntryChildrenRequestEntryType.md)
 - [OneOfWFieldInfoFieldType](docs/OneOfWFieldInfoFieldType.md)
 - [OneOfWFieldInfoFormat](docs/OneOfWFieldInfoFormat.md)
 - [OneOfWTagInfoWatermark](docs/OneOfWTagInfoWatermark.md)
 - [OneOfWTemplateInfoColor](docs/OneOfWTemplateInfoColor.md)
 - [OneOfWatermarkWatermarkPosition](docs/OneOfWatermarkWatermarkPosition.md)
 - [OperationErrorItem](docs/OperationErrorItem.md)
 - [OperationProgress](docs/OperationProgress.md)
 - [OperationStatus](docs/OperationStatus.md)
 - [ParentEntryIdFileNameBody](docs/ParentEntryIdFileNameBody.md)
 - [PatchEntryRequest](docs/PatchEntryRequest.md)
 - [PostEntryChildrenRequest](docs/PostEntryChildrenRequest.md)
 - [PostEntryWithEdocMetadataRequest](docs/PostEntryWithEdocMetadataRequest.md)
 - [PutFieldValsRequest](docs/PutFieldValsRequest.md)
 - [PutLinksRequest](docs/PutLinksRequest.md)
 - [PutTagRequest](docs/PutTagRequest.md)
 - [PutTemplateRequest](docs/PutTemplateRequest.md)
 - [Rule](docs/Rule.md)
 - [SessionKeyInfo](docs/SessionKeyInfo.md)
 - [SetEdoc](docs/SetEdoc.md)
 - [SetFields](docs/SetFields.md)
 - [SetLinks](docs/SetLinks.md)
 - [SetTags](docs/SetTags.md)
 - [SetTemplate](docs/SetTemplate.md)
 - [Shortcut](docs/Shortcut.md)
 - [SimpleSearchRequest](docs/SimpleSearchRequest.md)
 - [TemplateFieldInfo](docs/TemplateFieldInfo.md)
 - [ValueToUpdate](docs/ValueToUpdate.md)
 - [WAuditReason](docs/WAuditReason.md)
 - [WEntryLinkInfo](docs/WEntryLinkInfo.md)
 - [WFieldFormat](docs/WFieldFormat.md)
 - [WFieldInfo](docs/WFieldInfo.md)
 - [WFieldType](docs/WFieldType.md)
 - [WTagInfo](docs/WTagInfo.md)
 - [WTemplateInfo](docs/WTemplateInfo.md)
 - [Watermark](docs/Watermark.md)
 - [WatermarkPosition](docs/WatermarkPosition.md)

## Documentation For Authorization


## Authorization



## Author


