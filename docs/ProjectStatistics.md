# ProjectStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The unique identifier for the project. | [optional] 
**time_converted** | [**ProjectStatisticsTimeConverted**](ProjectStatisticsTimeConverted.md) |  | [optional] 
**conversions** | [**ProjectStatisticsConversions**](ProjectStatisticsConversions.md) |  | [optional] 

## Example

```python
from respeecher.models.project_statistics import ProjectStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatistics from a JSON string
project_statistics_instance = ProjectStatistics.from_json(json)
# print the JSON string representation of the object
print(ProjectStatistics.to_json())

# convert the object into a dict
project_statistics_dict = project_statistics_instance.to_dict()
# create an instance of ProjectStatistics from a dict
project_statistics_form_dict = project_statistics.from_dict(project_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


