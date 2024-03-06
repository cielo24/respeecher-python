# UpdateRecordingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | New label for the recording | [optional] 
**starred** | **bool** | Mark the recording as starred or not | [optional] 

## Example

```python
from respeecher.models.update_recording_request import UpdateRecordingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordingRequest from a JSON string
update_recording_request_instance = UpdateRecordingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordingRequest.to_json())

# convert the object into a dict
update_recording_request_dict = update_recording_request_instance.to_dict()
# create an instance of UpdateRecordingRequest from a dict
update_recording_request_form_dict = update_recording_request.from_dict(update_recording_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


