# OrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_id** | **str** | The ID of the original recording to create a conversion from. | [optional] 
**conversions** | [**List[ConversionDetail]**](ConversionDetail.md) |  | [optional] 
**calibration_id** | **str** | The ID of the calibration to use, if applicable. | [optional] 
**use_calibration** | **bool** | Whether to use a specific calibration for the conversion. | [optional] 

## Example

```python
from respeecher.models.order_request import OrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequest from a JSON string
order_request_instance = OrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrderRequest.to_json())

# convert the object into a dict
order_request_dict = order_request_instance.to_dict()
# create an instance of OrderRequest from a dict
order_request_form_dict = order_request.from_dict(order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


