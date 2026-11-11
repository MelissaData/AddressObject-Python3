from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
  lib = ctypes.CDLL('mdAddr.dll', winmode=0)
elif (os.name == 'nt'):
  lib = ctypes.CDLL('mdAddr.dll')
else:
  lib = ctypes.CDLL('libmdAddr.so')

lib.mdAddrCreate.argtypes = []
lib.mdAddrCreate.restype = c_void_p
lib.mdAddrDestroy.argtypes = [c_void_p]
lib.mdAddrDestroy.restype = None
lib.mdAddrInitialize.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdAddrInitialize.restype = c_int
lib.mdAddrInitializeDataFiles.argtypes = [c_void_p]
lib.mdAddrInitializeDataFiles.restype = c_int
lib.mdAddrGetInitializeErrorString.argtypes = [c_void_p]
lib.mdAddrGetInitializeErrorString.restype = c_char_p
lib.mdAddrSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetLicenseString.restype = c_bool
lib.mdAddrGetBuildNumber.argtypes = [c_void_p]
lib.mdAddrGetBuildNumber.restype = c_char_p
lib.mdAddrGetDatabaseDate.argtypes = [c_void_p]
lib.mdAddrGetDatabaseDate.restype = c_char_p
lib.mdAddrGetExpirationDate.argtypes = [c_void_p]
lib.mdAddrGetExpirationDate.restype = c_char_p
lib.mdAddrGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdAddrGetLicenseExpirationDate.restype = c_char_p
lib.mdAddrGetCanadianDatabaseDate.argtypes = [c_void_p]
lib.mdAddrGetCanadianDatabaseDate.restype = c_char_p
lib.mdAddrGetCanadianExpirationDate.argtypes = [c_void_p]
lib.mdAddrGetCanadianExpirationDate.restype = c_char_p
lib.mdAddrSetPathToUSFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToUSFiles.restype = None
lib.mdAddrSetPathToCanadaFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToCanadaFiles.restype = None
lib.mdAddrSetPathToDPVDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToDPVDataFiles.restype = None
lib.mdAddrSetPathToLACSLinkDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToLACSLinkDataFiles.restype = None
lib.mdAddrSetPathToSuiteLinkDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToSuiteLinkDataFiles.restype = None
lib.mdAddrSetPathToSuiteFinderDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToSuiteFinderDataFiles.restype = None
lib.mdAddrSetPathToRBDIFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToRBDIFiles.restype = None
lib.mdAddrGetRBDIDatabaseDate.argtypes = [c_void_p]
lib.mdAddrGetRBDIDatabaseDate.restype = c_char_p
lib.mdAddrSetPathToAddrKeyDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPathToAddrKeyDataFiles.restype = None
lib.mdAddrClearProperties.argtypes = [c_void_p]
lib.mdAddrClearProperties.restype = None
lib.mdAddrResetDPV.argtypes = [c_void_p]
lib.mdAddrResetDPV.restype = None
lib.mdAddrSetCASSEnable.argtypes = [c_void_p, c_int]
lib.mdAddrSetCASSEnable.restype = None
lib.mdAddrSetUseUSPSPreferredCityNames.argtypes = [c_void_p, c_int]
lib.mdAddrSetUseUSPSPreferredCityNames.restype = None
lib.mdAddrSetDiacritics.argtypes = [c_void_p, c_int]
lib.mdAddrSetDiacritics.restype = None
lib.mdAddrGetStatusCode.argtypes = [c_void_p]
lib.mdAddrGetStatusCode.restype = c_char_p
lib.mdAddrGetErrorCode.argtypes = [c_void_p]
lib.mdAddrGetErrorCode.restype = c_char_p
lib.mdAddrGetErrorString.argtypes = [c_void_p]
lib.mdAddrGetErrorString.restype = c_char_p
lib.mdAddrGetResults.argtypes = [c_void_p]
lib.mdAddrGetResults.restype = c_char_p
lib.mdAddrGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdAddrGetResultCodeDescription.restype = c_char_p
lib.mdAddrSetPS3553_B1_ProcessorName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_B1_ProcessorName.restype = None
lib.mdAddrSetPS3553_B4_ListName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_B4_ListName.restype = None
lib.mdAddrSetPS3553_D3_Name.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_Name.restype = None
lib.mdAddrSetPS3553_D3_Company.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_Company.restype = None
lib.mdAddrSetPS3553_D3_Address.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_Address.restype = None
lib.mdAddrSetPS3553_D3_City.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_City.restype = None
lib.mdAddrSetPS3553_D3_State.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_State.restype = None
lib.mdAddrSetPS3553_D3_ZIP.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPS3553_D3_ZIP.restype = None
lib.mdAddrGetFormPS3553.argtypes = [c_void_p]
lib.mdAddrGetFormPS3553.restype = c_char_p
lib.mdAddrSaveFormPS3553.argtypes = [c_void_p, c_char_p]
lib.mdAddrSaveFormPS3553.restype = c_bool
lib.mdAddrResetFormPS3553.argtypes = [c_void_p]
lib.mdAddrResetFormPS3553.restype = None
lib.mdAddrResetFormPS3553Counter.argtypes = [c_void_p]
lib.mdAddrResetFormPS3553Counter.restype = None
lib.mdAddrSetStandardizationType.argtypes = [c_void_p, c_int]
lib.mdAddrSetStandardizationType.restype = None
lib.mdAddrSetSuiteParseMode.argtypes = [c_void_p, c_int]
lib.mdAddrSetSuiteParseMode.restype = None
lib.mdAddrSetAliasMode.argtypes = [c_void_p, c_int]
lib.mdAddrSetAliasMode.restype = None
lib.mdAddrGetFormSOA.argtypes = [c_void_p]
lib.mdAddrGetFormSOA.restype = c_char_p
lib.mdAddrSaveFormSOA.argtypes = [c_void_p, c_char_p]
lib.mdAddrSaveFormSOA.restype = None
lib.mdAddrResetFormSOA.argtypes = [c_void_p]
lib.mdAddrResetFormSOA.restype = None
lib.mdAddrSetSOACustomerInfo.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdAddrSetSOACustomerInfo.restype = None
lib.mdAddrSetSOACPCNumber.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetSOACPCNumber.restype = None
lib.mdAddrGetSOACustomerInfo.argtypes = [c_void_p]
lib.mdAddrGetSOACustomerInfo.restype = c_char_p
lib.mdAddrGetSOACPCNumber.argtypes = [c_void_p]
lib.mdAddrGetSOACPCNumber.restype = c_char_p
lib.mdAddrGetSOATotalRecords.argtypes = [c_void_p]
lib.mdAddrGetSOATotalRecords.restype = c_long
lib.mdAddrGetSOAAAPercentage.argtypes = [c_void_p]
lib.mdAddrGetSOAAAPercentage.restype = c_float
lib.mdAddrGetSOAAAExpiryDate.argtypes = [c_void_p]
lib.mdAddrGetSOAAAExpiryDate.restype = c_char_p
lib.mdAddrGetSOASoftwareInfo.argtypes = [c_void_p]
lib.mdAddrGetSOASoftwareInfo.restype = c_char_p
lib.mdAddrGetSOAErrorString.argtypes = [c_void_p]
lib.mdAddrGetSOAErrorString.restype = c_char_p
lib.mdAddrSetCompany.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetCompany.restype = None
lib.mdAddrSetLastName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetLastName.restype = None
lib.mdAddrSetAddress.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetAddress.restype = None
lib.mdAddrSetAddress2.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetAddress2.restype = None
lib.mdAddrSetLastLine.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetLastLine.restype = None
lib.mdAddrSetSuite.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetSuite.restype = None
lib.mdAddrSetCity.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetCity.restype = None
lib.mdAddrSetState.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetState.restype = None
lib.mdAddrSetZip.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetZip.restype = None
lib.mdAddrSetPlus4.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetPlus4.restype = None
lib.mdAddrSetUrbanization.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetUrbanization.restype = None
lib.mdAddrSetParsedAddressRange.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedAddressRange.restype = None
lib.mdAddrSetParsedPreDirection.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedPreDirection.restype = None
lib.mdAddrSetParsedStreetName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedStreetName.restype = None
lib.mdAddrSetParsedSuffix.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedSuffix.restype = None
lib.mdAddrSetParsedPostDirection.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedPostDirection.restype = None
lib.mdAddrSetParsedSuiteName.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedSuiteName.restype = None
lib.mdAddrSetParsedSuiteRange.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedSuiteRange.restype = None
lib.mdAddrSetParsedRouteService.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedRouteService.restype = None
lib.mdAddrSetParsedLockBox.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedLockBox.restype = None
lib.mdAddrSetParsedDeliveryInstallation.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetParsedDeliveryInstallation.restype = None
lib.mdAddrSetCountryCode.argtypes = [c_void_p, c_char_p]
lib.mdAddrSetCountryCode.restype = None
lib.mdAddrVerifyAddress.argtypes = [c_void_p]
lib.mdAddrVerifyAddress.restype = c_bool
lib.mdAddrGetCompany.argtypes = [c_void_p]
lib.mdAddrGetCompany.restype = c_char_p
lib.mdAddrGetLastName.argtypes = [c_void_p]
lib.mdAddrGetLastName.restype = c_char_p
lib.mdAddrGetAddress.argtypes = [c_void_p]
lib.mdAddrGetAddress.restype = c_char_p
lib.mdAddrGetAddress2.argtypes = [c_void_p]
lib.mdAddrGetAddress2.restype = c_char_p
lib.mdAddrGetSuite.argtypes = [c_void_p]
lib.mdAddrGetSuite.restype = c_char_p
lib.mdAddrGetCity.argtypes = [c_void_p]
lib.mdAddrGetCity.restype = c_char_p
lib.mdAddrGetCityAbbreviation.argtypes = [c_void_p]
lib.mdAddrGetCityAbbreviation.restype = c_char_p
lib.mdAddrGetState.argtypes = [c_void_p]
lib.mdAddrGetState.restype = c_char_p
lib.mdAddrGetZip.argtypes = [c_void_p]
lib.mdAddrGetZip.restype = c_char_p
lib.mdAddrGetPlus4.argtypes = [c_void_p]
lib.mdAddrGetPlus4.restype = c_char_p
lib.mdAddrGetCarrierRoute.argtypes = [c_void_p]
lib.mdAddrGetCarrierRoute.restype = c_char_p
lib.mdAddrGetDeliveryPointCode.argtypes = [c_void_p]
lib.mdAddrGetDeliveryPointCode.restype = c_char_p
lib.mdAddrGetDeliveryPointCheckDigit.argtypes = [c_void_p]
lib.mdAddrGetDeliveryPointCheckDigit.restype = c_char_p
lib.mdAddrGetCountyFips.argtypes = [c_void_p]
lib.mdAddrGetCountyFips.restype = c_char_p
lib.mdAddrGetCountyName.argtypes = [c_void_p]
lib.mdAddrGetCountyName.restype = c_char_p
lib.mdAddrGetAddressTypeCode.argtypes = [c_void_p]
lib.mdAddrGetAddressTypeCode.restype = c_char_p
lib.mdAddrGetAddressTypeString.argtypes = [c_void_p]
lib.mdAddrGetAddressTypeString.restype = c_char_p
lib.mdAddrGetUrbanization.argtypes = [c_void_p]
lib.mdAddrGetUrbanization.restype = c_char_p
lib.mdAddrGetCongressionalDistrict.argtypes = [c_void_p]
lib.mdAddrGetCongressionalDistrict.restype = c_char_p
lib.mdAddrGetLACS.argtypes = [c_void_p]
lib.mdAddrGetLACS.restype = c_char_p
lib.mdAddrGetLACSLinkIndicator.argtypes = [c_void_p]
lib.mdAddrGetLACSLinkIndicator.restype = c_char_p
lib.mdAddrGetPrivateMailbox.argtypes = [c_void_p]
lib.mdAddrGetPrivateMailbox.restype = c_char_p
lib.mdAddrGetTimeZoneCode.argtypes = [c_void_p]
lib.mdAddrGetTimeZoneCode.restype = c_char_p
lib.mdAddrGetTimeZone.argtypes = [c_void_p]
lib.mdAddrGetTimeZone.restype = c_char_p
lib.mdAddrGetMsa.argtypes = [c_void_p]
lib.mdAddrGetMsa.restype = c_char_p
lib.mdAddrGetPmsa.argtypes = [c_void_p]
lib.mdAddrGetPmsa.restype = c_char_p
lib.mdAddrGetDefaultFlagIndicator.argtypes = [c_void_p]
lib.mdAddrGetDefaultFlagIndicator.restype = c_char_p
lib.mdAddrGetSuiteStatus.argtypes = [c_void_p]
lib.mdAddrGetSuiteStatus.restype = c_char_p
lib.mdAddrGetEWSFlag.argtypes = [c_void_p]
lib.mdAddrGetEWSFlag.restype = c_char_p
lib.mdAddrGetCMRA.argtypes = [c_void_p]
lib.mdAddrGetCMRA.restype = c_char_p
lib.mdAddrGetDsfVacant.argtypes = [c_void_p]
lib.mdAddrGetDsfVacant.restype = c_char_p
lib.mdAddrGetCountryCode.argtypes = [c_void_p]
lib.mdAddrGetCountryCode.restype = c_char_p
lib.mdAddrGetZipType.argtypes = [c_void_p]
lib.mdAddrGetZipType.restype = c_char_p
lib.mdAddrGetFalseTable.argtypes = [c_void_p]
lib.mdAddrGetFalseTable.restype = c_char_p
lib.mdAddrGetDPVFootnotes.argtypes = [c_void_p]
lib.mdAddrGetDPVFootnotes.restype = c_char_p
lib.mdAddrGetLACSLinkReturnCode.argtypes = [c_void_p]
lib.mdAddrGetLACSLinkReturnCode.restype = c_char_p
lib.mdAddrGetSuiteLinkReturnCode.argtypes = [c_void_p]
lib.mdAddrGetSuiteLinkReturnCode.restype = c_char_p
lib.mdAddrGetRBDI.argtypes = [c_void_p]
lib.mdAddrGetRBDI.restype = c_char_p
lib.mdAddrGetELotNumber.argtypes = [c_void_p]
lib.mdAddrGetELotNumber.restype = c_char_p
lib.mdAddrGetELotOrder.argtypes = [c_void_p]
lib.mdAddrGetELotOrder.restype = c_char_p
lib.mdAddrGetAddressKey.argtypes = [c_void_p]
lib.mdAddrGetAddressKey.restype = c_char_p
lib.mdAddrGetMelissaAddressKey.argtypes = [c_void_p]
lib.mdAddrGetMelissaAddressKey.restype = c_char_p
lib.mdAddrGetMelissaAddressKeyBase.argtypes = [c_void_p]
lib.mdAddrGetMelissaAddressKeyBase.restype = c_char_p
lib.mdAddrGetOutputParameter.argtypes = [c_void_p, c_char_p]
lib.mdAddrGetOutputParameter.restype = c_char_p
lib.mdAddrSetInputParameter.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdAddrSetInputParameter.restype = c_int
lib.mdAddrFindSuggestion.argtypes = [c_void_p]
lib.mdAddrFindSuggestion.restype = c_bool
lib.mdAddrFindSuggestionNext.argtypes = [c_void_p]
lib.mdAddrFindSuggestionNext.restype = c_bool
lib.mdAddrGetDsfNoStats.argtypes = [c_void_p]
lib.mdAddrGetDsfNoStats.restype = c_char_p
lib.mdAddrGetDsfDNA.argtypes = [c_void_p]
lib.mdAddrGetDsfDNA.restype = c_char_p
lib.mdAddrGetPS3553_B6_TotalRecords.argtypes = [c_void_p]
lib.mdAddrGetPS3553_B6_TotalRecords.restype = c_int
lib.mdAddrGetPS3553_C1a_ZIP4Coded.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1a_ZIP4Coded.restype = c_int
lib.mdAddrGetPS3553_C1c_DPBCAssigned.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1c_DPBCAssigned.restype = c_int
lib.mdAddrGetPS3553_C1d_FiveDigitCoded.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1d_FiveDigitCoded.restype = c_int
lib.mdAddrGetPS3553_C1e_CRRTCoded.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1e_CRRTCoded.restype = c_int
lib.mdAddrGetPS3553_C1f_eLOTAssigned.argtypes = [c_void_p]
lib.mdAddrGetPS3553_C1f_eLOTAssigned.restype = c_int
lib.mdAddrGetPS3553_E_HighRiseDefault.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_HighRiseDefault.restype = c_int
lib.mdAddrGetPS3553_E_HighRiseExact.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_HighRiseExact.restype = c_int
lib.mdAddrGetPS3553_E_RuralRouteDefault.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_RuralRouteDefault.restype = c_int
lib.mdAddrGetPS3553_E_RuralRouteExact.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_RuralRouteExact.restype = c_int
lib.mdAddrGetZip4HRDefault.argtypes = [c_void_p]
lib.mdAddrGetZip4HRDefault.restype = c_int
lib.mdAddrGetZip4HRExact.argtypes = [c_void_p]
lib.mdAddrGetZip4HRExact.restype = c_int
lib.mdAddrGetZip4RRDefault.argtypes = [c_void_p]
lib.mdAddrGetZip4RRDefault.restype = c_int
lib.mdAddrGetZip4RRExact.argtypes = [c_void_p]
lib.mdAddrGetZip4RRExact.restype = c_int
lib.mdAddrGetPS3553_E_LACSCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_LACSCount.restype = c_int
lib.mdAddrGetPS3553_E_EWSCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_EWSCount.restype = c_int
lib.mdAddrGetPS3553_E_DPVCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_E_DPVCount.restype = c_int
lib.mdAddrGetPS3553_X_POBoxCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_POBoxCount.restype = c_int
lib.mdAddrGetPS3553_X_HCExactCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_HCExactCount.restype = c_int
lib.mdAddrGetPS3553_X_FirmCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_FirmCount.restype = c_int
lib.mdAddrGetPS3553_X_GenDeliveryCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_GenDeliveryCount.restype = c_int
lib.mdAddrGetPS3553_X_MilitaryZipCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_MilitaryZipCount.restype = c_int
lib.mdAddrGetPS3553_X_NonDeliveryCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_NonDeliveryCount.restype = c_int
lib.mdAddrGetPS3553_X_StreetCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_StreetCount.restype = c_int
lib.mdAddrGetPS3553_X_HCDefaultCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_HCDefaultCount.restype = c_int
lib.mdAddrGetPS3553_X_OtherCount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_OtherCount.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCodeACount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCodeACount.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode00Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode00Count.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode14Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode14Count.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode92Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode92Count.restype = c_int
lib.mdAddrGetPS3553_X_LacsLinkCode09Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_LacsLinkCode09Count.restype = c_int
lib.mdAddrGetPS3553_X_SuiteLinkCodeACount.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_SuiteLinkCodeACount.restype = c_int
lib.mdAddrGetPS3553_X_SuiteLinkCode00Count.argtypes = [c_void_p]
lib.mdAddrGetPS3553_X_SuiteLinkCode00Count.restype = c_int
lib.mdAddrGetParsedAddressRange.argtypes = [c_void_p]
lib.mdAddrGetParsedAddressRange.restype = c_char_p
lib.mdAddrGetParsedPreDirection.argtypes = [c_void_p]
lib.mdAddrGetParsedPreDirection.restype = c_char_p
lib.mdAddrGetParsedStreetName.argtypes = [c_void_p]
lib.mdAddrGetParsedStreetName.restype = c_char_p
lib.mdAddrGetParsedSuffix.argtypes = [c_void_p]
lib.mdAddrGetParsedSuffix.restype = c_char_p
lib.mdAddrGetParsedPostDirection.argtypes = [c_void_p]
lib.mdAddrGetParsedPostDirection.restype = c_char_p
lib.mdAddrGetParsedSuiteName.argtypes = [c_void_p]
lib.mdAddrGetParsedSuiteName.restype = c_char_p
lib.mdAddrGetParsedSuiteRange.argtypes = [c_void_p]
lib.mdAddrGetParsedSuiteRange.restype = c_char_p
lib.mdAddrGetParsedPrivateMailboxName.argtypes = [c_void_p]
lib.mdAddrGetParsedPrivateMailboxName.restype = c_char_p
lib.mdAddrGetParsedPrivateMailboxNumber.argtypes = [c_void_p]
lib.mdAddrGetParsedPrivateMailboxNumber.restype = c_char_p
lib.mdAddrGetParsedGarbage.argtypes = [c_void_p]
lib.mdAddrGetParsedGarbage.restype = c_char_p
lib.mdAddrGetParsedRouteService.argtypes = [c_void_p]
lib.mdAddrGetParsedRouteService.restype = c_char_p
lib.mdAddrGetParsedLockBox.argtypes = [c_void_p]
lib.mdAddrGetParsedLockBox.restype = c_char_p
lib.mdAddrGetParsedDeliveryInstallation.argtypes = [c_void_p]
lib.mdAddrGetParsedDeliveryInstallation.restype = c_char_p
lib.mdAddrSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdAddrSetReserved.restype = None
lib.mdAddrGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdAddrGetReserved.restype = c_char_p

