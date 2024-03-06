# RecordingModeration

Moderation status or information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The moderation state of the recording. | [optional] 
**error** | **str** | Any error message associated with the moderation. | [optional] 
**language** | **str** | The language of the recording. | [optional] 
**has_violations** | **bool** | Indicates if the recording has violations. | [optional] 

## Example

```python
from respeecher.models.recording_moderation import RecordingModeration

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingModeration from a JSON string
recording_moderation_instance = RecordingModeration.from_json(json)
# print the JSON string representation of the object
print(RecordingModeration.to_json())

# convert the object into a dict
recording_moderation_dict = recording_moderation_instance.to_dict()
# create an instance of RecordingModeration from a dict
recording_moderation_form_dict = recording_moderation.from_dict(recording_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


