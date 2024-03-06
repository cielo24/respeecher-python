# FoldersStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | **List[str]** |  | [optional] 

## Example

```python
from respeecher.models.folders_statistics_request import FoldersStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersStatisticsRequest from a JSON string
folders_statistics_request_instance = FoldersStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(FoldersStatisticsRequest.to_json())

# convert the object into a dict
folders_statistics_request_dict = folders_statistics_request_instance.to_dict()
# create an instance of FoldersStatisticsRequest from a dict
folders_statistics_request_form_dict = folders_statistics_request.from_dict(folders_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


