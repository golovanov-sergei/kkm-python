import win32com.client

if __name__ == '__main__':
    frDrv = win32com.client.Dispatch('Addin.DRvFR')
    frDrv.FindDevice()
    frDrv.Password = 30
    frDrv.ProtocolType = 0
    frDrv.ConnectionType = 0
    frDrv.Connect()
    frDrv.Disconnect()
    # frDrv.Connect()
    # frDrv.GetDeviceMetrics()
    print('UDescription: ', frDrv.UDescription)
    print('OperatorNumber: ', frDrv.OperatorNumber)
    print('ECRSoftVersion: ', frDrv.ECRSoftVersion)
    print('ECRBuild: ', frDrv.ECRBuild)
    print('ECRSoftDate: ', frDrv.ECRSoftDate)
    print('LogicalNumber: ', frDrv.LogicalNumber)
    print('OpenDocumentNumber: ', frDrv.OpenDocumentNumber)
    print('ECRFlags: ', frDrv.ECRFlags)
    print('ReceiptRibbonIsPresent: ', frDrv.ReceiptRibbonIsPresent)
    print('JournalRibbonIsPresent: ', frDrv.JournalRibbonIsPresent)
    print('SKNOStatus: ', frDrv.SKNOStatus)
    print('SlipDocumentIsPresent: ', frDrv.SlipDocumentIsPresent)
    print('SlipDocumentIsMoving: ', frDrv.SlipDocumentIsMoving)
    print('PointPosition: ', frDrv.PointPosition)
    print('EKLZIsPresent: ', frDrv.EKLZIsPresent)
    print('JournalRibbonOpticalSensor: ', frDrv.JournalRibbonOpticalSensor)
    print('ReceiptRibbonOpticalSensor: ', frDrv.ReceiptRibbonOpticalSensor)
    print('JournalRibbonLever: ', frDrv.JournalRibbonLever)
    print('ReceiptRibbonLever: ', frDrv.ReceiptRibbonLever)
    print('LidPositionSensor: ', frDrv.LidPositionSensor)
    print('IsPrinterLeftSensorFailure: ', frDrv.IsPrinterLeftSensorFailure)
    print('IsPrinterRightSensorFailure: ', frDrv.IsPrinterRightSensorFailure)
    print('IsDrawerOpen: ', frDrv.IsDrawerOpen)
    print('IsEKLZOverflow: ', frDrv.IsEKLZOverflow)
    print('QuantityPointPosition: ', frDrv.QuantityPointPosition)
    print('ECRMode: ', frDrv.ECRMode)
    print('ECRModeDescription: ', frDrv.ECRModeDescription)
    print('ECRMode8Status: ', frDrv.ECRMode8Status)
    print('ECRModeStatus: ', frDrv.ECRModeStatus)
    print('ECRAdvancedMode: ', frDrv.ECRAdvancedMode)
    print('ECRAdvancedModeDescription: ', frDrv.ECRAdvancedModeDescription)
    print('PortNumber: ', frDrv.PortNumber)
    print('FMSoftVersion: ', frDrv.FMSoftVersion)
    print('FMBuild: ', frDrv.FMBuild)
    print('FMSoftDate: ', frDrv.FMSoftDate)
    print('Date: ', frDrv.Date)
    print('Time: ', frDrv.Time)
    print('TimeStr: ', frDrv.TimeStr)
    print('FMFlags: ', frDrv.FMFlags)
    print('FM1IsPresent: ', frDrv.FM1IsPresent)
    print('FM2IsPresent: ', frDrv.FM2IsPresent)
    print('FMOverflow: ', frDrv.FMOverflow)
    print('IsBatteryLow: ', frDrv.IsBatteryLow)
    print('IsLastFMRecordCorrupted: ', frDrv.IsLastFMRecordCorrupted)
    print('IsFMSessionOpen: ', frDrv.IsFMSessionOpen)
    print('IsFM24HoursOver: ', frDrv.IsFM24HoursOver)
    print('SerialNumber: ', frDrv.SerialNumber)
    print('SessionNumber: ', frDrv.SessionNumber)
    print('FreeRecordInFM: ', frDrv.FreeRecordInFM)
    print('RegistrationNumber: ', frDrv.RegistrationNumber)
    print('FreeRegistration: ', frDrv.FreeRegistration)
    print('INN: ', frDrv.INN)
    # frDrv.PrintReportWithoutCleaning()
    # frDrv.Disconnect()
    # print ('Fuck')
    # frDrv.Free()