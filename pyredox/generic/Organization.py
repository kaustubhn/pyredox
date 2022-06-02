# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import organization
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _Organization(GenericRedoxAbstractModel):
    _redox_module = organization


class New(_Organization):

    Directory: str = Field(...)
    Meta: generic.Meta = Field(...)
    Organizations: List[generic.Organization] = Field(...)


class Query(_Organization):

    Directory: str = Field(...)
    Identifier: generic.Identifier = Field(None)
    Index: Union[str, None] = Field(None)
    LastUpdated: Union[str, None] = Field(None)
    Limit: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    NameSearch: generic.NameSearch = Field(None)
    RadiusSearch: generic.RadiusSearch = Field(None)
    State: Union[str, None] = Field(None)


class QueryResponse(_Organization):

    Directory: str = Field(...)
    Meta: generic.Meta = Field(...)
    Organizations: List[generic.Organization] = Field(...)
    Paging: generic.Paging = Field(None)


class Update(_Organization):

    Action: str = Field(...)
    Directory: str = Field(...)
    Meta: generic.Meta = Field(...)
    Organizations: List[generic.Organization] = Field(...)