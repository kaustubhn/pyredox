# -*- coding: utf-8 -*-
"""Base class for all Redox elements."""
import abc
from typing import Any

from pydantic import BaseModel, Field

__all__ = [
    "EventTypeAbstractModel",
    "RedoxAbstractModel",
]


class RedoxAbstractModel(BaseModel, abc.ABC):
    Extensions: Any = Field(None)

    def __str__(self):
        return self.json()

    def dict(
        self,
        *,
        include=None,
        exclude=None,
        by_alias: bool = False,
        skip_defaults: bool = None,
        exclude_unset: bool = True,  # Differs from default
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ):
        return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )


class _Meta(RedoxAbstractModel, abc.ABC):
    """Bare minimum fields for all ``Meta`` types.

    This is defined strictly for type hinting purposes. No ``Meta`` field class
    should inherit from this or reference this class for simplicity's sake.
    """

    DataModel: str = Field(...)
    EventType: str = Field(...)


class EventTypeAbstractModel(RedoxAbstractModel, abc.ABC):
    """Event types should inherit from this instead of RedoxAbstractModel."""

    Meta: _Meta = Field(...)