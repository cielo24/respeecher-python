# VoiceSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_id** | **str** |  | [optional] 
**narration_style_id** | **str** |  | [optional] 
**accent_id** | **str** |  | [optional] 
**semitones_correction** | **int** |  | [optional] 

## Example

```python
from respeecher.models.voice_settings_request import VoiceSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceSettingsRequest from a JSON string
voice_settings_request_instance = VoiceSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(VoiceSettingsRequest.to_json())

# convert the object into a dict
voice_settings_request_dict = voice_settings_request_instance.to_dict()
# create an instance of VoiceSettingsRequest from a dict
voice_settings_request_form_dict = voice_settings_request.from_dict(voice_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


