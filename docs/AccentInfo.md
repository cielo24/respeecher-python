# AccentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from respeecher.models.accent_info import AccentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccentInfo from a JSON string
accent_info_instance = AccentInfo.from_json(json)
# print the JSON string representation of the object
print(AccentInfo.to_json())

# convert the object into a dict
accent_info_dict = accent_info_instance.to_dict()
# create an instance of AccentInfo from a dict
accent_info_form_dict = accent_info.from_dict(accent_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


