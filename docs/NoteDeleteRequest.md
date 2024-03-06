# NoteDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_id** | **str** |  | [optional] 

## Example

```python
from respeecher.models.note_delete_request import NoteDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NoteDeleteRequest from a JSON string
note_delete_request_instance = NoteDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NoteDeleteRequest.to_json())

# convert the object into a dict
note_delete_request_dict = note_delete_request_instance.to_dict()
# create an instance of NoteDeleteRequest from a dict
note_delete_request_form_dict = note_delete_request.from_dict(note_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


