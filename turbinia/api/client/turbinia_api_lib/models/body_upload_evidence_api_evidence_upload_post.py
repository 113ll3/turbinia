# coding: utf-8

"""
    Turbinia API Server

    Turbinia API server

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class BodyUploadEvidenceApiEvidenceUploadPost(BaseModel):
    """
    BodyUploadEvidenceApiEvidenceUploadPost
    """
    calculate_hash: Optional[Any] = None
    files: Optional[Any] = Field(...)
    ticket_id: Optional[Any] = Field(...)
    __properties = ["calculate_hash", "files", "ticket_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BodyUploadEvidenceApiEvidenceUploadPost:
        """Create an instance of BodyUploadEvidenceApiEvidenceUploadPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if calculate_hash (nullable) is None
        # and __fields_set__ contains the field
        if self.calculate_hash is None and "calculate_hash" in self.__fields_set__:
            _dict['calculate_hash'] = None

        # set to None if files (nullable) is None
        # and __fields_set__ contains the field
        if self.files is None and "files" in self.__fields_set__:
            _dict['files'] = None

        # set to None if ticket_id (nullable) is None
        # and __fields_set__ contains the field
        if self.ticket_id is None and "ticket_id" in self.__fields_set__:
            _dict['ticket_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BodyUploadEvidenceApiEvidenceUploadPost:
        """Create an instance of BodyUploadEvidenceApiEvidenceUploadPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BodyUploadEvidenceApiEvidenceUploadPost.parse_obj(obj)

        _obj = BodyUploadEvidenceApiEvidenceUploadPost.parse_obj({
            "calculate_hash": obj.get("calculate_hash"),
            "files": obj.get("files"),
            "ticket_id": obj.get("ticket_id")
        })
        return _obj


