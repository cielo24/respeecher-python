# ProjectListResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from respeecher.models.project_list_response_pagination import ProjectListResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListResponsePagination from a JSON string
project_list_response_pagination_instance = ProjectListResponsePagination.from_json(json)
# print the JSON string representation of the object
print(ProjectListResponsePagination.to_json())

# convert the object into a dict
project_list_response_pagination_dict = project_list_response_pagination_instance.to_dict()
# create an instance of ProjectListResponsePagination from a dict
project_list_response_pagination_form_dict = project_list_response_pagination.from_dict(project_list_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


