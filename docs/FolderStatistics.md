# FolderStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | The unique identifier of the folder. | [optional] 
**stats** | [**FolderStatisticsStats**](FolderStatisticsStats.md) |  | [optional] 

## Example

```python
from respeecher.models.folder_statistics import FolderStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of FolderStatistics from a JSON string
folder_statistics_instance = FolderStatistics.from_json(json)
# print the JSON string representation of the object
print(FolderStatistics.to_json())

# convert the object into a dict
folder_statistics_dict = folder_statistics_instance.to_dict()
# create an instance of FolderStatistics from a dict
folder_statistics_form_dict = folder_statistics.from_dict(folder_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


