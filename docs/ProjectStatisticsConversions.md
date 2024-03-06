# ProjectStatisticsConversions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of conversions for this project. | [optional] 
**completed** | **int** | The number of completed conversions for this project. | [optional] 
**in_progress** | **int** | The number of conversions currently in progress for this project. | [optional] 
**failed** | **int** | The number of conversions that failed for this project. | [optional] 

## Example

```python
from respeecher.models.project_statistics_conversions import ProjectStatisticsConversions

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatisticsConversions from a JSON string
project_statistics_conversions_instance = ProjectStatisticsConversions.from_json(json)
# print the JSON string representation of the object
print(ProjectStatisticsConversions.to_json())

# convert the object into a dict
project_statistics_conversions_dict = project_statistics_conversions_instance.to_dict()
# create an instance of ProjectStatisticsConversions from a dict
project_statistics_conversions_form_dict = project_statistics_conversions.from_dict(project_statistics_conversions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