lib.mdParseCreate.argtypes = []
lib.mdParseCreate.restype = c_void_p
lib.mdParseDestroy.argtypes = [c_void_p]
lib.mdParseDestroy.restype = None
lib.mdParseInitialize.argtypes = [c_void_p, c_char_p]
lib.mdParseInitialize.restype = c_int
lib.mdParseGetBuildNumber.argtypes = [c_void_p]
lib.mdParseGetBuildNumber.restype = c_char_p
lib.mdParseParse.argtypes = [c_void_p, c_char_p]
lib.mdParseParse.restype = None
lib.mdParseParseCanadian.argtypes = [c_void_p, c_char_p]
lib.mdParseParseCanadian.restype = None
lib.mdParseParseNext.argtypes = [c_void_p]
lib.mdParseParseNext.restype = c_bool
lib.mdParseLastLineParse.argtypes = [c_void_p, c_char_p]
lib.mdParseLastLineParse.restype = None
lib.mdParseGetZip.argtypes = [c_void_p]
lib.mdParseGetZip.restype = c_char_p
lib.mdParseGetPlus4.argtypes = [c_void_p]
lib.mdParseGetPlus4.restype = c_char_p
lib.mdParseGetCity.argtypes = [c_void_p]
lib.mdParseGetCity.restype = c_char_p
lib.mdParseGetState.argtypes = [c_void_p]
lib.mdParseGetState.restype = c_char_p
lib.mdParseGetStreetName.argtypes = [c_void_p]
lib.mdParseGetStreetName.restype = c_char_p
lib.mdParseGetRange.argtypes = [c_void_p]
lib.mdParseGetRange.restype = c_char_p
lib.mdParseGetPreDirection.argtypes = [c_void_p]
lib.mdParseGetPreDirection.restype = c_char_p
lib.mdParseGetPostDirection.argtypes = [c_void_p]
lib.mdParseGetPostDirection.restype = c_char_p
lib.mdParseGetSuffix.argtypes = [c_void_p]
lib.mdParseGetSuffix.restype = c_char_p
lib.mdParseGetSuiteName.argtypes = [c_void_p]
lib.mdParseGetSuiteName.restype = c_char_p
lib.mdParseGetSuiteNumber.argtypes = [c_void_p]
lib.mdParseGetSuiteNumber.restype = c_char_p
lib.mdParseGetPrivateMailboxNumber.argtypes = [c_void_p]
lib.mdParseGetPrivateMailboxNumber.restype = c_char_p
lib.mdParseGetPrivateMailboxName.argtypes = [c_void_p]
lib.mdParseGetPrivateMailboxName.restype = c_char_p
lib.mdParseGetGarbage.argtypes = [c_void_p]
lib.mdParseGetGarbage.restype = c_char_p
lib.mdParseGetRouteService.argtypes = [c_void_p]
lib.mdParseGetRouteService.restype = c_char_p
lib.mdParseGetLockBox.argtypes = [c_void_p]
lib.mdParseGetLockBox.restype = c_char_p
lib.mdParseGetDeliveryInstallation.argtypes = [c_void_p]
lib.mdParseGetDeliveryInstallation.restype = c_char_p
lib.mdParseParseRule.argtypes = [c_void_p]
lib.mdParseParseRule.restype = c_int

lib.mdStreetCreate.argtypes = []
lib.mdStreetCreate.restype = c_void_p
lib.mdStreetDestroy.argtypes = [c_void_p]
lib.mdStreetDestroy.restype = None
lib.mdStreetInitialize.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdStreetInitialize.restype = c_int
lib.mdStreetGetInitializeErrorString.argtypes = [c_void_p]
lib.mdStreetGetInitializeErrorString.restype = c_char_p
lib.mdStreetGetDatabaseDate.argtypes = [c_void_p]
lib.mdStreetGetDatabaseDate.restype = c_char_p
lib.mdStreetGetBuildNumber.argtypes = [c_void_p]
lib.mdStreetGetBuildNumber.restype = c_char_p
lib.mdStreetSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdStreetSetLicenseString.restype = c_bool
lib.mdStreetGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdStreetGetLicenseExpirationDate.restype = c_char_p
lib.mdStreetFindStreet.argtypes = [c_void_p, c_char_p, c_char_p, c_bool]
lib.mdStreetFindStreet.restype = c_bool
lib.mdStreetFindStreetNext.argtypes = [c_void_p]
lib.mdStreetFindStreetNext.restype = c_bool
lib.mdStreetIsAddressInRange.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdStreetIsAddressInRange.restype = c_bool
lib.mdStreetIsAddressInRange2.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p, c_char_p]
lib.mdStreetIsAddressInRange2.restype = c_bool
lib.mdStreetGetAutoCompletion.argtypes = [c_void_p, c_char_p, c_char_p, c_int, c_bool]
lib.mdStreetGetAutoCompletion.restype = c_char_p
lib.mdStreetResetAutoCompletion.argtypes = [c_void_p]
lib.mdStreetResetAutoCompletion.restype = None
lib.mdStreetGetBaseAlternateIndicator.argtypes = [c_void_p]
lib.mdStreetGetBaseAlternateIndicator.restype = c_char_p
lib.mdStreetGetLACSIndicator.argtypes = [c_void_p]
lib.mdStreetGetLACSIndicator.restype = c_char_p
lib.mdStreetGetUrbanizationCode.argtypes = [c_void_p]
lib.mdStreetGetUrbanizationCode.restype = c_char_p
lib.mdStreetGetUrbanizationName.argtypes = [c_void_p]
lib.mdStreetGetUrbanizationName.restype = c_char_p
lib.mdStreetGetLastLineNumber.argtypes = [c_void_p]
lib.mdStreetGetLastLineNumber.restype = c_char_p
lib.mdStreetGetAddressType.argtypes = [c_void_p]
lib.mdStreetGetAddressType.restype = c_char_p
lib.mdStreetGetCongressionalDistrict.argtypes = [c_void_p]
lib.mdStreetGetCongressionalDistrict.restype = c_char_p
lib.mdStreetGetCountyFips.argtypes = [c_void_p]
lib.mdStreetGetCountyFips.restype = c_char_p
lib.mdStreetGetCompany.argtypes = [c_void_p]
lib.mdStreetGetCompany.restype = c_char_p
lib.mdStreetGetCarrierRoute.argtypes = [c_void_p]
lib.mdStreetGetCarrierRoute.restype = c_char_p
lib.mdStreetGetZip.argtypes = [c_void_p]
lib.mdStreetGetZip.restype = c_char_p
lib.mdStreetGetDeliveryInstallation.argtypes = [c_void_p]
lib.mdStreetGetDeliveryInstallation.restype = c_char_p
lib.mdStreetGetPlus4High.argtypes = [c_void_p]
lib.mdStreetGetPlus4High.restype = c_char_p
lib.mdStreetGetPlus4Low.argtypes = [c_void_p]
lib.mdStreetGetPlus4Low.restype = c_char_p
lib.mdStreetGetSuiteRangeOddEven.argtypes = [c_void_p]
lib.mdStreetGetSuiteRangeOddEven.restype = c_char_p
lib.mdStreetGetSuiteRangeHigh.argtypes = [c_void_p]
lib.mdStreetGetSuiteRangeHigh.restype = c_char_p
lib.mdStreetGetSuiteRangeLow.argtypes = [c_void_p]
lib.mdStreetGetSuiteRangeLow.restype = c_char_p
lib.mdStreetGetSuiteName.argtypes = [c_void_p]
lib.mdStreetGetSuiteName.restype = c_char_p
lib.mdStreetGetPostDirection.argtypes = [c_void_p]
lib.mdStreetGetPostDirection.restype = c_char_p
lib.mdStreetGetSuffix.argtypes = [c_void_p]
lib.mdStreetGetSuffix.restype = c_char_p
lib.mdStreetGetStreetName.argtypes = [c_void_p]
lib.mdStreetGetStreetName.restype = c_char_p
lib.mdStreetGetPreDirection.argtypes = [c_void_p]
lib.mdStreetGetPreDirection.restype = c_char_p
lib.mdStreetGetPrimaryRangeOddEven.argtypes = [c_void_p]
lib.mdStreetGetPrimaryRangeOddEven.restype = c_char_p
lib.mdStreetGetPrimaryRangeHigh.argtypes = [c_void_p]
lib.mdStreetGetPrimaryRangeHigh.restype = c_char_p
lib.mdStreetGetPrimaryRangeLow.argtypes = [c_void_p]
lib.mdStreetGetPrimaryRangeLow.restype = c_char_p

