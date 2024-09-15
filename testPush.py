Perf
| where ObjectName == "LogicalDisk" and CounterName in ("% Free Space", "% Disk Space Used")
| summarize avg(CounterValue) by bin(TimeGenerated, 1h), Computer, CounterName, InstanceName
| project TimeGenerated, Computer, InstanceName, CounterName, avg_CounterValue
| order by TimeGenerated asc
