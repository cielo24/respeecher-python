# Recording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the recording. | [optional] 
**project_id** | **str** | The project identifier this recording belongs to. | [optional] 
**parent_folder_id** | **str** | The folder identifier in which this recording is stored. | [optional] 
**type** | **str** | The type of recording. | [optional] 
**url** | **str** | The URL to access the recording. | [optional] 
**waveform_url** | **str** | The URL to access the waveform of the recording. | [optional] 
**file_name** | **str** | The name of the recording file. | [optional] 
**label** | **str** | A label for the recording. | [optional] 
**state** | **str** | The state of the recording. | [optional] 
**original_id** | **str** | Identifier for the original recording. | [optional] 
**model_id** | **str** | The model identifier used for the recording. | [optional] 
**model_name** | **str** | The name of the model used. | [optional] 
**voice_id** | **str** | The voice identifier used for the recording. | [optional] 
**voice_name** | **str** | The name of the voice used. | [optional] 
**accent_id** | **str** | The accent identifier used for the recording. | [optional] 
**accent_name** | **str** | The name of the accent used. | [optional] 
**narration_style_id** | **str** | The narration style identifier used for the recording. | [optional] 
**narration_style_name** | **str** | The name of the narration style used. | [optional] 
**semitones_correction** | **float** | Semitones correction applied to the recording. | [optional] 
**calibration_id** | **str** | The calibration identifier used for the recording. | [optional] 
**calibration_value** | **str** | The calibration value used. | [optional] 
**calibration_name** | **str** | The name of the calibration used. | [optional] 
**microphone** | **str** | The microphone used for the recording. | [optional] 
**size** | **int** | The size of the recording file in bytes. | [optional] 
**duration** | **float** | The duration of the recording in seconds. | [optional] 
**starred** | **bool** | Indicates if the recording is marked as favorite. | [optional] 
**tts** | **bool** | Indicates if the recording is synthesized from text. | [optional] 
**tts_voice** | **str** | The TTS voice used for the recording. | [optional] 
**tts_voice_id** | **str** | The TTS voice identifier used for the recording. | [optional] 
**text** | **str** | The text content of the TTS recording. | [optional] 
**params** | **Dict[str, object]** | Additional parameters for the recording. | [optional] 
**error** | **str** | Any error message associated with the recording. | [optional] 
**active** | **bool** | Indicates if the recording is active. | [optional] 
**created_at** | **datetime** | The creation date and time of the recording. | [optional] 
**converted_at** | **datetime** | The date and time when the recording was converted. | [optional] 
**listen_count** | **int** | The number of times the recording has been played. | [optional] 
**process_stage** | **str** | The current processing stage of the recording. | [optional] 
**note** | **str** | An optional note about the recording. | [optional] 
**transaction_id** | **str** | The transaction identifier associated with the recording. | [optional] 
**moderation** | [**RecordingModeration**](RecordingModeration.md) |  | [optional] 

## Example

```python
from respeecher.models.recording import Recording

# TODO update the JSON string below
json = "{}"
# create an instance of Recording from a JSON string
recording_instance = Recording.from_json(json)
# print the JSON string representation of the object
print(Recording.to_json())

# convert the object into a dict
recording_dict = recording_instance.to_dict()
# create an instance of Recording from a dict
recording_form_dict = recording.from_dict(recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