lib.mdZipCreate.argtypes = []
lib.mdZipCreate.restype = c_void_p
lib.mdZipDestroy.argtypes = [c_void_p]
lib.mdZipDestroy.restype = None
lib.mdZipInitialize.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdZipInitialize.restype = c_int
lib.mdZipGetInitializeErrorString.argtypes = [c_void_p]
lib.mdZipGetInitializeErrorString.restype = c_char_p
lib.mdZipGetDatabaseDate.argtypes = [c_void_p]
lib.mdZipGetDatabaseDate.restype = c_char_p
lib.mdZipGetBuildNumber.argtypes = [c_void_p]
lib.mdZipGetBuildNumber.restype = c_char_p
lib.mdZipSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdZipSetLicenseString.restype = c_bool
lib.mdZipGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdZipGetLicenseExpirationDate.restype = c_char_p
lib.mdZipFindZip.argtypes = [c_void_p, c_char_p, c_bool]
lib.mdZipFindZip.restype = c_bool
lib.mdZipFindZipNext.argtypes = [c_void_p]
lib.mdZipFindZipNext.restype = c_bool
lib.mdZipFindZipInCity.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdZipFindZipInCity.restype = c_bool
lib.mdZipFindZipInCityNext.argtypes = [c_void_p]
lib.mdZipFindZipInCityNext.restype = c_bool
lib.mdZipFindCityInState.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdZipFindCityInState.restype = c_bool
lib.mdZipFindCityInStateNext.argtypes = [c_void_p]
lib.mdZipFindCityInStateNext.restype = c_bool
lib.mdZipComputeDistance.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdZipComputeDistance.restype = c_double
lib.mdZipComputeBearing.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdZipComputeBearing.restype = c_double
lib.mdZipGetCountyNameFromFips.argtypes = [c_void_p, c_char_p]
lib.mdZipGetCountyNameFromFips.restype = c_char_p
lib.mdZipGetSCFArea.argtypes = [c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p]
lib.mdZipGetSCFArea.restype = c_int
lib.mdZipGetZip.argtypes = [c_void_p]
lib.mdZipGetZip.restype = c_char_p
lib.mdZipGetCity.argtypes = [c_void_p]
lib.mdZipGetCity.restype = c_char_p
lib.mdZipGetCityAbbreviation.argtypes = [c_void_p]
lib.mdZipGetCityAbbreviation.restype = c_char_p
lib.mdZipGetState.argtypes = [c_void_p]
lib.mdZipGetState.restype = c_char_p
lib.mdZipGetZipType.argtypes = [c_void_p]
lib.mdZipGetZipType.restype = c_char_p
lib.mdZipGetCountyName.argtypes = [c_void_p]
lib.mdZipGetCountyName.restype = c_char_p
lib.mdZipGetCountyFips.argtypes = [c_void_p]
lib.mdZipGetCountyFips.restype = c_char_p
lib.mdZipGetAreaCode.argtypes = [c_void_p]
lib.mdZipGetAreaCode.restype = c_char_p
lib.mdZipGetLongitude.argtypes = [c_void_p]
lib.mdZipGetLongitude.restype = c_char_p
lib.mdZipGetLatitude.argtypes = [c_void_p]
lib.mdZipGetLatitude.restype = c_char_p
lib.mdZipGetTimeZone.argtypes = [c_void_p]
lib.mdZipGetTimeZone.restype = c_char_p
lib.mdZipGetTimeZoneCode.argtypes = [c_void_p]
lib.mdZipGetTimeZoneCode.restype = c_char_p
lib.mdZipGetMsa.argtypes = [c_void_p]
lib.mdZipGetMsa.restype = c_char_p
lib.mdZipGetPmsa.argtypes = [c_void_p]
lib.mdZipGetPmsa.restype = c_char_p
lib.mdZipGetFacilityCode.argtypes = [c_void_p]
lib.mdZipGetFacilityCode.restype = c_char_p
lib.mdZipGetLastLineIndicator.argtypes = [c_void_p]
lib.mdZipGetLastLineIndicator.restype = c_char_p
lib.mdZipGetLastLineNumber.argtypes = [c_void_p]
lib.mdZipGetLastLineNumber.restype = c_char_p
lib.mdZipGetPreferredLastLineNumber.argtypes = [c_void_p]
lib.mdZipGetPreferredLastLineNumber.restype = c_char_p
lib.mdZipGetAutomation.argtypes = [c_void_p]
lib.mdZipGetAutomation.restype = c_char_p
lib.mdZipGetFinanceNumber.argtypes = [c_void_p]
lib.mdZipGetFinanceNumber.restype = c_char_p

class ProgramStatus(Enum):
	"""Programming, installation, and execution error codes returned by Initialize and InitializeDataFiles"""
	ErrorNone = 0
	"""No error - initialization was successful"""
	ErrorOther = 1
	"""Could not open the mdAddr.dat file"""
	ErrorOutOfMemory = 2
	"""Out of memory"""
	ErrorRequiredFileNotFound = 3
	"""A required data file could not be found"""
	ErrorFoundOldFile = 4
	"""Conflicts found between two or more data files"""
	ErrorDatabaseExpired = 5
	"""The database has expired"""
	ErrorLicenseExpired = 6
	"""The license has expired"""

class DiacriticsMode(Enum):
	"""Controls whether diacritic characters are returned in the standardized output, set via SetDiacritics"""
	Auto = 0
	"""If the input value contains diacritic characters, diacritics will be returned in the output. This is the default setting"""
	On = 1
	"""Diacritics will be returned in the output for all addresses, regardless of input"""
	Off = 2
	"""Diacritics will not be returned in the output for any addresses, regardless of input"""

class StandardizeMode(Enum):
	"""Controls how street directionals and suffixes are abbreviated in standardized output, set via SetStandardizationType"""
	ShortFormat = 0
	"""The street address is returned with directionals and suffixes shortened according to postal standards. This is the default setting"""
	LongFormat = 1
	"""The street address is returned with directionals and suffixes spelled out rather than abbreviated"""
	AutoFormat = 2
	"""The street address is returned with the abbreviation or non-abbreviation of the directionals and suffixes preserved. If any of these components need to be corrected and replaced, the replacement will preserve the original standardization"""

class SuiteParseMode(Enum):
	"""Controls whether suite information is parsed into its own field or combined with the address line, set via SetSuiteParseMode"""
	ParseSuite = 0
	"""The suite will be parsed out into the suite field after VerifyAddress(). This is the default setting"""
	CombineSuite = 1
	"""The suite will be appended to the end of the Address1 line after VerifyAddress()"""

class AliasPreserveMode(Enum):
	"""Controls whether nickname or former street name inputs are converted to their USPS preferred name, set via SetAliasMode"""
	ConvertAlias = 0
	"""Nickname or former name street inputs will be converted to their USPS preferred street name during the verification process. This is the default setting"""
	PreserveAlias = 1
	"""Nickname or former name street inputs will be preserved during the verification process"""

class ResultCdDescOpt(Enum):
	"""Controls the verbosity of the description returned by GetResultCodeDescription"""
	ResultCodeDescriptionLong = 0
	"""Return long (detailed) result code descriptions. This is the default setting"""
	ResultCodeDescriptionShort = 1
	"""Return short (brief) result code descriptions"""

class AutoCompletionMode(Enum):
	"""Controls how suite information is presented in GetAutoCompletion suggestions"""
	AutoCompleteSingleSuite = 0
	"""Show each individual suite"""
	AutoCompleteRangedSuite = 1
	"""Show the suite ranges"""
	AutoCompletePlaceHolderSuite = 2
	"""Use a '#' to denote where a suite should go"""
	AutoCompleteNoSuite = 3
	"""Do not show suites"""

