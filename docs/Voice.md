# Voice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**species** | **str** |  | [optional] 
**artist** | **str** |  | [optional] 
**verified_artist** | **bool** |  | [optional] 
**gender** | **str** |  | [optional] 
**pitch** | **float** |  | [optional] 
**age_group** | **str** |  | [optional] 
**pitch_group** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rating** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**favorite** | **bool** |  | [optional] 
**available** | **bool** |  | [optional] 
**accents** | [**List[Accent]**](Accent.md) |  | [optional] 
**narration_styles** | **List[object]** |  | [optional] 
**tiers** | [**List[Tier]**](Tier.md) |  | [optional] 

## Example

```python
from respeecher.models.voice import Voice

# TODO update the JSON string below
json = "{}"
# create an instance of Voice from a JSON string
voice_instance = Voice.from_json(json)
# print the JSON string representation of the object
print(Voice.to_json())

# convert the object into a dict
voice_dict = voice_instance.to_dict()
# create an instance of Voice from a dict
voice_form_dict = voice.from_dict(voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


