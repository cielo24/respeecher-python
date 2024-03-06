# FavoriteVoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite** | **bool** |  | [optional] 

## Example

```python
from respeecher.models.favorite_voice_request import FavoriteVoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteVoiceRequest from a JSON string
favorite_voice_request_instance = FavoriteVoiceRequest.from_json(json)
# print the JSON string representation of the object
print(FavoriteVoiceRequest.to_json())

# convert the object into a dict
favorite_voice_request_dict = favorite_voice_request_instance.to_dict()
# create an instance of FavoriteVoiceRequest from a dict
favorite_voice_request_form_dict = favorite_voice_request.from_dict(favorite_voice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


