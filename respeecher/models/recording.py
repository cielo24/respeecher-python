# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from respeecher.models.recording_moderation import RecordingModeration
from typing import Optional, Set
from typing_extensions import Self

class Recording(BaseModel):
    """
    Recording
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the recording.")
    project_id: Optional[StrictStr] = Field(default=None, description="The project identifier this recording belongs to.")
    parent_folder_id: Optional[StrictStr] = Field(default=None, description="The folder identifier in which this recording is stored.")
    type: Optional[StrictStr] = Field(default=None, description="The type of recording.")
    url: Optional[StrictStr] = Field(default=None, description="The URL to access the recording.")
    waveform_url: Optional[StrictStr] = Field(default=None, description="The URL to access the waveform of the recording.")
    file_name: Optional[StrictStr] = Field(default=None, description="The name of the recording file.")
    label: Optional[StrictStr] = Field(default=None, description="A label for the recording.")
    state: Optional[StrictStr] = Field(default=None, description="The state of the recording.")
    original_id: Optional[StrictStr] = Field(default=None, description="Identifier for the original recording.")
    model_id: Optional[StrictStr] = Field(default=None, description="The model identifier used for the recording.")
    model_name: Optional[StrictStr] = Field(default=None, description="The name of the model used.")
    voice_id: Optional[StrictStr] = Field(default=None, description="The voice identifier used for the recording.")
    voice_name: Optional[StrictStr] = Field(default=None, description="The name of the voice used.")
    accent_id: Optional[StrictStr] = Field(default=None, description="The accent identifier used for the recording.")
    accent_name: Optional[StrictStr] = Field(default=None, description="The name of the accent used.")
    narration_style_id: Optional[StrictStr] = Field(default=None, description="The narration style identifier used for the recording.")
    narration_style_name: Optional[StrictStr] = Field(default=None, description="The name of the narration style used.")
    semitones_correction: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Semitones correction applied to the recording.")
    calibration_id: Optional[StrictStr] = Field(default=None, description="The calibration identifier used for the recording.")
    calibration_value: Optional[StrictStr] = Field(default=None, description="The calibration value used.")
    calibration_name: Optional[StrictStr] = Field(default=None, description="The name of the calibration used.")
    microphone: Optional[StrictStr] = Field(default=None, description="The microphone used for the recording.")
    size: Optional[StrictInt] = Field(default=None, description="The size of the recording file in bytes.")
    duration: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The duration of the recording in seconds.")
    starred: Optional[StrictBool] = Field(default=None, description="Indicates if the recording is marked as favorite.")
    tts: Optional[StrictBool] = Field(default=None, description="Indicates if the recording is synthesized from text.")
    tts_voice: Optional[StrictStr] = Field(default=None, description="The TTS voice used for the recording.")
    tts_voice_id: Optional[StrictStr] = Field(default=None, description="The TTS voice identifier used for the recording.")
    text: Optional[StrictStr] = Field(default=None, description="The text content of the TTS recording.")
    params: Optional[Dict[str, Any]] = Field(default=None, description="Additional parameters for the recording.")
    error: Optional[StrictStr] = Field(default=None, description="Any error message associated with the recording.")
    active: Optional[StrictBool] = Field(default=None, description="Indicates if the recording is active.")
    created_at: Optional[datetime] = Field(default=None, description="The creation date and time of the recording.")
    converted_at: Optional[datetime] = Field(default=None, description="The date and time when the recording was converted.")
    listen_count: Optional[StrictInt] = Field(default=None, description="The number of times the recording has been played.")
    process_stage: Optional[StrictStr] = Field(default=None, description="The current processing stage of the recording.")
    note: Optional[StrictStr] = Field(default=None, description="An optional note about the recording.")
    transaction_id: Optional[StrictStr] = Field(default=None, description="The transaction identifier associated with the recording.")
    moderation: Optional[RecordingModeration] = None
    __properties: ClassVar[List[str]] = ["id", "project_id", "parent_folder_id", "type", "url", "waveform_url", "file_name", "label", "state", "original_id", "model_id", "model_name", "voice_id", "voice_name", "accent_id", "accent_name", "narration_style_id", "narration_style_name", "semitones_correction", "calibration_id", "calibration_value", "calibration_name", "microphone", "size", "duration", "starred", "tts", "tts_voice", "tts_voice_id", "text", "params", "error", "active", "created_at", "converted_at", "listen_count", "process_stage", "note", "transaction_id", "moderation"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Recording from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of moderation
        if self.moderation:
            _dict['moderation'] = self.moderation.to_dict()
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if waveform_url (nullable) is None
        # and model_fields_set contains the field
        if self.waveform_url is None and "waveform_url" in self.model_fields_set:
            _dict['waveform_url'] = None

        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['file_name'] = None

        # set to None if original_id (nullable) is None
        # and model_fields_set contains the field
        if self.original_id is None and "original_id" in self.model_fields_set:
            _dict['original_id'] = None

        # set to None if model_id (nullable) is None
        # and model_fields_set contains the field
        if self.model_id is None and "model_id" in self.model_fields_set:
            _dict['model_id'] = None

        # set to None if voice_id (nullable) is None
        # and model_fields_set contains the field
        if self.voice_id is None and "voice_id" in self.model_fields_set:
            _dict['voice_id'] = None

        # set to None if accent_id (nullable) is None
        # and model_fields_set contains the field
        if self.accent_id is None and "accent_id" in self.model_fields_set:
            _dict['accent_id'] = None

        # set to None if accent_name (nullable) is None
        # and model_fields_set contains the field
        if self.accent_name is None and "accent_name" in self.model_fields_set:
            _dict['accent_name'] = None

        # set to None if narration_style_id (nullable) is None
        # and model_fields_set contains the field
        if self.narration_style_id is None and "narration_style_id" in self.model_fields_set:
            _dict['narration_style_id'] = None

        # set to None if narration_style_name (nullable) is None
        # and model_fields_set contains the field
        if self.narration_style_name is None and "narration_style_name" in self.model_fields_set:
            _dict['narration_style_name'] = None

        # set to None if calibration_id (nullable) is None
        # and model_fields_set contains the field
        if self.calibration_id is None and "calibration_id" in self.model_fields_set:
            _dict['calibration_id'] = None

        # set to None if calibration_value (nullable) is None
        # and model_fields_set contains the field
        if self.calibration_value is None and "calibration_value" in self.model_fields_set:
            _dict['calibration_value'] = None

        # set to None if calibration_name (nullable) is None
        # and model_fields_set contains the field
        if self.calibration_name is None and "calibration_name" in self.model_fields_set:
            _dict['calibration_name'] = None

        # set to None if tts_voice (nullable) is None
        # and model_fields_set contains the field
        if self.tts_voice is None and "tts_voice" in self.model_fields_set:
            _dict['tts_voice'] = None

        # set to None if tts_voice_id (nullable) is None
        # and model_fields_set contains the field
        if self.tts_voice_id is None and "tts_voice_id" in self.model_fields_set:
            _dict['tts_voice_id'] = None

        # set to None if converted_at (nullable) is None
        # and model_fields_set contains the field
        if self.converted_at is None and "converted_at" in self.model_fields_set:
            _dict['converted_at'] = None

        # set to None if process_stage (nullable) is None
        # and model_fields_set contains the field
        if self.process_stage is None and "process_stage" in self.model_fields_set:
            _dict['process_stage'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_id is None and "transaction_id" in self.model_fields_set:
            _dict['transaction_id'] = None

        # set to None if moderation (nullable) is None
        # and model_fields_set contains the field
        if self.moderation is None and "moderation" in self.model_fields_set:
            _dict['moderation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Recording from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "project_id": obj.get("project_id"),
            "parent_folder_id": obj.get("parent_folder_id"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "waveform_url": obj.get("waveform_url"),
            "file_name": obj.get("file_name"),
            "label": obj.get("label"),
            "state": obj.get("state"),
            "original_id": obj.get("original_id"),
            "model_id": obj.get("model_id"),
            "model_name": obj.get("model_name"),
            "voice_id": obj.get("voice_id"),
            "voice_name": obj.get("voice_name"),
            "accent_id": obj.get("accent_id"),
            "accent_name": obj.get("accent_name"),
            "narration_style_id": obj.get("narration_style_id"),
            "narration_style_name": obj.get("narration_style_name"),
            "semitones_correction": obj.get("semitones_correction"),
            "calibration_id": obj.get("calibration_id"),
            "calibration_value": obj.get("calibration_value"),
            "calibration_name": obj.get("calibration_name"),
            "microphone": obj.get("microphone"),
            "size": obj.get("size"),
            "duration": obj.get("duration"),
            "starred": obj.get("starred"),
            "tts": obj.get("tts"),
            "tts_voice": obj.get("tts_voice"),
            "tts_voice_id": obj.get("tts_voice_id"),
            "text": obj.get("text"),
            "params": obj.get("params"),
            "error": obj.get("error"),
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "converted_at": obj.get("converted_at"),
            "listen_count": obj.get("listen_count"),
            "process_stage": obj.get("process_stage"),
            "note": obj.get("note"),
            "transaction_id": obj.get("transaction_id"),
            "moderation": RecordingModeration.from_dict(obj["moderation"]) if obj.get("moderation") is not None else None
        })
        return _obj

