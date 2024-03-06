# FolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from respeecher.models.folder_request import FolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FolderRequest from a JSON string
folder_request_instance = FolderRequest.from_json(json)
# print the JSON string representation of the object
print(FolderRequest.to_json())

# convert the object into a dict
folder_request_dict = folder_request_instance.to_dict()
# create an instance of FolderRequest from a dict
folder_request_form_dict = folder_request.from_dict(folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


