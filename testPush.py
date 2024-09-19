KubePodInventory
| summarize RunningPods = countif(Status == "Running"),
            OtherStatusCount = countif(Status != "Running" and Status != "Pending"),
            PodRestartCount = countif(RestartCount > 0)
    by ServiceName
| extend PodRestartTimeInDays = (max(Timestamp) - min(Timestamp)) / 86400 // Assuming Timestamp is in seconds
| project ServiceName, Running = RunningPods, OtherStatus = OtherStatusCount, PodRestartTimeInDays
