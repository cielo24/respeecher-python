# FolderListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[Folder]**](Folder.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from respeecher.models.folder_list_response import FolderListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolderListResponse from a JSON string
folder_list_response_instance = FolderListResponse.from_json(json)
# print the JSON string representation of the object
print(FolderListResponse.to_json())

# convert the object into a dict
folder_list_response_dict = folder_list_response_instance.to_dict()
# create an instance of FolderListResponse from a dict
folder_list_response_form_dict = folder_list_response.from_dict(folder_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


