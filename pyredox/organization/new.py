# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):

    Directory: str = Field(...)
    Meta: "NewMeta" = Field(...)
    Organizations: List["NewOrganization"] = Field(...)


class NewMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["NewMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NewMetaLog"] = Field(None)
    Message: "NewMetaMessage" = Field(None)
    Source: "NewMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NewMetaTransmission" = Field(None)


class NewMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NewMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewOrganization(RedoxAbstractModel):

    Active: bool = Field(...)
    Address: "NewOrganizationAddress" = Field(None)
    Aliases: List[str] = Field(None)
    Contacts: List["NewOrganizationContact"] = Field(None)
    DestinationID: Union[str, None] = Field(None)
    Endpoints: List["NewOrganizationEndpoint"] = Field(None)
    Identifiers: List["NewOrganizationIdentifier"] = Field(None)
    Name: str = Field(...)
    PartOf: "NewOrganizationPartOf" = Field(None)
    Type: "NewOrganizationType" = Field(None)


class NewOrganizationAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewOrganizationContact(RedoxAbstractModel):

    EmailAddresses: List[str] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "NewOrganizationContactPhoneNumber" = Field(None)
    Purpose: Union[str, None] = Field(None)


class NewOrganizationContactPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Work: Union[str, None] = Field(None)


class NewOrganizationEndpoint(RedoxAbstractModel):

    Address: Union[str, None] = Field(None)
    Attributes: "NewOrganizationEndpointAttributes" = Field(None)
    ConnectionType: "NewOrganizationEndpointConnectionType" = Field(None)
    Identifiers: List["NewOrganizationEndpointIdentifier"] = Field(None)
    MIMEType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewOrganizationEndpointAttributes(RedoxAbstractModel):

    Actor: "NewOrganizationEndpointAttributesActor" = Field(None)
    PurposeOfUse: List["NewOrganizationEndpointAttributesPurposeOfUse"] = Field(None)
    Roles: List["NewOrganizationEndpointAttributesRole"] = Field(None)
    Transaction: Union[str, None] = Field(None)
    UseCases: List["NewOrganizationEndpointAttributesUseCase"] = Field(None)
    Version: "NewOrganizationEndpointAttributesVersion" = Field(None)


class NewOrganizationEndpointAttributesActor(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationEndpointAttributesPurposeOfUse(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationEndpointAttributesRole(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationEndpointAttributesUseCase(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationEndpointAttributesVersion(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationEndpointConnectionType(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationEndpointIdentifier(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewOrganizationPartOf(RedoxAbstractModel):

    Identifier: "NewOrganizationPartOfIdentifier" = Field(None)


class NewOrganizationPartOfIdentifier(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewOrganizationType(RedoxAbstractModel):

    System: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


New.update_forward_refs()
NewMeta.update_forward_refs()
NewOrganization.update_forward_refs()
NewOrganizationContact.update_forward_refs()
NewOrganizationEndpoint.update_forward_refs()
NewOrganizationEndpointAttributes.update_forward_refs()
NewOrganizationPartOf.update_forward_refs()
