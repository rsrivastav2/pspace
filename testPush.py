Perf
| where ObjectName == "Process" // Filter for process-related data
| where CounterName == "% Processor Time" // Specify the counter for CPU usage by processes
| summarize AvgCpuUsage = avg(CounterValue) by InstanceName, bin(TimeGenerated, 5m)
| project InstanceName, TimeGenerated, AvgCpuUsage
