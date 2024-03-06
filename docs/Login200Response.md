# Login200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **object** |  | [optional] 
**csrf_token** | **str** |  | [optional] 
**session_duration** | **int** |  | [optional] 

## Example

```python
from respeecher.models.login200_response import Login200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Login200Response from a JSON string
login200_response_instance = Login200Response.from_json(json)
# print the JSON string representation of the object
print(Login200Response.to_json())

# convert the object into a dict
login200_response_dict = login200_response_instance.to_dict()
# create an instance of Login200Response from a dict
login200_response_form_dict = login200_response.from_dict(login200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


