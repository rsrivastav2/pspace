Perf
| where ObjectName == "LogicalDisk" // Filter for disk-related data
| where CounterName == "% Free Space" // Specify the counter for free space percentage
| summarize AvgFreeSpace = avg(CounterValue) by InstanceName, bin(TimeGenerated, 1h)
| project InstanceName, TimeGenerated, AvgFreeSpace
