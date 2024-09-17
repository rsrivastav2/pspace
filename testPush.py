Perf
| where ObjectName == "LogicalDisk"
| where CounterName in ("% Free Space", "% Disk Space Used") // Specify the relevant counters
| summarize AvgValue = avg(CounterValue) by InstanceName, CounterName, bin(TimeGenerated, 1h)
| project InstanceName, CounterName, AvgValue
| extend SpaceType = case(
    CounterName == "% Free Space", "Free Space",
    CounterName == "% Disk Space Used", "Used Space"
)
| summarize TotalValue = sum(AvgValue) by InstanceName, SpaceType
| project SpaceType, TotalValue
