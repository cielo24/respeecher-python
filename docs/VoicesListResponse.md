# VoicesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[Voice]**](Voice.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from respeecher.models.voices_list_response import VoicesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoicesListResponse from a JSON string
voices_list_response_instance = VoicesListResponse.from_json(json)
# print the JSON string representation of the object
print(VoicesListResponse.to_json())

# convert the object into a dict
voices_list_response_dict = voices_list_response_instance.to_dict()
# create an instance of VoicesListResponse from a dict
voices_list_response_form_dict = voices_list_response.from_dict(voices_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


