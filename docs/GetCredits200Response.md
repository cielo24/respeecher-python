# GetCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** |  | [optional] 
**initial_credits** | **int** |  | [optional] 

## Example

```python
from respeecher.models.get_credits200_response import GetCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredits200Response from a JSON string
get_credits200_response_instance = GetCredits200Response.from_json(json)
# print the JSON string representation of the object
print(GetCredits200Response.to_json())

# convert the object into a dict
get_credits200_response_dict = get_credits200_response_instance.to_dict()
# create an instance of GetCredits200Response from a dict
get_credits200_response_form_dict = get_credits200_response.from_dict(get_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


