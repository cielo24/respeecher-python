# GenerateApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Expiration date and time of the API key in ISO 8601 format. | [optional] 

## Example

```python
from respeecher.models.generate_api_key_request import GenerateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateApiKeyRequest from a JSON string
generate_api_key_request_instance = GenerateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateApiKeyRequest.to_json())

# convert the object into a dict
generate_api_key_request_dict = generate_api_key_request_instance.to_dict()
# create an instance of GenerateApiKeyRequest from a dict
generate_api_key_request_form_dict = generate_api_key_request.from_dict(generate_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


