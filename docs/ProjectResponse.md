# ProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**models** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_recording_at** | **datetime** |  | [optional] 

## Example

```python
from respeecher.models.project_response import ProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponse from a JSON string
project_response_instance = ProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectResponse.to_json())

# convert the object into a dict
project_response_dict = project_response_instance.to_dict()
# create an instance of ProjectResponse from a dict
project_response_form_dict = project_response.from_dict(project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


