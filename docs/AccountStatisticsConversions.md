# AccountStatisticsConversions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**completed** | **int** |  | [optional] 
**in_progress** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 

## Example

```python
from respeecher.models.account_statistics_conversions import AccountStatisticsConversions

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatisticsConversions from a JSON string
account_statistics_conversions_instance = AccountStatisticsConversions.from_json(json)
# print the JSON string representation of the object
print(AccountStatisticsConversions.to_json())

# convert the object into a dict
account_statistics_conversions_dict = account_statistics_conversions_instance.to_dict()
# create an instance of AccountStatisticsConversions from a dict
account_statistics_conversions_form_dict = account_statistics_conversions.from_dict(account_statistics_conversions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


