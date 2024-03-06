# ProjectsStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** |  | [optional] 

## Example

```python
from respeecher.models.projects_statistics_request import ProjectsStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsStatisticsRequest from a JSON string
projects_statistics_request_instance = ProjectsStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsStatisticsRequest.to_json())

# convert the object into a dict
projects_statistics_request_dict = projects_statistics_request_instance.to_dict()
# create an instance of ProjectsStatisticsRequest from a dict
projects_statistics_request_form_dict = projects_statistics_request.from_dict(projects_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


