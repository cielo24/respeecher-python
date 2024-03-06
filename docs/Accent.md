# Accent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**native** | **bool** |  | [optional] 
**info** | [**AccentInfo**](AccentInfo.md) |  | [optional] 
**tiers** | [**List[Tier]**](Tier.md) |  | [optional] 
**available** | **bool** |  | [optional] 
**settings** | **object** |  | [optional] 

## Example

```python
from respeecher.models.accent import Accent

# TODO update the JSON string below
json = "{}"
# create an instance of Accent from a JSON string
accent_instance = Accent.from_json(json)
# print the JSON string representation of the object
print(Accent.to_json())

# convert the object into a dict
accent_dict = accent_instance.to_dict()
# create an instance of Accent from a dict
accent_form_dict = accent.from_dict(accent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


