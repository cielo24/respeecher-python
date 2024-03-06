# FolderStatisticsStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of conversions within the folder. | [optional] 
**completed** | **int** | The number of completed conversions within the folder. | [optional] 
**in_progress** | **int** | The number of conversions currently in progress within the folder. | [optional] 
**failed** | **int** | The number of conversions that failed within the folder. | [optional] 

## Example

```python
from respeecher.models.folder_statistics_stats import FolderStatisticsStats

# TODO update the JSON string below
json = "{}"
# create an instance of FolderStatisticsStats from a JSON string
folder_statistics_stats_instance = FolderStatisticsStats.from_json(json)
# print the JSON string representation of the object
print(FolderStatisticsStats.to_json())

# convert the object into a dict
folder_statistics_stats_dict = folder_statistics_stats_instance.to_dict()
# create an instance of FolderStatisticsStats from a dict
folder_statistics_stats_form_dict = folder_statistics_stats.from_dict(folder_statistics_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


