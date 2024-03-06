# AccountStatisticsModelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**conversions_count** | **int** |  | [optional] 
**converted_time** | **int** |  | [optional] 

## Example

```python
from respeecher.models.account_statistics_models_inner import AccountStatisticsModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatisticsModelsInner from a JSON string
account_statistics_models_inner_instance = AccountStatisticsModelsInner.from_json(json)
# print the JSON string representation of the object
print(AccountStatisticsModelsInner.to_json())

# convert the object into a dict
account_statistics_models_inner_dict = account_statistics_models_inner_instance.to_dict()
# create an instance of AccountStatisticsModelsInner from a dict
account_statistics_models_inner_form_dict = account_statistics_models_inner.from_dict(account_statistics_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


