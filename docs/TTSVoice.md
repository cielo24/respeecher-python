# TTSVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**f0** | **float** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from respeecher.models.tts_voice import TTSVoice

# TODO update the JSON string below
json = "{}"
# create an instance of TTSVoice from a JSON string
tts_voice_instance = TTSVoice.from_json(json)
# print the JSON string representation of the object
print(TTSVoice.to_json())

# convert the object into a dict
tts_voice_dict = tts_voice_instance.to_dict()
# create an instance of TTSVoice from a dict
tts_voice_form_dict = tts_voice.from_dict(tts_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


