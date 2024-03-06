# ConversionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_id** | **str** | The ID of the voice to use for the conversion. | [optional] 
**narration_style_id** | **str** | The ID of the narration style to use, if applicable. | [optional] 
**accent_id** | **str** | The ID of the accent to use, if applicable. | [optional] 
**semitones_correction** | **int** | The number of semitones to shift the converted output to. | [optional] 
**label** | **str** | A label to identify the conversion. | [optional] 

## Example

```python
from respeecher.models.conversion_detail import ConversionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionDetail from a JSON string
conversion_detail_instance = ConversionDetail.from_json(json)
# print the JSON string representation of the object
print(ConversionDetail.to_json())

# convert the object into a dict
conversion_detail_dict = conversion_detail_instance.to_dict()
# create an instance of ConversionDetail from a dict
conversion_detail_form_dict = conversion_detail.from_dict(conversion_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


