# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the conversion order. | [optional] 
**user_id** | **str** | The user identifier associated with the order. | [optional] 
**original_id** | **str** | Identifier for the original recording or file. | [optional] 
**conversion_id** | **str** | Identifier for the conversion operation. | [optional] 
**transaction_id** | **str** | Transaction identifier associated with the order (if applicable). | [optional] 
**moderation_id** | **str** | Moderation identifier associated with the order (if applicable). | [optional] 
**calibration_id** | **str** | Calibration identifier used in the conversion process (if applicable). | [optional] 
**tracking_id** | **str** | Tracking identifier for the order. | [optional] 
**f0** | **float** | Fundamental frequency adjustment applied to the conversion (if any). | [optional] 
**state** | **str** | The current state of the conversion order. | [optional] 
**created_at** | **datetime** | Timestamp when the order was created. | [optional] 
**closed_at** | **datetime** | Timestamp when the order was closed (if applicable). | [optional] 
**error** | **str** | Error message related to the order (if any). | [optional] 

## Example

```python
from respeecher.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_form_dict = order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


