# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class AccountUpdate(EventTypeAbstractModel):

    Meta: "AccountUpdateMeta" = Field(...)
    Patient: "AccountUpdatePatient" = Field(...)
    Visit: "AccountUpdateVisit" = Field(None)


class AccountUpdateMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["AccountUpdateMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["AccountUpdateMetaLog"] = Field(None)
    Message: "AccountUpdateMetaMessage" = Field(None)
    Source: "AccountUpdateMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "AccountUpdateMetaTransmission" = Field(None)


class AccountUpdateMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AccountUpdateMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class AccountUpdateMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class AccountUpdateMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AccountUpdateMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class AccountUpdatePatient(RedoxAbstractModel):

    Demographics: "AccountUpdatePatientDemographics" = Field(None)
    Identifiers: List["AccountUpdatePatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class AccountUpdatePatientDemographics(RedoxAbstractModel):

    Address: "AccountUpdatePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "AccountUpdatePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class AccountUpdatePatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdatePatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class AccountUpdatePatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class AccountUpdateVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "AccountUpdateVisitAttendingProvider" = Field(None)
    Balance: Union[Number, None] = Field(None)
    ConsultingProvider: "AccountUpdateVisitConsultingProvider" = Field(None)
    Diagnoses: List["AccountUpdateVisitDiagnosis"] = Field(None)
    DiagnosisRelatedGroup: Union[Number, None] = Field(None)
    DiagnosisRelatedGroupType: Union[Number, None] = Field(None)
    DischargeDateTime: Union[str, None] = Field(None)
    Guarantor: "AccountUpdateVisitGuarantor" = Field(None)
    Insurances: List["AccountUpdateVisitInsurance"] = Field(None)
    Location: "AccountUpdateVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Procedures: List["AccountUpdateVisitProcedure"] = Field(None)
    ReferringProvider: "AccountUpdateVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class AccountUpdateVisitAttendingProvider(RedoxAbstractModel):

    Address: "AccountUpdateVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AccountUpdateVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "AccountUpdateVisitAttendingProviderPhoneNumber" = Field(None)


class AccountUpdateVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class AccountUpdateVisitConsultingProvider(RedoxAbstractModel):

    Address: "AccountUpdateVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AccountUpdateVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "AccountUpdateVisitConsultingProviderPhoneNumber" = Field(None)


class AccountUpdateVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class AccountUpdateVisitDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitGuarantor(RedoxAbstractModel):

    Address: "AccountUpdateVisitGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "AccountUpdateVisitGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "AccountUpdateVisitGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "AccountUpdateVisitGuarantorSpouse" = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitGuarantorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitGuarantorEmployer(RedoxAbstractModel):

    Address: "AccountUpdateVisitGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class AccountUpdateVisitGuarantorEmployerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitGuarantorPhoneNumber(RedoxAbstractModel):

    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class AccountUpdateVisitGuarantorSpouse(RedoxAbstractModel):

    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class AccountUpdateVisitInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "AccountUpdateVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "AccountUpdateVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "AccountUpdateVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class AccountUpdateVisitInsuranceCompany(RedoxAbstractModel):

    Address: "AccountUpdateVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class AccountUpdateVisitInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitInsuranceInsured(RedoxAbstractModel):

    Address: "AccountUpdateVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["AccountUpdateVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class AccountUpdateVisitInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AccountUpdateVisitInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitLocation(RedoxAbstractModel):

    Address: "AccountUpdateVisitLocationAddress" = Field(None)
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitLocationAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitProcedure(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    PerformedDateTime: Union[str, None] = Field(None)
    Performers: List["AccountUpdateVisitProcedurePerformer"] = Field(None)


class AccountUpdateVisitProcedurePerformer(RedoxAbstractModel):

    Address: "AccountUpdateVisitProcedurePerformerAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AccountUpdateVisitProcedurePerformerLocation" = Field(None)
    PhoneNumber: "AccountUpdateVisitProcedurePerformerPhoneNumber" = Field(None)


class AccountUpdateVisitProcedurePerformerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitProcedurePerformerLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitProcedurePerformerPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class AccountUpdateVisitReferringProvider(RedoxAbstractModel):

    Address: "AccountUpdateVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AccountUpdateVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "AccountUpdateVisitReferringProviderPhoneNumber" = Field(None)


class AccountUpdateVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AccountUpdateVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AccountUpdateVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


AccountUpdate.update_forward_refs()
AccountUpdateMeta.update_forward_refs()
AccountUpdatePatient.update_forward_refs()
AccountUpdatePatientDemographics.update_forward_refs()
AccountUpdateVisit.update_forward_refs()
AccountUpdateVisitAttendingProvider.update_forward_refs()
AccountUpdateVisitConsultingProvider.update_forward_refs()
AccountUpdateVisitGuarantor.update_forward_refs()
AccountUpdateVisitGuarantorEmployer.update_forward_refs()
AccountUpdateVisitInsurance.update_forward_refs()
AccountUpdateVisitInsuranceCompany.update_forward_refs()
AccountUpdateVisitInsuranceInsured.update_forward_refs()
AccountUpdateVisitLocation.update_forward_refs()
AccountUpdateVisitProcedure.update_forward_refs()
AccountUpdateVisitProcedurePerformer.update_forward_refs()
AccountUpdateVisitReferringProvider.update_forward_refs()
