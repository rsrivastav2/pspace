Perf
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| summarize avg(CounterValue) by bin(TimeGenerated, 5m), Computer
| project TimeGenerated, Computer, avg_CounterValue
| order by TimeGenerated asc
