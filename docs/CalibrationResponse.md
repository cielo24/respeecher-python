# CalibrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**f0** | **int** |  | [optional] 
**algorithm** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**calibrated_at** | **datetime** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from respeecher.models.calibration_response import CalibrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalibrationResponse from a JSON string
calibration_response_instance = CalibrationResponse.from_json(json)
# print the JSON string representation of the object
print(CalibrationResponse.to_json())

# convert the object into a dict
calibration_response_dict = calibration_response_instance.to_dict()
# create an instance of CalibrationResponse from a dict
calibration_response_form_dict = calibration_response.from_dict(calibration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