class mdAddr(object):
	"""Verifies, standardizes, and enhances U.S. and Canadian addresses

	Provides DPV processing, CASS certification, LACSLink, SuiteLink, and RBDI capabilities
	"""
	def __init__(self):
		"""Constructs a new AddressCheck instance"""
		self.I = lib.mdAddrCreate()

	def __del__(self):
		"""Destroys an existing AddressCheck instance"""
		lib.mdAddrDestroy(self.I)

	def Initialize(self, DataPath, NationalPath, RegionalPath):
		"""Deprecated; use InitializeDataFiles instead. Initializes the data files using explicit file paths
		.. deprecated::
			Use InitializeDataFiles instead.

		Args:
			DataPath: Path to the mdAddr.dat file
			NationalPath: Path to the mdAddr.nat file
			RegionalPath: Path to a regional data file
		Returns:
			ProgramStatus enum - ErrorNone (0) on success; use GetInitializeErrorString to retrieve the nature of any other error
		"""
		return ProgramStatus(lib.mdAddrInitialize(self.I, (DataPath or '').encode('utf-8'), (NationalPath or '').encode('utf-8'), (RegionalPath or '').encode('utf-8')))

	def InitializeDataFiles(self):
		"""Opens the needed data files and prepares Address Object for use. Requires SetPathToUSFiles and/or SetPathToCanadaFiles to have been called first
		Returns:
			ProgramStatus enum - NoError (0) on success; use GetInitializeErrorString to retrieve the nature of any other error
		"""
		return ProgramStatus(lib.mdAddrInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		"""Returns a description of the error from the last InitializeDataFiles call
		Returns:
			Error description string
		"""
		return lib.mdAddrGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, License):
		"""Sets the license string required to enable AddressCheck's complete functionality

		Args:
			License: The software license key
		Returns:
			True (1) if the specified license is correct
		"""
		return lib.mdAddrSetLicenseString(self.I, (License or '').encode('utf-8'))

	def GetBuildNumber(self):
		"""Returns the current development release build number of Address Object
		Returns:
			The current release build number of Address Object
		"""
		return lib.mdAddrGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		"""Returns the date of the US address data files
		Returns:
			The US address database date in the format yyyy-mm-dd
		"""
		return lib.mdAddrGetDatabaseDate(self.I).decode('utf-8')

	def GetExpirationDate(self):
		"""Returns the date when the US address data files will expire
		Returns:
			The US address expiration date in the format yyyy-mm-dd
		"""
		return lib.mdAddrGetExpirationDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		"""Returns the expiration date of the current license string
		Returns:
			The license expiration date in the format yyyy-mm-dd
		"""
		return lib.mdAddrGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetCanadianDatabaseDate(self):
		"""Returns the date of the Canadian address data files
		Returns:
			The Canadian address database date in the format yyyy-mm-dd
		"""
		return lib.mdAddrGetCanadianDatabaseDate(self.I).decode('utf-8')

	def GetCanadianExpirationDate(self):
		"""Returns the date when the Canadian address data files will expire
		Returns:
			The Canadian address expiration date in the format yyyy-mm-dd
		"""
		return lib.mdAddrGetCanadianExpirationDate(self.I).decode('utf-8')

	def SetPathToUSFiles(self, DataFilePath):
		"""Sets the path to the US data files required for US address verification

		Args:
			DataFilePath: Path to directory containing mdAddr.dat, mdAddr.nat, mdAddr.str, and mdAddr.lic
		"""
		lib.mdAddrSetPathToUSFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def SetPathToCanadaFiles(self, DataFilePath):
		"""Sets the path to the Canadian data files required for Canadian address verification

		Args:
			DataFilePath: Path to directory containing mdCanada3.db
		"""
		lib.mdAddrSetPathToCanadaFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def SetPathToDPVDataFiles(self, DataFilePath):
		"""Sets the path to the DPV data files required for CASS processing

		Args:
			DataFilePath: Path to DPV data files (dph.hsa, dph.hsx, dph.hsv, dph.hsf, dph.hsc, dph.dte, lcd)
		"""
		lib.mdAddrSetPathToDPVDataFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def SetPathToLACSLinkDataFiles(self, DataFilePath):
		"""Sets the path to the LACSLink data files required for CASS processing

		Args:
			DataFilePath: Path to directory containing mdLACS.dat
		"""
		lib.mdAddrSetPathToLACSLinkDataFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def SetPathToSuiteLinkDataFiles(self, DataFilePath):
		"""Sets the path to the SuiteLink data files required for CASS processing

		Args:
			DataFilePath: Path to directory containing mdSteLink.dat
		"""
		lib.mdAddrSetPathToSuiteLinkDataFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def SetPathToSuiteFinderDataFiles(self, DataFilePath):
		"""Sets the path to the AddressPlus suite finder data files

		Args:
			DataFilePath: Path to directory containing mdSuiteFinder.db
		"""
		lib.mdAddrSetPathToSuiteFinderDataFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def SetPathToRBDIFiles(self, DataFilePath):
		"""Sets the path to the RBDI (Residential Business Delivery Indicator) data files

		Args:
			DataFilePath: Path to directory containing mdRBDI.dat
		"""
		lib.mdAddrSetPathToRBDIFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def GetRBDIDatabaseDate(self):
		"""Returns the date of the RBDI data files
		Returns:
			RBDI database date string
		"""
		return lib.mdAddrGetRBDIDatabaseDate(self.I).decode('utf-8')

	def SetPathToAddrKeyDataFiles(self, DataFilePath):
		"""Sets the path to the Melissa Address Key (MAK) data files

		Args:
			DataFilePath: Path to the MAK data files
		"""
		lib.mdAddrSetPathToAddrKeyDataFiles(self.I, (DataFilePath or '').encode('utf-8'))

	def ClearProperties(self):
		"""Clears all stored address input and output values before processing the next address
		"""
		lib.mdAddrClearProperties(self.I)

	def ResetDPV(self):
		"""Resets internal DPV counters
		"""
		lib.mdAddrResetDPV(self.I)

	def SetCASSEnable(self, Enable):
		"""Enables or disables full CASS Certified address verification including DPV processing

		Args:
			Enable: Pass 1 to enable CASS processing; 0 to disable (default is disabled)
		"""
		lib.mdAddrSetCASSEnable(self.I, Enable)

	def SetUseUSPSPreferredCityNames(self, Enable):
		"""Forces VerifyAddress to always return the USPS preferred city name regardless of vanity names

		Args:
			Enable: Pass 1 to always return the USPS preferred city name
		"""
		lib.mdAddrSetUseUSPSPreferredCityNames(self.I, Enable)

	def SetDiacritics(self, mode):
		"""Sets how diacritic characters are handled for Quebec addresses

		Args:
			mode: DiacriticsMode enum - Auto (0), On (1), or Off (2)
		"""
		lib.mdAddrSetDiacritics(self.I, DiacriticsMode(mode).value)

	def GetStatusCode(self):
		"""Returns the status code from the last VerifyAddress call
		.. deprecated::
			Use GetResults instead.
		Returns:
			Status code string
		"""
		return lib.mdAddrGetStatusCode(self.I).decode('utf-8')

	def GetErrorCode(self):
		"""Returns the error code from the last VerifyAddress call
		.. deprecated::
			Use GetResults instead.
		Returns:
			Error code string
		"""
		return lib.mdAddrGetErrorCode(self.I).decode('utf-8')

	def GetErrorString(self):
		"""Returns a description of the error from the last VerifyAddress call
		.. deprecated::
			Use GetResults instead.
		Returns:
			Error description string
		"""
		return lib.mdAddrGetErrorString(self.I).decode('utf-8')

	def GetResults(self):
		"""Returns a comma-delimited list of result codes describing the outcome of the last VerifyAddress call
		Returns:
			Comma-delimited result code string (e.g. "AS01" for a fully verified address)
		"""
		return lib.mdAddrGetResults(self.I).decode('utf-8')

	def GetResultCodeDescription(self, resultCode, opt=0):
		"""Returns a human-readable description for a given result code

		Args:
			resultCode: The four-character result code to look up
			opt: ResultCdDescOpt enum specifying description format (default is long)
		Returns:
			Description of the result code
		"""
		return lib.mdAddrGetResultCodeDescription(self.I, (resultCode or '').encode('utf-8'), ResultCdDescOpt(opt).value).decode('utf-8')

	def SetPS3553_B1_ProcessorName(self, ProcessorName):
		"""Sets the name of the company that processed the address list for CASS Form 3553 item B1

		Args:
			ProcessorName: Company name that coded the address list
		"""
		lib.mdAddrSetPS3553_B1_ProcessorName(self.I, (ProcessorName or '').encode('utf-8'))

	def SetPS3553_B4_ListName(self, ListName):
		"""Sets the name or ID of the address list for CASS Form 3553 item B4

		Args:
			ListName: List name or ID number (prefix IDs with "ID#")
		"""
		lib.mdAddrSetPS3553_B4_ListName(self.I, (ListName or '').encode('utf-8'))

	def SetPS3553_D3_Name(self, Name):
		"""Sets the list owner's name for CASS Form 3553 item D3

		Args:
			Name: Name of the list owner
		"""
		lib.mdAddrSetPS3553_D3_Name(self.I, (Name or '').encode('utf-8'))

	def SetPS3553_D3_Company(self, Company):
		"""Sets the list owner's company name for CASS Form 3553 item D3

		Args:
			Company: Company name of the list owner
		"""
		lib.mdAddrSetPS3553_D3_Company(self.I, (Company or '').encode('utf-8'))

	def SetPS3553_D3_Address(self, Address):
		"""Sets the list owner's street address for CASS Form 3553 item D3

		Args:
			Address: Street address of the list owner
		"""
		lib.mdAddrSetPS3553_D3_Address(self.I, (Address or '').encode('utf-8'))

	def SetPS3553_D3_City(self, City):
		"""Sets the list owner's city for CASS Form 3553 item D3

		Args:
			City: City of the list owner
		"""
		lib.mdAddrSetPS3553_D3_City(self.I, (City or '').encode('utf-8'))

	def SetPS3553_D3_State(self, State):
		"""Sets the list owner's state for CASS Form 3553 item D3

		Args:
			State: State of the list owner
		"""
		lib.mdAddrSetPS3553_D3_State(self.I, (State or '').encode('utf-8'))

	def SetPS3553_D3_ZIP(self, ZIP):
		"""Sets the list owner's ZIP code for CASS Form 3553 item D3

		Args:
			ZIP: ZIP code of the list owner
		"""
		lib.mdAddrSetPS3553_D3_ZIP(self.I, (ZIP or '').encode('utf-8'))

	def GetFormPS3553(self):
		"""Returns the CASS Form 3553 as an HTML string for display or printing
		Returns:
			HTML string of the CASS Form 3553
		"""
		return lib.mdAddrGetFormPS3553(self.I).decode('utf-8')

	def SaveFormPS3553(self, PathAndFileName):
		"""Saves the CASS Form 3553 as an HTML or PDF file

		Args:
			PathAndFileName: Full path and filename including .html or .pdf extension
		Returns:
			True (1) if saved successfully
		"""
		return lib.mdAddrSaveFormPS3553(self.I, (PathAndFileName or '').encode('utf-8'))

	def ResetFormPS3553(self):
		"""Resets all internal counters to zero, useful when producing several CASS forms in sequence for multiple jobs. Removing Address Object from memory also clears the counters
		"""
		lib.mdAddrResetFormPS3553(self.I)

	def ResetFormPS3553Counter(self):
		"""Resets only the CASS Form 3553 record counter
		"""
		lib.mdAddrResetFormPS3553Counter(self.I)

	def SetStandardizationType(self, mode):
		"""Sets how address suffixes and directionals are abbreviated in standardized output

		Args:
			mode: StandardizeMode enum - ShortFormat (0), LongFormat (1), or AutoFormat (2)
		"""
		lib.mdAddrSetStandardizationType(self.I, StandardizeMode(mode).value)

	def SetSuiteParseMode(self, mode):
		"""Controls whether suite information is parsed into its own field or appended to the address line

		Args:
			mode: SuiteParseMode enum - ParseSuite (default) or CombineSuite
		"""
		lib.mdAddrSetSuiteParseMode(self.I, SuiteParseMode(mode).value)

	def SetAliasMode(self, mode):
		"""Controls whether street alias or nickname names are converted to the USPS preferred name or preserved

		Args:
			mode: AliasPreserveMode enum - ConvertAlias (default) or PreserveAlias
		"""
		lib.mdAddrSetAliasMode(self.I, AliasPreserveMode(mode).value)

	def GetFormSOA(self):
		"""Returns the Canada Post Summary of Addresses as an HTML string
		Returns:
			HTML string of the Summary of Addresses
		"""
		return lib.mdAddrGetFormSOA(self.I).decode('utf-8')

	def SaveFormSOA(self, PathAndFileName):
		"""Saves the Canada Post Summary of Addresses to an HTML file

		Args:
			PathAndFileName: Full path and filename including .html extension
		"""
		lib.mdAddrSaveFormSOA(self.I, (PathAndFileName or '').encode('utf-8'))

	def ResetFormSOA(self):
		"""Resets the SOA running totals for Canadian address records
		"""
		lib.mdAddrResetFormSOA(self.I)

	def SetSOACustomerInfo(self, customerName, customerAddress):
		"""Sets the company name and mailing address for the Canada Post Summary of Addresses

		Args:
			customerName: Company name as it appears on the Canada Post contract
			customerAddress: Mailing address as it appears on the Canada Post contract
		"""
		lib.mdAddrSetSOACustomerInfo(self.I, (customerName or '').encode('utf-8'), (customerAddress or '').encode('utf-8'))

	def SetSOACPCNumber(self, CPCNumber):
		"""Sets the Canada Post Contract (CPC) number for the Summary of Addresses

		Args:
			CPCNumber: Eight-digit Canada Post contract number
		"""
		lib.mdAddrSetSOACPCNumber(self.I, (CPCNumber or '').encode('utf-8'))

	def GetSOACustomerInfo(self):
		"""Returns the company name and mailing address set via SetSOACustomerInfo for the Summary of Addresses
		Returns:
			Customer name and address string
		"""
		return lib.mdAddrGetSOACustomerInfo(self.I).decode('utf-8')

	def GetSOACPCNumber(self):
		"""Returns the Canada Post Contract (CPC) number set via SetSOACPCNumber for the Summary of Addresses
		Returns:
			CPC number string
		"""
		return lib.mdAddrGetSOACPCNumber(self.I).decode('utf-8')

	def GetSOATotalRecords(self):
		"""Returns the total number of Canadian address records processed since initialization or last reset
		Returns:
			Total record count
		"""
		return lib.mdAddrGetSOATotalRecords(self.I)

	def GetSOAAAPercentage(self):
		"""Returns the address accuracy percentage for Canadian records processed
		Returns:
			Address accuracy percentage (must be 95% or higher for postage discounts)
		"""
		return lib.mdAddrGetSOAAAPercentage(self.I)

	def GetSOAAAExpiryDate(self):
		"""Returns the expiry date of the current Summary of Addresses
		Returns:
			SOA expiry date string
		"""
		return lib.mdAddrGetSOAAAExpiryDate(self.I).decode('utf-8')

	def GetSOASoftwareInfo(self):
		"""Returns the software name and build number shown on the Summary of Addresses
		Returns:
			Software name and version string
		"""
		return lib.mdAddrGetSOASoftwareInfo(self.I).decode('utf-8')

	def GetSOAErrorString(self):
		"""Returns an error description generated by any SOA function call
		Returns:
			SOA error description string
		"""
		return lib.mdAddrGetSOAErrorString(self.I).decode('utf-8')

	def SetCompany(self, Company):
		"""Sets the company name for the address to be verified

		Args:
			Company: Optional company name; improves Plus4 accuracy and enables SuiteLink for firm addresses
		"""
		lib.mdAddrSetCompany(self.I, (Company or '').encode('utf-8'))

	def SetLastName(self, LastName):
		"""Sets the last name associated with a residential address (required for AddressPlus)

		Args:
			LastName: Last name associated with the address
		"""
		lib.mdAddrSetLastName(self.I, (LastName or '').encode('utf-8'))

	def SetAddress(self, Address):
		"""Sets the primary delivery address line to be verified

		Args:
			Address: Street address including number, name, directionals, and suffix
		"""
		lib.mdAddrSetAddress(self.I, (Address or '').encode('utf-8'))

	def SetAddress2(self, Address2):
		"""Sets a secondary address line such as a PO Box or suite on a separate line

		Args:
			Address2: Secondary address line
		"""
		lib.mdAddrSetAddress2(self.I, (Address2 or '').encode('utf-8'))

	def SetLastLine(self, LastLine):
		"""Sets the city, state, and ZIP code as a single combined string

		Args:
			LastLine: Combined city, state, and ZIP string (e.g. "Rancho Santa Margarita, CA 92688")
		"""
		lib.mdAddrSetLastLine(self.I, (LastLine or '').encode('utf-8'))

	def SetSuite(self, Suite):
		"""Sets the suite name and number for the address to be verified

		Args:
			Suite: Suite designation (e.g. "Apt 3" or "Ste 100")
		"""
		lib.mdAddrSetSuite(self.I, (Suite or '').encode('utf-8'))

	def SetCity(self, City):
		"""Sets the city or municipality name for the address to be verified

		Args:
			City: City or municipality name
		"""
		lib.mdAddrSetCity(self.I, (City or '').encode('utf-8'))

	def SetState(self, State):
		"""Sets the two-letter state or province abbreviation for the address to be verified

		Args:
			State: Two-letter state or province abbreviation
		"""
		lib.mdAddrSetState(self.I, (State or '').encode('utf-8'))

	def SetZip(self, Zip):
		"""Sets the five-digit US ZIP code or six-character Canadian postal code for the address to be verified

		Args:
			Zip: US ZIP code or Canadian postal code
		"""
		lib.mdAddrSetZip(self.I, (Zip or '').encode('utf-8'))

	def SetPlus4(self, Plus4):
		"""Sets the four-digit ZIP+4 add-on code for the address to be verified

		Args:
			Plus4: Four-digit ZIP+4 extension
		"""
		lib.mdAddrSetPlus4(self.I, (Plus4 or '').encode('utf-8'))

	def SetUrbanization(self, Urbanization):
		"""Sets the urbanization name for Puerto Rican addresses

		Args:
			Urbanization: Puerto Rico urbanization (neighborhood) name
		"""
		lib.mdAddrSetUrbanization(self.I, (Urbanization or '').encode('utf-8'))

	def SetParsedAddressRange(self, AddressRange):
		"""Sets the pre-parsed delivery number portion of the street address

		Args:
			AddressRange: Numeric address range (max 10 characters)
		"""
		lib.mdAddrSetParsedAddressRange(self.I, (AddressRange or '').encode('utf-8'))

	def SetParsedPreDirection(self, PreDirection):
		"""Sets the pre-parsed directional that precedes the street name

		Args:
			PreDirection: Pre-directional (e.g. "N", "NE", "SW")
		"""
		lib.mdAddrSetParsedPreDirection(self.I, (PreDirection or '').encode('utf-8'))

	def SetParsedStreetName(self, StreetName):
		"""Sets the pre-parsed street name portion of the address

		Args:
			StreetName: Street name (max 28 characters)
		"""
		lib.mdAddrSetParsedStreetName(self.I, (StreetName or '').encode('utf-8'))

	def SetParsedSuffix(self, Suffix):
		"""Sets the pre-parsed street suffix portion of the address

		Args:
			Suffix: Street suffix (e.g. "ST", "AVE", "BLVD")
		"""
		lib.mdAddrSetParsedSuffix(self.I, (Suffix or '').encode('utf-8'))

	def SetParsedPostDirection(self, PostDirection):
		"""Sets the pre-parsed directional that follows the street name

		Args:
			PostDirection: Post-directional (e.g. "N", "NE", "SW")
		"""
		lib.mdAddrSetParsedPostDirection(self.I, (PostDirection or '').encode('utf-8'))

	def SetParsedSuiteName(self, SuiteName):
		"""Sets the pre-parsed secondary unit designator (e.g. "APT", "STE", "UNIT")

		Args:
			SuiteName: Secondary unit designator
		"""
		lib.mdAddrSetParsedSuiteName(self.I, (SuiteName or '').encode('utf-8'))

	def SetParsedSuiteRange(self, SuiteRange):
		"""Sets the pre-parsed secondary unit number

		Args:
			SuiteRange: Secondary unit number
		"""
		lib.mdAddrSetParsedSuiteRange(self.I, (SuiteRange or '').encode('utf-8'))

	def SetParsedRouteService(self, RouteService):
		"""Sets the pre-parsed route service for Canadian addresses (equivalent to US rural route)

		Args:
			RouteService: Canadian route service information
		"""
		lib.mdAddrSetParsedRouteService(self.I, (RouteService or '').encode('utf-8'))

	def SetParsedLockBox(self, LockBox):
		"""Sets the pre-parsed lock box for Canadian addresses (equivalent to US PO Box)

		Args:
			LockBox: Canadian lock box information
		"""
		lib.mdAddrSetParsedLockBox(self.I, (LockBox or '').encode('utf-8'))

	def SetParsedDeliveryInstallation(self, DeliveryInstallation):
		"""Sets the pre-parsed delivery installation for Canadian addresses

		Args:
			DeliveryInstallation: Canadian delivery installation (post office facility)
		"""
		lib.mdAddrSetParsedDeliveryInstallation(self.I, (DeliveryInstallation or '').encode('utf-8'))

	def SetCountryCode(self, CountryCode):
		"""Sets the two-character country code for the address to be verified

		Args:
			CountryCode: Two-character country code ("US" or "CA")
		"""
		lib.mdAddrSetCountryCode(self.I, (CountryCode or '').encode('utf-8'))

	def VerifyAddress(self):
		"""Verifies, standardizes, and enhances the address set via the Set functions
		Returns:
			True (1) if the address was successfully coded; check GetResults for match level
		"""
		return lib.mdAddrVerifyAddress(self.I)

	def GetCompany(self):
		"""Returns the company name associated with the verified address
		Returns:
			Company name string (unchanged from input)
		"""
		return lib.mdAddrGetCompany(self.I).decode('utf-8')

	def GetLastName(self):
		"""Returns the last name associated with the verified address
		Returns:
			Last name string (unchanged from input)
		"""
		return lib.mdAddrGetLastName(self.I).decode('utf-8')

	def GetAddress(self):
		"""Returns the standardized primary delivery address line
		Returns:
			Standardized street address string
		"""
		return lib.mdAddrGetAddress(self.I).decode('utf-8')

	def GetAddress2(self):
		"""Returns the second address line associated with the verified address
		Returns:
			Second address line string
		"""
		return lib.mdAddrGetAddress2(self.I).decode('utf-8')

	def GetSuite(self):
		"""Returns the standardized suite name and number
		Returns:
			Suite string (e.g. "APT 3")
		"""
		return lib.mdAddrGetSuite(self.I).decode('utf-8')

	def GetCity(self):
		"""Returns the verified city or municipality name
		Returns:
			City name string
		"""
		return lib.mdAddrGetCity(self.I).decode('utf-8')

	def GetCityAbbreviation(self):
		"""Returns the official USPS 13-character city name abbreviation
		Returns:
			City abbreviation (same as city name if 13 characters or fewer)
		"""
		return lib.mdAddrGetCityAbbreviation(self.I).decode('utf-8')

	def GetState(self):
		"""Returns the two-letter state or province abbreviation for the verified address
		Returns:
			Two-letter state or province code
		"""
		return lib.mdAddrGetState(self.I).decode('utf-8')

	def GetZip(self):
		"""Returns the verified five-digit US ZIP code or six-character Canadian postal code
		Returns:
			ZIP or postal code string
		"""
		return lib.mdAddrGetZip(self.I).decode('utf-8')

	def GetPlus4(self):
		"""Returns the four-digit ZIP+4 add-on code for the verified address
		Returns:
			Four-digit Plus4 string
		"""
		return lib.mdAddrGetPlus4(self.I).decode('utf-8')

	def GetCarrierRoute(self):
		"""Returns the four-character carrier route code for the verified address
		Returns:
			Carrier route code (e.g. "C027" or "R001")
		"""
		return lib.mdAddrGetCarrierRoute(self.I).decode('utf-8')

	def GetDeliveryPointCode(self):
		"""Returns the two-digit delivery point code used in POSTNET barcodes (positions 10-11)
		Returns:
			Two-digit delivery point code string
		"""
		return lib.mdAddrGetDeliveryPointCode(self.I).decode('utf-8')

	def GetDeliveryPointCheckDigit(self):
		"""Returns the one-digit check digit for POSTNET barcodes (position 12)
		Returns:
			One-digit check digit string
		"""
		return lib.mdAddrGetDeliveryPointCheckDigit(self.I).decode('utf-8')

	def GetCountyFips(self):
		"""Returns the five-digit county FIPS code for the verified address
		Returns:
			Five-digit FIPS code (e.g. "06037" for Los Angeles CA)
		"""
		return lib.mdAddrGetCountyFips(self.I).decode('utf-8')

	def GetCountyName(self):
		"""Returns the county name for the verified address
		Returns:
			County name string (up to 25 characters)
		"""
		return lib.mdAddrGetCountyName(self.I).decode('utf-8')

	def GetAddressTypeCode(self):
		"""Returns a single-character code indicating the type of the verified address
		Returns:
			S=Street, P=PO Box, H=High Rise, R=Rural Route, F=Firm, G=General Delivery, A=Alias
		"""
		return lib.mdAddrGetAddressTypeCode(self.I).decode('utf-8')

	def GetAddressTypeString(self):
		"""Returns a description of the address type code returned by GetAddressTypeCode
		Returns:
			Address type description string
		"""
		return lib.mdAddrGetAddressTypeString(self.I).decode('utf-8')

	def GetUrbanization(self):
		"""Returns the urbanization name for Puerto Rican addresses
		Returns:
			Urbanization name string
		"""
		return lib.mdAddrGetUrbanization(self.I).decode('utf-8')

	def GetCongressionalDistrict(self):
		"""Returns the congressional district for the verified address
		Returns:
			State abbreviation plus two-digit district number (e.g. "CA01")
		"""
		return lib.mdAddrGetCongressionalDistrict(self.I).decode('utf-8')

	def GetLACS(self):
		"""Returns whether the address has undergone a rural-to-city-style address conversion
		Returns:
			"L" if the address was converted, empty if not
		"""
		return lib.mdAddrGetLACS(self.I).decode('utf-8')

	def GetLACSLinkIndicator(self):
		"""Returns whether the submitted address was corrected using LACSLink data
		Returns:
			"Y" if updated, "S" if updated but suite unmatched, "N" if not updated
		"""
		return lib.mdAddrGetLACSLinkIndicator(self.I).decode('utf-8')

	def GetPrivateMailbox(self):
		"""Returns the private mailbox number for CMRA addresses
		Returns:
			Private mailbox number string
		"""
		return lib.mdAddrGetPrivateMailbox(self.I).decode('utf-8')

	def GetTimeZoneCode(self):
		"""Returns the numeric time zone code for the verified address
		Returns:
			Time zone code (e.g. "5" for Eastern, "8" for Pacific)
		"""
		return lib.mdAddrGetTimeZoneCode(self.I).decode('utf-8')

	def GetTimeZone(self):
		"""Returns the time zone name for the verified address
		Returns:
			Time zone name string (e.g. "Eastern Time", "Pacific Time")
		"""
		return lib.mdAddrGetTimeZone(self.I).decode('utf-8')

	def GetMsa(self):
		"""Returns the Metropolitan Statistical Area (MSA) code for the verified address
		Returns:
			MSA code string
		"""
		return lib.mdAddrGetMsa(self.I).decode('utf-8')

	def GetPmsa(self):
		"""Returns the Primary Metropolitan Statistical Area (PMSA) code for the verified address
		Returns:
			PMSA code string
		"""
		return lib.mdAddrGetPmsa(self.I).decode('utf-8')

	def GetDefaultFlagIndicator(self):
		"""Returns whether a default Plus4 code was assigned during address verification
		Returns:
			Default flag indicator string
		"""
		return lib.mdAddrGetDefaultFlagIndicator(self.I).decode('utf-8')

	def GetSuiteStatus(self):
		"""Returns the SuiteLink suite status indicator for the verified address
		Returns:
			Suite status string
		"""
		return lib.mdAddrGetSuiteStatus(self.I).decode('utf-8')

	def GetEWSFlag(self):
		"""Returns whether the address was found in the Early Warning System (EWS) database. Only returns a value if EnableEarlyWarningSystem was set to true and ews.txt is present in the data files folder
		Returns:
			"Y" if found in EWS (GetResults also returns "AE06"), empty otherwise
		"""
		return lib.mdAddrGetEWSFlag(self.I).decode('utf-8')

	def GetCMRA(self):
		"""Returns whether the address is a private mailbox at a Commercial Mail Receiving Agency (e.g. UPS Store). Does not return data when GetResults returns "AS03" (non-USPS address)
		Returns:
			"N" if not a CMRA, "Y" if a CMRA, empty if not populated (e.g. certain DPV footnote codes)
		"""
		return lib.mdAddrGetCMRA(self.I).decode('utf-8')

	def GetDsfVacant(self):
		"""Returns whether the delivery point is currently vacant
		Returns:
			"Y" if vacant (unoccupied over 90 days), "N" if not vacant
		"""
		return lib.mdAddrGetDsfVacant(self.I).decode('utf-8')

	def GetCountryCode(self):
		"""Returns the two-character country code for the verified address
		Returns:
			"US" for United States, "CA" for Canada
		"""
		return lib.mdAddrGetCountryCode(self.I).decode('utf-8')

	def GetZipType(self):
		"""Returns the ZIP code type for the verified address
		Returns:
			"P" for PO Box only, "U" for unique/institutional, "M" for military, empty for standard
		"""
		return lib.mdAddrGetZipType(self.I).decode('utf-8')

	def GetFalseTable(self):
		"""Returns whether the address appears in the DPV false positive table
		Returns:
			False positive table indicator string
		"""
		return lib.mdAddrGetFalseTable(self.I).decode('utf-8')

	def GetDPVFootnotes(self):
		"""Returns the USPS standard DPV footnote codes for the verified address
		Returns:
			String of up to 6 DPV footnote codes
		"""
		return lib.mdAddrGetDPVFootnotes(self.I).decode('utf-8')

	def GetLACSLinkReturnCode(self):
		"""Returns the LACSLink match result code
		Returns:
			"A" for match, "00" for no match, "14" for unconvertible, "92" for secondary dropped
		"""
		return lib.mdAddrGetLACSLinkReturnCode(self.I).decode('utf-8')

	def GetSuiteLinkReturnCode(self):
		"""Returns the SuiteLink match result code indicating whether suite information was appended
		Returns:
			"A" if suite matched and appended, "00" if no match
		"""
		return lib.mdAddrGetSuiteLinkReturnCode(self.I).decode('utf-8')

	def GetRBDI(self):
		"""Returns the Residential Business Delivery Indicator for the verified address
		Returns:
			"R" for residential, "B" for business, "U" for unknown
		"""
		return lib.mdAddrGetRBDI(self.I).decode('utf-8')

	def GetELotNumber(self):
		"""Returns the enhanced Line-of-Travel (eLOT) sequence number for the verified address
		Returns:
			eLOT number string, or "-1" if eLOT data is unavailable
		"""
		return lib.mdAddrGetELotNumber(self.I).decode('utf-8')

	def GetELotOrder(self):
		"""Returns the eLOT delivery direction indicator
		Returns:
			"A" for ascending delivery order, "D" for descending, "X" if unavailable
		"""
		return lib.mdAddrGetELotOrder(self.I).decode('utf-8')

	def GetAddressKey(self):
		"""Returns the unique 11-digit USPS address key for the verified address
		Returns:
			11-digit address key string
		"""
		return lib.mdAddrGetAddressKey(self.I).decode('utf-8')

	def GetMelissaAddressKey(self):
		"""Returns the Melissa Address Key (MAK), a persistent 10-digit unique identifier for the address
		Returns:
			10-digit MAK string
		"""
		return lib.mdAddrGetMelissaAddressKey(self.I).decode('utf-8')

	def GetMelissaAddressKeyBase(self):
		"""Returns the Melissa Address Key Base (BaseMAK), linking suite addresses to their parent building
		Returns:
			10-digit BaseMAK string
		"""
		return lib.mdAddrGetMelissaAddressKeyBase(self.I).decode('utf-8')

	def GetOutputParameter(self, ParameterName):
		"""Returns the value of a named output parameter after a call to VerifyAddress

		Args:
			ParameterName: Parameter name defined by header macros: "CMRA", "PBSA", "Vacant", "ZipIncludedIn3553", "DropIndicator", "ThrowBack", "DeliveryDays", "NoStatIndicator", "NoStatReasonCode", "DPVConfirmationCode", "EnhancedDPVCode", "NoSecureLocation", "DoorNotAccessible", "FalseTable", "RDI", "CongressionalDistrict"
		Returns:
			Parameter value string
		"""
		return lib.mdAddrGetOutputParameter(self.I, (ParameterName or '').encode('utf-8')).decode('utf-8')

	def SetInputParameter(self, ParameterName, Value):
		"""Sets a named input parameter before calling VerifyAddress

		Args:
			ParameterName: Parameter name defined by header macros: "EnableRDI", "CASSTest", "TotalDPS", "UsePostalCongressionalDistricts"
			Value: Parameter value string
		Returns:
			0 on success
		"""
		return lib.mdAddrSetInputParameter(self.I, (ParameterName or '').encode('utf-8'), (Value or '').encode('utf-8'))

	def FindSuggestion(self):
		"""Returns the first suggested address when VerifyAddress could not verify the submitted address
		Returns:
			True (1) if a suggestion was found
		"""
		return lib.mdAddrFindSuggestion(self.I)

	def FindSuggestionNext(self):
		"""Returns the next suggested address after a successful call to FindSuggestion
		Returns:
			True (1) if another suggestion was found, false (0) if no more suggestions
		"""
		return lib.mdAddrFindSuggestionNext(self.I)

	def GetDsfNoStats(self):
		"""Returns the DSF (Delivery Sequence File) no-stats indicator for the verified address
		Returns:
			DSF no-stats indicator string
		"""
		return lib.mdAddrGetDsfNoStats(self.I).decode('utf-8')

	def GetDsfDNA(self):
		"""Returns the DSF Do Not Address indicator for the verified address
		Returns:
			DSF DNA indicator string
		"""
		return lib.mdAddrGetDsfDNA(self.I).decode('utf-8')

	def GetPS3553_B6_TotalRecords(self):
		"""Returns the total number of address records verified since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 item B6)
		Returns:
			Total verified record count (integer)
		"""
		return lib.mdAddrGetPS3553_B6_TotalRecords(self.I)

	def GetPS3553_C1a_ZIP4Coded(self):
		"""Returns the count of records matched to the ZIP+4 level since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 item C1a)
		Returns:
			ZIP+4 coded record count (integer)
		"""
		return lib.mdAddrGetPS3553_C1a_ZIP4Coded(self.I)

	def GetPS3553_C1c_DPBCAssigned(self):
		"""Returns the count of records assigned a Delivery Point Bar Code since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 item C1c)
		Returns:
			DPBC assigned record count (integer)
		"""
		return lib.mdAddrGetPS3553_C1c_DPBCAssigned(self.I)

	def GetPS3553_C1d_FiveDigitCoded(self):
		"""Returns the count of records verified to the five-digit carrier route level since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 item C1d)
		Returns:
			Five-digit coded record count (integer)
		"""
		return lib.mdAddrGetPS3553_C1d_FiveDigitCoded(self.I)

	def GetPS3553_C1e_CRRTCoded(self):
		"""Returns the count of records verified to the carrier route level since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 item C1e)
		Returns:
			Carrier route coded record count (integer)
		"""
		return lib.mdAddrGetPS3553_C1e_CRRTCoded(self.I)

	def GetPS3553_C1f_eLOTAssigned(self):
		"""Returns the count of records assigned an enhanced Line of Travel (eLOT) sequence number since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 item C1f)
		Returns:
			eLOT assigned record count (integer)
		"""
		return lib.mdAddrGetPS3553_C1f_eLOTAssigned(self.I)

	def GetPS3553_E_HighRiseDefault(self):
		"""Returns the count of high-rise records default matched (matched at the street address level but not to a valid secondary address) since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			High-rise default match count (integer)
		"""
		return lib.mdAddrGetPS3553_E_HighRiseDefault(self.I)

	def GetPS3553_E_HighRiseExact(self):
		"""Returns the count of high-rise records exactly matched to both a primary and secondary address since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			High-rise exact match count (integer)
		"""
		return lib.mdAddrGetPS3553_E_HighRiseExact(self.I)

	def GetPS3553_E_RuralRouteDefault(self):
		"""Returns the count of rural route records default matched (verified at the route number level but not to a valid primary range) since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			Rural route default match count (integer)
		"""
		return lib.mdAddrGetPS3553_E_RuralRouteDefault(self.I)

	def GetPS3553_E_RuralRouteExact(self):
		"""Returns the count of rural route records verified at the route number level and matched to a valid primary range, since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			Rural route exact match count (integer)
		"""
		return lib.mdAddrGetPS3553_E_RuralRouteExact(self.I)

	def GetZip4HRDefault(self):
		"""Returns the count of high-rise records default matched at the ZIP+4 level, since the current instance was created or the last ResetFormPS3553 call
		Returns:
			ZIP+4 high-rise default match count (integer)
		"""
		return lib.mdAddrGetZip4HRDefault(self.I)

	def GetZip4HRExact(self):
		"""Returns the count of high-rise records exactly matched at the ZIP+4 level, since the current instance was created or the last ResetFormPS3553 call
		Returns:
			ZIP+4 high-rise exact match count (integer)
		"""
		return lib.mdAddrGetZip4HRExact(self.I)

	def GetZip4RRDefault(self):
		"""Returns the count of rural route records default matched at the ZIP+4 level, since the current instance was created or the last ResetFormPS3553 call
		Returns:
			ZIP+4 rural route default match count (integer)
		"""
		return lib.mdAddrGetZip4RRDefault(self.I)

	def GetZip4RRExact(self):
		"""Returns the count of rural route records exactly matched at the ZIP+4 level, since the current instance was created or the last ResetFormPS3553 call
		Returns:
			ZIP+4 rural route exact match count (integer)
		"""
		return lib.mdAddrGetZip4RRExact(self.I)

	def GetPS3553_E_LACSCount(self):
		"""Returns the count of records flagged as having undergone a rural-to-city-style address conversion since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			LACS record count (integer)
		"""
		return lib.mdAddrGetPS3553_E_LACSCount(self.I)

	def GetPS3553_E_EWSCount(self):
		"""Returns the count of records that did not appear in the current USPS ZIP+4 file but were valid addresses, since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			EWS record count (integer)
		"""
		return lib.mdAddrGetPS3553_E_EWSCount(self.I)

	def GetPS3553_E_DPVCount(self):
		"""Returns the count of records confirmed via DPV since the current instance was created or the last ResetFormPS3553 call (CASS Form 3553 section E)
		Returns:
			DPV confirmed record count (integer)
		"""
		return lib.mdAddrGetPS3553_E_DPVCount(self.I)

	def GetPS3553_X_POBoxCount(self):
		"""Returns the count of PO Box address records verified since the current instance was created or the last ResetFormPS3553 call
		Returns:
			PO Box record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_POBoxCount(self.I)

	def GetPS3553_X_HCExactCount(self):
		"""Returns the count of Highway Contract route records exactly matched since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Highway Contract exact match count (integer)
		"""
		return lib.mdAddrGetPS3553_X_HCExactCount(self.I)

	def GetPS3553_X_FirmCount(self):
		"""Returns the count of firm/company address records verified since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Firm record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_FirmCount(self.I)

	def GetPS3553_X_GenDeliveryCount(self):
		"""Returns the count of General Delivery address records verified since the current instance was created or the last ResetFormPS3553 call
		Returns:
			General Delivery record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_GenDeliveryCount(self.I)

	def GetPS3553_X_MilitaryZipCount(self):
		"""Returns the count of military ZIP code address records verified since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Military ZIP record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_MilitaryZipCount(self.I)

	def GetPS3553_X_NonDeliveryCount(self):
		"""Returns the count of non-deliverable address records since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Non-delivery record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_NonDeliveryCount(self.I)

	def GetPS3553_X_StreetCount(self):
		"""Returns the count of street-level address records verified since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Street record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_StreetCount(self.I)

	def GetPS3553_X_HCDefaultCount(self):
		"""Returns the count of Highway Contract route records default matched since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Highway Contract default match count (integer)
		"""
		return lib.mdAddrGetPS3553_X_HCDefaultCount(self.I)

	def GetPS3553_X_OtherCount(self):
		"""Returns the count of address records not falling into any standard category, since the current instance was created or the last ResetFormPS3553 call
		Returns:
			Other record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_OtherCount(self.I)

	def GetPS3553_X_LacsLinkCodeACount(self):
		"""Returns the count of records with LACSLink Code A (successful match and conversion), since the current instance was created or the last ResetFormPS3553 call
		Returns:
			LACSLink Code A count (integer)
		"""
		return lib.mdAddrGetPS3553_X_LacsLinkCodeACount(self.I)

	def GetPS3553_X_LacsLinkCode00Count(self):
		"""Returns the count of records with LACSLink Code 00 (no match found), since the current instance was created or the last ResetFormPS3553 call
		Returns:
			LACSLink Code 00 count (integer)
		"""
		return lib.mdAddrGetPS3553_X_LacsLinkCode00Count(self.I)

	def GetPS3553_X_LacsLinkCode14Count(self):
		"""Returns the count of records with LACSLink Code 14 (new address would not convert), since the current instance was created or the last ResetFormPS3553 call
		Returns:
			LACSLink Code 14 count (integer)
		"""
		return lib.mdAddrGetPS3553_X_LacsLinkCode14Count(self.I)

	def GetPS3553_X_LacsLinkCode92Count(self):
		"""Returns the count of records with LACSLink Code 92 (secondary number dropped during conversion), since the current instance was created or the last ResetFormPS3553 call
		Returns:
			LACSLink Code 92 count (integer)
		"""
		return lib.mdAddrGetPS3553_X_LacsLinkCode92Count(self.I)

	def GetPS3553_X_LacsLinkCode09Count(self):
		"""Returns the count of records with LACSLink Code 09, since the current instance was created or the last ResetFormPS3553 call
		Returns:
			LACSLink Code 09 count (integer)
		"""
		return lib.mdAddrGetPS3553_X_LacsLinkCode09Count(self.I)

	def GetPS3553_X_SuiteLinkCodeACount(self):
		"""Returns the count of address records with suite information appended via SuiteLink (Code A), since the current instance was created or the last ResetFormPS3553 call
		Returns:
			SuiteLink Code A record count (integer)
		"""
		return lib.mdAddrGetPS3553_X_SuiteLinkCodeACount(self.I)

	def GetPS3553_X_SuiteLinkCode00Count(self):
		"""Returns the count of records with SuiteLink Code 00 (no suite match), since the current instance was created or the last ResetFormPS3553 call
		Returns:
			SuiteLink Code 00 count (integer)
		"""
		return lib.mdAddrGetPS3553_X_SuiteLinkCode00Count(self.I)

	def GetParsedAddressRange(self):
		"""Returns the numeric delivery number from the verified street address
		Returns:
			Address range string (max 10 characters)
		"""
		return lib.mdAddrGetParsedAddressRange(self.I).decode('utf-8')

	def GetParsedPreDirection(self):
		"""Returns the directional preceding the street name from the verified address
		Returns:
			Pre-directional string (e.g. "N", "SW")
		"""
		return lib.mdAddrGetParsedPreDirection(self.I).decode('utf-8')

	def GetParsedStreetName(self):
		"""Returns the street name from the verified address
		Returns:
			Street name string (max 28 characters)
		"""
		return lib.mdAddrGetParsedStreetName(self.I).decode('utf-8')

	def GetParsedSuffix(self):
		"""Returns the street suffix from the verified address
		Returns:
			Street suffix string (e.g. "ST", "AVE", "BLVD")
		"""
		return lib.mdAddrGetParsedSuffix(self.I).decode('utf-8')

	def GetParsedPostDirection(self):
		"""Returns the directional following the street name from the verified address
		Returns:
			Post-directional string (e.g. "N", "SW")
		"""
		return lib.mdAddrGetParsedPostDirection(self.I).decode('utf-8')

	def GetParsedSuiteName(self):
		"""Returns the secondary unit designator from the verified address
		Returns:
			Suite designator string (e.g. "APT", "STE", "UNIT")
		"""
		return lib.mdAddrGetParsedSuiteName(self.I).decode('utf-8')

	def GetParsedSuiteRange(self):
		"""Returns the secondary unit number from the verified address
		Returns:
			Suite number string
		"""
		return lib.mdAddrGetParsedSuiteRange(self.I).decode('utf-8')

	def GetParsedPrivateMailboxName(self):
		"""Returns the private mailbox designator from the verified address
		Returns:
			Private mailbox name string ("PMB" or "#")
		"""
		return lib.mdAddrGetParsedPrivateMailboxName(self.I).decode('utf-8')

	def GetParsedPrivateMailboxNumber(self):
		"""Returns the private mailbox number from the verified address
		Returns:
			Private mailbox number string (max 10 characters)
		"""
		return lib.mdAddrGetParsedPrivateMailboxNumber(self.I).decode('utf-8')

	def GetParsedGarbage(self):
		"""Returns any unrecognized characters left over after parsing the verified address
		Returns:
			Garbage string (max 50 characters)
		"""
		return lib.mdAddrGetParsedGarbage(self.I).decode('utf-8')

	def GetParsedRouteService(self):
		"""Returns the route service information from the verified Canadian address
		Returns:
			Route service string
		"""
		return lib.mdAddrGetParsedRouteService(self.I).decode('utf-8')

	def GetParsedLockBox(self):
		"""Returns the lock box information from the verified Canadian address
		Returns:
			Lock box string
		"""
		return lib.mdAddrGetParsedLockBox(self.I).decode('utf-8')

	def GetParsedDeliveryInstallation(self):
		"""Returns the delivery installation information from the verified Canadian address
		Returns:
			Delivery installation string
		"""
		return lib.mdAddrGetParsedDeliveryInstallation(self.I).decode('utf-8')

	def SetReserved(self, Key, Value):
		"""Reserved for Melissa Data internal use

		Args:
			Key: Reserved parameter name
			Value: Reserved parameter value
		"""
		lib.mdAddrSetReserved(self.I, (Key or '').encode('utf-8'), (Value or '').encode('utf-8'))

	def GetReserved(self, Key):
		"""Reserved for Melissa Data internal use

		Args:
			Key: Reserved parameter name
		Returns:
			Reserved parameter value
		"""
		return lib.mdAddrGetReserved(self.I, (Key or '').encode('utf-8')).decode('utf-8')


class mdParse(object):
	"""Parses a street address string into its component parts without requiring data file initialization

	Lighter-weight alternative to AddressCheck when full verification is not needed
	"""
	def __init__(self):
		"""Constructs a new Parse instance"""
		self.I = lib.mdParseCreate()

	def __del__(self):
		"""Destroys an existing Parse instance"""
		lib.mdParseDestroy(self.I)

	def Initialize(self, DataPath):
		"""Initializes the Parse interface

		Args:
			DataPath: Path to data files (optional for basic parsing)
		Returns:
			ProgramStatus enum - ErrorNone (0) on success
		"""
		return ProgramStatus(lib.mdParseInitialize(self.I, (DataPath or '').encode('utf-8')))

	def GetBuildNumber(self):
		"""Returns the current build number of Address Object
		Returns:
			Build number string
		"""
		return lib.mdParseGetBuildNumber(self.I).decode('utf-8')

	def Parse(self, AddressToParse):
		"""Parses a US street address string into its individual components

		Args:
			AddressToParse: Full street address string to parse (e.g. "123 N Main St E Apt 3")
		"""
		lib.mdParseParse(self.I, (AddressToParse or '').encode('utf-8'))

	def ParseCanadian(self, AddressToParse):
		"""Parses a Canadian street address string into its individual components

		Args:
			AddressToParse: Full Canadian street address string to parse
		"""
		lib.mdParseParseCanadian(self.I, (AddressToParse or '').encode('utf-8'))

	def ParseNext(self):
		"""Returns an alternate parsing of the address previously submitted to Parse or ParseCanadian
		Returns:
			True (1) if another parse variant was found, false (0) if no more variants
		"""
		return lib.mdParseParseNext(self.I)

	def LastLineParse(self, LastLine):
		"""Parses a combined city, state, and ZIP code string into separate components

		Args:
			LastLine: Combined last line string (e.g. "Rancho Santa Margarita, CA 92688-2112")
		"""
		lib.mdParseLastLineParse(self.I, (LastLine or '').encode('utf-8'))

	def GetZip(self):
		"""Returns the ZIP code from the parsed address
		Returns:
			Five-digit ZIP code or Canadian postal code string
		"""
		return lib.mdParseGetZip(self.I).decode('utf-8')

	def GetPlus4(self):
		"""Returns the four-digit ZIP+4 extension from the parsed last line
		Returns:
			Plus4 string
		"""
		return lib.mdParseGetPlus4(self.I).decode('utf-8')

	def GetCity(self):
		"""Returns the city name from the parsed last line
		Returns:
			City name string
		"""
		return lib.mdParseGetCity(self.I).decode('utf-8')

	def GetState(self):
		"""Returns the two-letter state or province abbreviation from the parsed last line
		Returns:
			State abbreviation string
		"""
		return lib.mdParseGetState(self.I).decode('utf-8')

	def GetStreetName(self):
		"""Returns the street name from the parsed address
		Returns:
			Street name string (max 28 characters)
		"""
		return lib.mdParseGetStreetName(self.I).decode('utf-8')

	def GetRange(self):
		"""Returns the delivery number from the parsed address
		Returns:
			Address range string (max 10 characters)
		"""
		return lib.mdParseGetRange(self.I).decode('utf-8')

	def GetPreDirection(self):
		"""Returns the directional preceding the street name from the parsed address
		Returns:
			Pre-directional string (e.g. "N", "NE", "SW")
		"""
		return lib.mdParseGetPreDirection(self.I).decode('utf-8')

	def GetPostDirection(self):
		"""Returns the directional following the street name from the parsed address
		Returns:
			Post-directional string (e.g. "N", "NE", "SW")
		"""
		return lib.mdParseGetPostDirection(self.I).decode('utf-8')

	def GetSuffix(self):
		"""Returns the street suffix from the parsed address
		Returns:
			Street suffix string (e.g. "ST", "AVE", "BLVD")
		"""
		return lib.mdParseGetSuffix(self.I).decode('utf-8')

	def GetSuiteName(self):
		"""Returns the secondary unit designator from the parsed address
		Returns:
			Suite designator string (e.g. "APT", "STE", "UNIT")
		"""
		return lib.mdParseGetSuiteName(self.I).decode('utf-8')

	def GetSuiteNumber(self):
		"""Returns the secondary unit number from the parsed address
		Returns:
			Suite number string (max 6 characters)
		"""
		return lib.mdParseGetSuiteNumber(self.I).decode('utf-8')

	def GetPrivateMailboxNumber(self):
		"""Returns the private mailbox number from the parsed address
		Returns:
			PMB number string
		"""
		return lib.mdParseGetPrivateMailboxNumber(self.I).decode('utf-8')

	def GetPrivateMailboxName(self):
		"""Returns the private mailbox designator from the parsed address
		Returns:
			PMB designator string ("PMB" or "#")
		"""
		return lib.mdParseGetPrivateMailboxName(self.I).decode('utf-8')

	def GetGarbage(self):
		"""Returns any unrecognized characters remaining after parsing
		Returns:
			Garbage string (max 50 characters)
		"""
		return lib.mdParseGetGarbage(self.I).decode('utf-8')

	def GetRouteService(self):
		"""Returns the route service information from the parsed Canadian address
		Returns:
			Route service string
		"""
		return lib.mdParseGetRouteService(self.I).decode('utf-8')

	def GetLockBox(self):
		"""Returns the lock box information from the parsed Canadian address
		Returns:
			Lock box string
		"""
		return lib.mdParseGetLockBox(self.I).decode('utf-8')

	def GetDeliveryInstallation(self):
		"""Returns the delivery installation information from the parsed Canadian address
		Returns:
			Delivery installation string
		"""
		return lib.mdParseGetDeliveryInstallation(self.I).decode('utf-8')

	def ParseRule(self):
		"""Returns the rule number used for the last address parse
		Returns:
			Integer parse rule number
		"""
		return lib.mdParseParseRule(self.I)


class mdStreet(object):
	"""Looks up valid address ranges for a given street name and ZIP code

	Use FindStreet and FindStreetNext to iterate over matching street records
	"""
	def __init__(self):
		"""Constructs a new StreetData instance"""
		self.I = lib.mdStreetCreate()

	def __del__(self):
		"""Destroys an existing StreetData instance"""
		lib.mdStreetDestroy(self.I)

	def Initialize(self, DataPath, NationalPath, RegionalPath):
		"""Opens the required data files and prepares the StreetData interface for use

		Args:
			DataPath: Path to the mdAddr.dat file
			NationalPath: Path to the mdAddr.nat file
			RegionalPath: Deprecated; pass an empty string if required by the language
		Returns:
			ProgramStatus enum - ErrorNone (0) on success; use GetInitializeErrorString to retrieve the nature of any other error
		"""
		return ProgramStatus(lib.mdStreetInitialize(self.I, (DataPath or '').encode('utf-8'), (NationalPath or '').encode('utf-8'), (RegionalPath or '').encode('utf-8')))

	def GetInitializeErrorString(self):
		"""Returns a description of the error from the last Initialize call
		Returns:
			Error description string
		"""
		return lib.mdStreetGetInitializeErrorString(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		"""Returns the date of the US address data files
		Returns:
			Database date string in yyyy-mm-dd format
		"""
		return lib.mdStreetGetDatabaseDate(self.I).decode('utf-8')

	def GetBuildNumber(self):
		"""Returns the current build number of Address Object
		Returns:
			Build number string
		"""
		return lib.mdStreetGetBuildNumber(self.I).decode('utf-8')

	def SetLicenseString(self, License):
		"""Sets the license string required to enable full StreetData functionality

		Args:
			License: The software license key
		Returns:
			True (1) if the specified license is correct
		"""
		return lib.mdStreetSetLicenseString(self.I, (License or '').encode('utf-8'))

	def GetLicenseExpirationDate(self):
		"""Returns the expiration date of the current license string
		Returns:
			License expiration date string
		"""
		return lib.mdStreetGetLicenseExpirationDate(self.I).decode('utf-8')

	def FindStreet(self, StreetName, ZIP, CodeOnly):
		"""Retrieves the first address range matching the given street name pattern and ZIP code

		Args:
			StreetName: Street name to search; wildcards allowed at end (e.g. "MA*")
			ZIP: Five-digit ZIP code to search within
			CodeOnly: If true, restricts results to the exact ZIP code; if false, includes the surrounding city
		Returns:
			True (1) if a matching record was found
		"""
		return lib.mdStreetFindStreet(self.I, (StreetName or '').encode('utf-8'), (ZIP or '').encode('utf-8'), CodeOnly)

	def FindStreetNext(self):
		"""Retrieves the next matching address range after a successful FindStreet call
		Returns:
			True (1) if another record was found, false (0) if no more records
		"""
		return lib.mdStreetFindStreetNext(self.I)

	def IsAddressInRange(self, InputRange, LoRange, HiRange):
		"""Determines if an address number falls within a street address range
		.. deprecated::
			Use IsAddressInRange2 instead.

		Args:
			InputRange: Address number to test
			LoRange: Low end of the valid range
			HiRange: High end of the valid range
		Returns:
			True (1) if the address falls within the range
		"""
		return lib.mdStreetIsAddressInRange(self.I, (InputRange or '').encode('utf-8'), (LoRange or '').encode('utf-8'), (HiRange or '').encode('utf-8'))

	def IsAddressInRange2(self, InputRange, LoRange, HiRange, OddEvenFlag):
		"""Determines if an address number falls within a street address range and matches the odd/even indicator. Supersedes the older IsAddressInRange function, which did not account for odd/even ranges

		Args:
			InputRange: Address number to test (from input address)
			LoRange: Low end of the valid range (from GetPrimaryRangeLow)
			HiRange: High end of the valid range (from GetPrimaryRangeHigh)
			OddEvenFlag: Odd/even indicator from GetPrimaryRangeOddEven
		Returns:
			True (1) if the address is within range and matches the odd/even indicator
		"""
		return lib.mdStreetIsAddressInRange2(self.I, (InputRange or '').encode('utf-8'), (LoRange or '').encode('utf-8'), (HiRange or '').encode('utf-8'), (OddEvenFlag or '').encode('utf-8'))

	def GetAutoCompletion(self, Address, Zip, mode, DPVOnly):
		"""Returns one possible street address suggestion for auto-complete based on partial address and ZIP code

		Args:
			Address: Full or partial street address input
			Zip: Five-digit US ZIP code
			mode: AutoCompletionMode enum controlling suite display (SingleSuite, RangedSuite, PlaceHolderSuite, NoSuite)
			DPVOnly: If true, returns only DPV-confirmed addresses
		Returns:
			Suggested address string, or empty string when no more suggestions remain
		"""
		return lib.mdStreetGetAutoCompletion(self.I, (Address or '').encode('utf-8'), (Zip or '').encode('utf-8'), AutoCompletionMode(mode).value, DPVOnly).decode('utf-8')

	def ResetAutoCompletion(self):
		"""Resets the auto-completion state to prepare for a new address lookup
		"""
		lib.mdStreetResetAutoCompletion(self.I)

	def GetBaseAlternateIndicator(self):
		"""Returns whether the matched street record is a base or alternate record
		Returns:
			"B" for base (preferred) record, "A" for alternate record
		"""
		return lib.mdStreetGetBaseAlternateIndicator(self.I).decode('utf-8')

	def GetLACSIndicator(self):
		"""Returns whether the street address has undergone a rural-to-city-style conversion
		Returns:
			"L" if converted, empty if not
		"""
		return lib.mdStreetGetLACSIndicator(self.I).decode('utf-8')

	def GetUrbanizationCode(self):
		"""Returns the urbanization code for Puerto Rican street records
		Returns:
			Urbanization code string (max 6 characters)
		"""
		return lib.mdStreetGetUrbanizationCode(self.I).decode('utf-8')

	def GetUrbanizationName(self):
		"""Returns the urbanization name for Puerto Rican street records
		Returns:
			Urbanization name string
		"""
		return lib.mdStreetGetUrbanizationName(self.I).decode('utf-8')

	def GetLastLineNumber(self):
		"""Returns the last line number used for advanced address matching tie-breaking
		Returns:
			Last line number string (max 6 characters)
		"""
		return lib.mdStreetGetLastLineNumber(self.I).decode('utf-8')

	def GetAddressType(self):
		"""Returns the address type code for the matched street record
		Returns:
			S=Street, P=PO Box, H=High Rise, R=Rural Route, F=Firm, G=General Delivery
		"""
		return lib.mdStreetGetAddressType(self.I).decode('utf-8')

	def GetCongressionalDistrict(self):
		"""Returns the congressional district for the matched street record
		Returns:
			State abbreviation plus two-digit district number (e.g. "CA01")
		"""
		return lib.mdStreetGetCongressionalDistrict(self.I).decode('utf-8')

	def GetCountyFips(self):
		"""Returns the five-digit county FIPS code for the matched street record
		Returns:
			Five-digit FIPS code (e.g. "06037" for Los Angeles CA)
		"""
		return lib.mdStreetGetCountyFips(self.I).decode('utf-8')

	def GetCompany(self):
		"""Returns the company or building name associated with the matched street record
		Returns:
			Company name string (max 40 characters)
		"""
		return lib.mdStreetGetCompany(self.I).decode('utf-8')

	def GetCarrierRoute(self):
		"""Returns the carrier route code for the matched street record
		Returns:
			Four-character carrier route code (e.g. "C027")
		"""
		return lib.mdStreetGetCarrierRoute(self.I).decode('utf-8')

	def GetZip(self):
		"""Returns the five-digit ZIP code for the matched street record
		Returns:
			Five-digit ZIP code string
		"""
		return lib.mdStreetGetZip(self.I).decode('utf-8')

	def GetDeliveryInstallation(self):
		"""Returns the delivery installation for matched Canadian street records
		Returns:
			Delivery installation string
		"""
		return lib.mdStreetGetDeliveryInstallation(self.I).decode('utf-8')

	def GetPlus4High(self):
		"""Returns the highest Plus4 code in the range for the matched street record
		Returns:
			Four-digit Plus4 high value string
		"""
		return lib.mdStreetGetPlus4High(self.I).decode('utf-8')

	def GetPlus4Low(self):
		"""Returns the lowest Plus4 code in the range for the matched street record
		Returns:
			Four-digit Plus4 low value string
		"""
		return lib.mdStreetGetPlus4Low(self.I).decode('utf-8')

	def GetSuiteRangeOddEven(self):
		"""Returns the odd/even indicator for the suite range of the matched street record
		Returns:
			"O" for odd only, "E" for even only, "B" for both
		"""
		return lib.mdStreetGetSuiteRangeOddEven(self.I).decode('utf-8')

	def GetSuiteRangeHigh(self):
		"""Returns the highest suite number in the range for the matched street record
		Returns:
			Suite range high value string (max 8 characters)
		"""
		return lib.mdStreetGetSuiteRangeHigh(self.I).decode('utf-8')

	def GetSuiteRangeLow(self):
		"""Returns the lowest suite number in the range for the matched street record
		Returns:
			Suite range low value string (max 8 characters)
		"""
		return lib.mdStreetGetSuiteRangeLow(self.I).decode('utf-8')

	def GetSuiteName(self):
		"""Returns the suite designator for the matched street record
		Returns:
			Suite designator string (e.g. "APT", "STE", "UNIT")
		"""
		return lib.mdStreetGetSuiteName(self.I).decode('utf-8')

	def GetPostDirection(self):
		"""Returns the directional following the street name for the matched street record
		Returns:
			Post-directional string (e.g. "N", "NE", "SW")
		"""
		return lib.mdStreetGetPostDirection(self.I).decode('utf-8')

	def GetSuffix(self):
		"""Returns the street suffix for the matched street record
		Returns:
			Street suffix string (e.g. "ST", "AVE", "BLVD")
		"""
		return lib.mdStreetGetSuffix(self.I).decode('utf-8')

	def GetStreetName(self):
		"""Returns the street name for the matched street record
		Returns:
			Street name string (max 28 characters)
		"""
		return lib.mdStreetGetStreetName(self.I).decode('utf-8')

	def GetPreDirection(self):
		"""Returns the directional preceding the street name for the matched street record
		Returns:
			Pre-directional string (e.g. "N", "NE", "SW")
		"""
		return lib.mdStreetGetPreDirection(self.I).decode('utf-8')

	def GetPrimaryRangeOddEven(self):
		"""Returns the odd/even indicator for the primary address range of the matched street record
		Returns:
			"O" for odd only, "E" for even only, "B" for both
		"""
		return lib.mdStreetGetPrimaryRangeOddEven(self.I).decode('utf-8')

	def GetPrimaryRangeHigh(self):
		"""Returns the highest street number in the primary address range of the matched record
		Returns:
			Primary range high value string (10 digits, zero-padded)
		"""
		return lib.mdStreetGetPrimaryRangeHigh(self.I).decode('utf-8')

	def GetPrimaryRangeLow(self):
		"""Returns the lowest street number in the primary address range of the matched record
		Returns:
			Primary range low value string (10 digits, zero-padded)
		"""
		return lib.mdStreetGetPrimaryRangeLow(self.I).decode('utf-8')


class mdZip(object):
	"""Looks up geographic data, city names, and postal information by ZIP code or city name

	Use FindZip, FindZipInCity, and FindCityInState to retrieve ZIP code and city records
	"""
	def __init__(self):
		"""Constructs a new ZipData instance"""
		self.I = lib.mdZipCreate()

	def __del__(self):
		"""Destroys an existing ZipData instance"""
		lib.mdZipDestroy(self.I)

	def Initialize(self, DataPath, NationalPath, RegionalPath):
		"""Opens the required data files and prepares the ZipData interface for use

		Args:
			DataPath: Path to the mdAddr.dat file
			NationalPath: Path to the mdAddr.nat file
			RegionalPath: Deprecated; pass an empty string if required by the language
		Returns:
			ProgramStatus enum - ErrorNone (0) on success; use GetInitializeErrorString to retrieve the nature of any other error
		"""
		return ProgramStatus(lib.mdZipInitialize(self.I, (DataPath or '').encode('utf-8'), (NationalPath or '').encode('utf-8'), (RegionalPath or '').encode('utf-8')))

	def GetInitializeErrorString(self):
		"""Returns a description of the error from the last Initialize call
		Returns:
			Error description string
		"""
		return lib.mdZipGetInitializeErrorString(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		"""Returns the date of the US address data files
		Returns:
			Database date string in yyyy-mm-dd format
		"""
		return lib.mdZipGetDatabaseDate(self.I).decode('utf-8')

	def GetBuildNumber(self):
		"""Returns the current build number of Address Object
		Returns:
			Build number string
		"""
		return lib.mdZipGetBuildNumber(self.I).decode('utf-8')

	def SetLicenseString(self, License):
		"""Sets the license string required to enable full ZipData functionality

		Args:
			License: The software license key
		Returns:
			True (1) if the specified license is correct
		"""
		return lib.mdZipSetLicenseString(self.I, (License or '').encode('utf-8'))

	def GetLicenseExpirationDate(self):
		"""Returns the expiration date of the current license string
		Returns:
			License expiration date string
		"""
		return lib.mdZipGetLicenseExpirationDate(self.I).decode('utf-8')

	def FindZip(self, Zip, GetLastLineRecord):
		"""Retrieves the first city record for the specified ZIP code

		Args:
			Zip: Five-digit ZIP code to look up
			GetLastLineRecord: If true, returns only the official preferred city name record; disables FindZipNext
		Returns:
			True (1) if a record was found
		"""
		return lib.mdZipFindZip(self.I, (Zip or '').encode('utf-8'), GetLastLineRecord)

	def FindZipNext(self):
		"""Retrieves the next city record for the ZIP code passed to FindZip
		Returns:
			True (1) if another record was found, false (0) if no more records
		"""
		return lib.mdZipFindZipNext(self.I)

	def FindZipInCity(self, City, State):
		"""Retrieves the first ZIP code record for the specified city and state

		Args:
			City: City name to look up (max 28 characters; wildcards allowed with *)
			State: Two-character state abbreviation
		Returns:
			True (1) if a record was found
		"""
		return lib.mdZipFindZipInCity(self.I, (City or '').encode('utf-8'), (State or '').encode('utf-8'))

	def FindZipInCityNext(self):
		"""Retrieves the next ZIP code record for the city and state passed to FindZipInCity
		Returns:
			True (1) if another record was found, false (0) if no more records
		"""
		return lib.mdZipFindZipInCityNext(self.I)

	def FindCityInState(self, City, State):
		"""Retrieves the first city record matching the given city name and state

		Args:
			City: City name to search (max 28 characters; wildcards allowed with *)
			State: Two-character state abbreviation
		Returns:
			True (1) if a match was found
		"""
		return lib.mdZipFindCityInState(self.I, (City or '').encode('utf-8'), (State or '').encode('utf-8'))

	def FindCityInStateNext(self):
		"""Retrieves the next matching city record after a successful FindCityInState call
		Returns:
			True (1) if another match was found, false (0) if no more records
		"""
		return lib.mdZipFindCityInStateNext(self.I)

	def ComputeDistance(self, lat1, long1, lat2, long2):
		"""Computes the distance in miles between two geographic coordinates

		Args:
			lat1: Latitude of point 1 in degrees
			long1: Longitude of point 1 in degrees (negative for US)
			lat2: Latitude of point 2 in degrees
			long2: Longitude of point 2 in degrees (negative for US)
		Returns:
			Distance in miles, or 9999 if coordinates are invalid
		"""
		return lib.mdZipComputeDistance(self.I, lat1, long1, lat2, long2)

	def ComputeBearing(self, lat1, long1, lat2, long2):
		"""Computes the compass bearing in degrees from point 1 to point 2

		Args:
			lat1: Latitude of point 1 in degrees
			long1: Longitude of point 1 in degrees (negative for US)
			lat2: Latitude of point 2 in degrees
			long2: Longitude of point 2 in degrees (negative for US)
		Returns:
			Bearing in degrees (0=North, 90=East, 180=South, 270=West), or 999 if coordinates are invalid
		"""
		return lib.mdZipComputeBearing(self.I, lat1, long1, lat2, long2)

	def GetCountyNameFromFips(self, FipsCode):
		"""Returns the county name for a given county FIPS code

		Args:
			FipsCode: Five-digit county FIPS code
		Returns:
			County name string
		"""
		return lib.mdZipGetCountyNameFromFips(self.I, (FipsCode or '').encode('utf-8')).decode('utf-8')

	def GetSCFArea(self, Zip, LatN, LatS, LonE, LonW):
		"""Returns the geographic bounding box (north, south, east, west) for a Sectional Center Facility area

		Args:
			Zip: ZIP code to look up the SCF area for
			LatN: Pointer to receive the northern latitude boundary
			LatS: Pointer to receive the southern latitude boundary
			LonE: Pointer to receive the eastern longitude boundary
			LonW: Pointer to receive the western longitude boundary
		Returns:
			Number of ZIP codes in the SCF area
		"""
		return lib.mdZipGetSCFArea(self.I, (Zip or '').encode('utf-8'), LatN, LatS, LonE, LonW)

	def GetZip(self):
		"""Returns the five-digit ZIP code from the current ZipData record
		Returns:
			Five-digit ZIP code string
		"""
		return lib.mdZipGetZip(self.I).decode('utf-8')

	def GetCity(self):
		"""Returns the city name from the current ZipData record
		Returns:
			City name string (max 28 characters)
		"""
		return lib.mdZipGetCity(self.I).decode('utf-8')

	def GetCityAbbreviation(self):
		"""Returns the official USPS 13-character city name abbreviation from the current record
		Returns:
			City abbreviation (full city name if 13 characters or fewer)
		"""
		return lib.mdZipGetCityAbbreviation(self.I).decode('utf-8')

	def GetState(self):
		"""Returns the two-letter state abbreviation from the current ZipData record
		Returns:
			Two-letter state abbreviation string
		"""
		return lib.mdZipGetState(self.I).decode('utf-8')

	def GetZipType(self):
		"""Returns the ZIP code type for the current record
		Returns:
			"P" for PO Box only, "U" for unique/institutional, "M" for military, empty for standard
		"""
		return lib.mdZipGetZipType(self.I).decode('utf-8')

	def GetCountyName(self):
		"""Returns the county name for the current ZipData record
		Returns:
			County name string (max 25 characters)
		"""
		return lib.mdZipGetCountyName(self.I).decode('utf-8')

	def GetCountyFips(self):
		"""Returns the five-digit county FIPS code for the current ZipData record
		Returns:
			Five-digit FIPS code string
		"""
		return lib.mdZipGetCountyFips(self.I).decode('utf-8')

	def GetAreaCode(self):
		"""Returns the dominant telephone area code for the ZIP code
		Returns:
			Three-digit area code string
		"""
		return lib.mdZipGetAreaCode(self.I).decode('utf-8')

	def GetLongitude(self):
		"""Returns the longitude of the geographic center of the ZIP code
		Returns:
			Longitude string accurate to 6 decimal places (negative for US)
		"""
		return lib.mdZipGetLongitude(self.I).decode('utf-8')

	def GetLatitude(self):
		"""Returns the latitude of the geographic center of the ZIP code
		Returns:
			Latitude string accurate to 4 decimal places
		"""
		return lib.mdZipGetLatitude(self.I).decode('utf-8')

	def GetTimeZone(self):
		"""Returns the time zone name for the ZIP code
		Returns:
			Time zone name string (e.g. "Eastern Time", "Pacific Time")
		"""
		return lib.mdZipGetTimeZone(self.I).decode('utf-8')

	def GetTimeZoneCode(self):
		"""Returns the numeric time zone code for the ZIP code
		Returns:
			Time zone code (e.g. "5" for Eastern, "8" for Pacific)
		"""
		return lib.mdZipGetTimeZoneCode(self.I).decode('utf-8')

	def GetMsa(self):
		"""Returns the Metropolitan Statistical Area (MSA) code for the ZIP code
		Returns:
			MSA code string
		"""
		return lib.mdZipGetMsa(self.I).decode('utf-8')

	def GetPmsa(self):
		"""Returns the Primary Metropolitan Statistical Area (PMSA) code for the ZIP code
		Returns:
			PMSA code string
		"""
		return lib.mdZipGetPmsa(self.I).decode('utf-8')

	def GetFacilityCode(self):
		"""Returns the USPS postal facility type code for the ZIP code
		Returns:
			A=Airport Mail Facility, B=Branch, C=Community Post Office, D=Area Distribution Center, E=Sectional Center Facility, F=Delivery Distribution Center, G=General Mail Facility, K=Bulk Mail Facility, M=Money Order Unit, N=Community or Place name, P=Post Office, S=Station, U=Urbanization (Puerto Rico), X=Vanity name (should not be used). Not returned for Canadian postal codes
		"""
		return lib.mdZipGetFacilityCode(self.I).decode('utf-8')

	def GetLastLineIndicator(self):
		"""Returns whether the current city name is the official USPS last-line name for the ZIP code. Not returned for Canadian postal codes
		Returns:
			"L" if this is the official last-line city (only one record per ZIP Code is coded with "L"), empty otherwise
		"""
		return lib.mdZipGetLastLineIndicator(self.I).decode('utf-8')

	def GetLastLineNumber(self):
		"""Returns the last line number used for advanced address matching tie-breaking. Not returned for Canadian postal codes
		Returns:
			Six-character last line number string
		"""
		return lib.mdZipGetLastLineNumber(self.I).decode('utf-8')

	def GetPreferredLastLineNumber(self):
		"""Returns the preferred last line number for the current city record
		Returns:
			Six-character preferred last line number string
		"""
		return lib.mdZipGetPreferredLastLineNumber(self.I).decode('utf-8')

	def GetAutomation(self):
		"""Returns the carrier route rate mail indicator for letter-size mail in the ZIP code. Not returned for Canadian postal codes
		Returns:
			"A" carrier route rates apply and merging is permitted, "B" carrier route rates apply and merging is not permitted, "C" carrier route rates do not apply and merging is permitted, "D" carrier route rates do not apply and merging is not permitted
		"""
		return lib.mdZipGetAutomation(self.I).decode('utf-8')

	def GetFinanceNumber(self):
		"""Returns the USPS finance number for the postal facility associated with the ZIP code
		Returns:
			Finance number string
		"""
		return lib.mdZipGetFinanceNumber(self.I).decode('utf-8')
