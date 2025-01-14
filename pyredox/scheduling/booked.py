# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Booked(EventTypeAbstractModel):

    EndDateTime: Union[str, None] = Field(None)
    Meta: "BookedMeta" = Field(...)
    StartDateTime: str = Field(...)
    Visit: "BookedVisit" = Field(None)


class BookedMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["BookedMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["BookedMetaLog"] = Field(None)
    Message: "BookedMetaMessage" = Field(None)
    Source: "BookedMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "BookedMetaTransmission" = Field(None)


class BookedMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class BookedMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class BookedMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class BookedMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class BookedMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class BookedVisit(RedoxAbstractModel):

    AttendingProviders: List["BookedVisitAttendingProvider"] = Field(None)
    Location: "BookedVisitLocation" = Field(None)
    Patients: List["BookedVisitPatient"] = Field(None)
    Reason: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)
    VisitProvider: "BookedVisitVisitProvider" = Field(None)


class BookedVisitAttendingProvider(RedoxAbstractModel):

    Address: "BookedVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "BookedVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "BookedVisitAttendingProviderPhoneNumber" = Field(None)


class BookedVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class BookedVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class BookedVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class BookedVisitLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class BookedVisitPatient(RedoxAbstractModel):

    Identifiers: List["BookedVisitPatientIdentifier"] = Field(None)


class BookedVisitPatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class BookedVisitVisitProvider(RedoxAbstractModel):

    Address: "BookedVisitVisitProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "BookedVisitVisitProviderLocation" = Field(None)
    PhoneNumber: "BookedVisitVisitProviderPhoneNumber" = Field(None)


class BookedVisitVisitProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class BookedVisitVisitProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class BookedVisitVisitProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


Booked.update_forward_refs()
BookedMeta.update_forward_refs()
BookedVisit.update_forward_refs()
BookedVisitAttendingProvider.update_forward_refs()
BookedVisitPatient.update_forward_refs()
BookedVisitVisitProvider.update_forward_refs()
