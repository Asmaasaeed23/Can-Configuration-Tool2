#define CanIndex 1U
#define CanMainFunctionModePeriod 2U
#define CanTimeoutDuration 3U
#define CanMainFunctionWakeupPeriod 4U
#define CanMultiplexedTransmission False
#define CanPublicIcomSupport False
#define CanSetBaudrateApi False
#define CanVersionInfoApi False
#define CanDevErrorDetect False



#define NUM_OF_CanControllers 2U
#define NUM_OF_HTH 4U
#define NUM_OF_HRH 0U
#define size_MAP_HOH_2_CANObj 4U





#define UserCANCfg \
{.CanConfigSet.CanController =\
    {\
        {\
        .CanControllerId = 0,\
        .CanControllerActivation = False,\
        .CanControllerBaseAddress = 0x40040000,\
        .CanWakeupSupport = False,\
        .CanWakeupFunctionalityAPI = False,\
        .CanTxProcessing = INTERRUPT,\
        .CanRxProcessing = INTERRUPT,\
        .CanBusoffProcessing = INTERRUPT,\
        .CanWakeupProcessing = INTERRUPT,\


        .CanControllerDefaultBaudrate = &CanContanier.CanConfigSet.CanController[0].CanControllerBaudrateConfig,\


        .CanControllerBaudrateConfig.CanControllerBaudRate = 0,\
        .CanControllerBaudrateConfig.CanControllerPropSeg = 0,\
        .CanControllerBaudrateConfig.CanControllerSeg1 = 0,\
        .CanControllerBaudrateConfig.CanControllerSeg2 = 0,\
        .CanControllerBaudrateConfig.CanControllerSyncJumpWidth = 0,\
        .CanControllerBaudrateConfig.CanControllerBaudRateConfigID = 0,\
        },\
        {\
        .CanControllerId = 0,\
        .CanControllerActivation = False,\
        .CanControllerBaseAddress = 0x40041000,\
        .CanWakeupSupport = False,\
        .CanWakeupFunctionalityAPI = False,\
        .CanTxProcessing = INTERRUPT,\
        .CanRxProcessing = INTERRUPT,\
        .CanBusoffProcessing = INTERRUPT,\
        .CanWakeupProcessing = INTERRUPT,\


        .CanControllerDefaultBaudrate = &CanContanier.CanConfigSet.CanController[1].CanControllerBaudrateConfig,\


        .CanControllerBaudrateConfig.CanControllerBaudRate = 0,\
        .CanControllerBaudrateConfig.CanControllerPropSeg = 0,\
        .CanControllerBaudrateConfig.CanControllerSeg1 = 0,\
        .CanControllerBaudrateConfig.CanControllerSeg2 = 0,\
        .CanControllerBaudrateConfig.CanControllerSyncJumpWidth = 0,\
        .CanControllerBaudrateConfig.CanControllerBaudRateConfigID = 0,\
        }\
    }\
};





#define hthMap \
{.CanConfigSet.CanHardwareObject =\
    {\
        {\
           .CanHandleType = BASIC,\
           .CanObjectType = TRANSMIT,\
           .CanIdType = STANDARD,\
           .CanObjectId = 0,\
           .CanFdPaddingValue = 0,\
           .CanTriggerTransmitEnable = False,\
           .CanControllerRef = &CanContanier.CanConfigSet.CanController[0],\


           .CanHwFilter.CanHwFilterMask = 0x0,\
           .CanHwFilter.CanHwFilterCode = 0,\
        },\
        {\
           .CanHandleType = BASIC,\
           .CanObjectType = TRANSMIT,\
           .CanIdType = STANDARD,\
           .CanObjectId = 0,\
           .CanFdPaddingValue = 0,\
           .CanTriggerTransmitEnable = False,\
           .CanControllerRef = &CanContanier.CanConfigSet.CanController[0],\


           .CanHwFilter.CanHwFilterMask = 0x0,\
           .CanHwFilter.CanHwFilterCode = 0,\
        },\
        {\
           .CanHandleType = BASIC,\
           .CanObjectType = TRANSMIT,\
           .CanIdType = STANDARD,\
           .CanObjectId = 0,\
           .CanFdPaddingValue = 0,\
           .CanTriggerTransmitEnable = False,\
           .CanControllerRef = &CanContanier.CanConfigSet.CanController[0],\


           .CanHwFilter.CanHwFilterMask = 0x0,\
           .CanHwFilter.CanHwFilterCode = 0,\
        },\
        {\
           .CanHandleType = BASIC,\
           .CanObjectType = TRANSMIT,\
           .CanIdType = STANDARD,\
           .CanObjectId = 0,\
           .CanFdPaddingValue = 0,\
           .CanTriggerTransmitEnable = False,\
           .CanControllerRef = &CanContanier.CanConfigSet.CanController[0],\


           .CanHwFilter.CanHwFilterMask = 0x0,\
           .CanHwFilter.CanHwFilterCode = 0,\
        }\
    }\
};
#define hrhMap \
{.CanConfigSet.CanHardwareObject =\
    {\
        {\
