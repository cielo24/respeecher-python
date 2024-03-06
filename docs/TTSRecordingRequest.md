# TTSRecordingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_folder_id** | **str** | The ID of the parent folder. | [optional] 
**text** | **str** | The text to be converted to speech. | [optional] 
**tts_voice_id** | **str** | The ID of the TTS voice to be used. | [optional] 
**label** | **str** | A label for the request. (Optional) | [optional] 

## Example

```python
from respeecher.models.tts_recording_request import TTSRecordingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TTSRecordingRequest from a JSON string
tts_recording_request_instance = TTSRecordingRequest.from_json(json)
# print the JSON string representation of the object
print(TTSRecordingRequest.to_json())

# convert the object into a dict
tts_recording_request_dict = tts_recording_request_instance.to_dict()
# create an instance of TTSRecordingRequest from a dict
tts_recording_request_form_dict = tts_recording_request.from_dict(tts_recording_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


