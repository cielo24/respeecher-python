# ProjectStatisticsTimeConverted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total time converted for this project. | [optional] 
**current_month** | **int** | The total time converted for this project in the current month. | [optional] 

## Example

```python
from respeecher.models.project_statistics_time_converted import ProjectStatisticsTimeConverted

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatisticsTimeConverted from a JSON string
project_statistics_time_converted_instance = ProjectStatisticsTimeConverted.from_json(json)
# print the JSON string representation of the object
print(ProjectStatisticsTimeConverted.to_json())

# convert the object into a dict
project_statistics_time_converted_dict = project_statistics_time_converted_instance.to_dict()
# create an instance of ProjectStatisticsTimeConverted from a dict
project_statistics_time_converted_form_dict = project_statistics_time_converted.from_dict(project_statistics_time_converted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


