# RecordingListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[Recording]**](Recording.md) |  | [optional] 
**pagination** | [**ProjectListResponsePagination**](ProjectListResponsePagination.md) |  | [optional] 

## Example

```python
from respeecher.models.recording_list_response import RecordingListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingListResponse from a JSON string
recording_list_response_instance = RecordingListResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingListResponse.to_json())

# convert the object into a dict
recording_list_response_dict = recording_list_response_instance.to_dict()
# create an instance of RecordingListResponse from a dict
recording_list_response_form_dict = recording_list_response.from_dict(recording_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


