
sql1 = "insert into alerts.status(Identifier,Node,Severity,Summary,StateChange,FirstOccurrence,LastOccurrence,AlertKey,AlertGroup,Agent,Manager,CSL_Maintenance,CSL_ComponentType,CSL_Component,CSL_SubComponent,CSL_EventID,CSL_Flag,NodeAlias) values('test.01','3.255.255.1',5,'专线中断需手工切换1.3.6.1.2.1.80.0.1<pingProbeFailed> NQA entry sh sh probe fail trap information: pingCtlOwnerIndex: sh, pingCtlTestName: sh, pingCtlTargetAddressType: 1, pingCtlTargetAddress: 172.27.31.2, pingResultsOperStatus: 1, pingResultsIp',getdate(),getdate(),getdate(),'test','10NQA_NQA Trap','H3c','Syslog Probe on pmprobe01',0,'网络设备','H3C ROUTER','H3C ROUTER','FM-07-03-999-9999',1,'YZPCRT01');" \
       "go" \
       "quit"





sql2 = 'i'
sql3 = 'i'
sql4 = 'i'
sql5 = 'i'
sql6 = 'i'
sql7 = 'i'
sql8 = 'i'
sql9 = 'i'
sql10 = 'i'
sql11 = 'i'
sql12 = 'i'
sql13 = 'i'
sql14 = 'i'




drill_dict = {
    1:sql1,
    2:sql2,
    3:sql3,
    4:sql4,
    5:sql5,
    6:sql6,
    7:sql7,
    8:sql8,
    9:sql9,
    10:sql10,
    11:sql11,
    12:sql12,
    13:sql13,
    14:sql14,
    # 1:sql15,
    # 1:sql1,
}