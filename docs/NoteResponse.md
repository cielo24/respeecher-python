# NoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_id** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from respeecher.models.note_response import NoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteResponse from a JSON string
note_response_instance = NoteResponse.from_json(json)
# print the JSON string representation of the object
print(NoteResponse.to_json())

# convert the object into a dict
note_response_dict = note_response_instance.to_dict()
# create an instance of NoteResponse from a dict
note_response_form_dict = note_response.from_dict(note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


