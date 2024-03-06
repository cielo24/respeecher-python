# AccountStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_converted** | [**AccountStatisticsTimeConverted**](AccountStatisticsTimeConverted.md) |  | [optional] 
**conversions** | [**AccountStatisticsConversions**](AccountStatisticsConversions.md) |  | [optional] 
**models** | [**List[AccountStatisticsModelsInner]**](AccountStatisticsModelsInner.md) |  | [optional] 

## Example

```python
from respeecher.models.account_statistics import AccountStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatistics from a JSON string
account_statistics_instance = AccountStatistics.from_json(json)
# print the JSON string representation of the object
print(AccountStatistics.to_json())

# convert the object into a dict
account_statistics_dict = account_statistics_instance.to_dict()
# create an instance of AccountStatistics from a dict
account_statistics_form_dict = account_statistics.from_dict(account_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


