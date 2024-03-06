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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from respeecher.models.accent import Accent
from respeecher.models.tier import Tier
from typing import Optional, Set
from typing_extensions import Self

class Voice(BaseModel):
    """
    Voice
    """ # noqa: E501
    id: Optional[StrictStr] = None
    owner_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    slug: Optional[StrictStr] = None
    visibility: Optional[StrictStr] = None
    species: Optional[StrictStr] = None
    artist: Optional[StrictStr] = None
    verified_artist: Optional[StrictBool] = None
    gender: Optional[StrictStr] = None
    pitch: Optional[Union[StrictFloat, StrictInt]] = None
    age_group: Optional[StrictStr] = None
    pitch_group: Optional[StrictStr] = None
    nationality: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    thumbnail_url: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    rating: Optional[StrictInt] = None
    active: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    favorite: Optional[StrictBool] = None
    available: Optional[StrictBool] = None
    accents: Optional[List[Accent]] = None
    narration_styles: Optional[List[Dict[str, Any]]] = None
    tiers: Optional[List[Tier]] = None
    __properties: ClassVar[List[str]] = ["id", "owner_id", "name", "slug", "visibility", "species", "artist", "verified_artist", "gender", "pitch", "age_group", "pitch_group", "nationality", "image_url", "thumbnail_url", "description", "rating", "active", "created_at", "favorite", "available", "accents", "narration_styles", "tiers"]

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
        """Create an instance of Voice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in accents (list)
        _items = []
        if self.accents:
            for _item in self.accents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item in self.tiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tiers'] = _items
        # set to None if artist (nullable) is None
        # and model_fields_set contains the field
        if self.artist is None and "artist" in self.model_fields_set:
            _dict['artist'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Voice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "owner_id": obj.get("owner_id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "visibility": obj.get("visibility"),
            "species": obj.get("species"),
            "artist": obj.get("artist"),
            "verified_artist": obj.get("verified_artist"),
            "gender": obj.get("gender"),
            "pitch": obj.get("pitch"),
            "age_group": obj.get("age_group"),
            "pitch_group": obj.get("pitch_group"),
            "nationality": obj.get("nationality"),
            "image_url": obj.get("image_url"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "description": obj.get("description"),
            "rating": obj.get("rating"),
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "favorite": obj.get("favorite"),
            "available": obj.get("available"),
            "accents": [Accent.from_dict(_item) for _item in obj["accents"]] if obj.get("accents") is not None else None,
            "narration_styles": obj.get("narration_styles"),
            "tiers": [Tier.from_dict(_item) for _item in obj["tiers"]] if obj.get("tiers") is not None else None
        })
        return _obj

