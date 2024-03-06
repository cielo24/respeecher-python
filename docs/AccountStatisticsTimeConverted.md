# AccountStatisticsTimeConverted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current_month** | **int** |  | [optional] 
**previous_monthes** | [**List[AccountStatisticsTimeConvertedPreviousMonthesInner]**](AccountStatisticsTimeConvertedPreviousMonthesInner.md) |  | [optional] 

## Example

```python
from respeecher.models.account_statistics_time_converted import AccountStatisticsTimeConverted

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatisticsTimeConverted from a JSON string
account_statistics_time_converted_instance = AccountStatisticsTimeConverted.from_json(json)
# print the JSON string representation of the object
print(AccountStatisticsTimeConverted.to_json())

# convert the object into a dict
account_statistics_time_converted_dict = account_statistics_time_converted_instance.to_dict()
# create an instance of AccountStatisticsTimeConverted from a dict
account_statistics_time_converted_form_dict = account_statistics_time_converted.from_dict(account_statistics_time_converted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


