# Set variables
$serverInstance = "localhost"       # Change if needed
$databaseName = "TestDB_PowerShell"

# Create the T-SQL command
$query = @"
CREATE DATABASE [$databaseName];
"@

# Run the SQL command
Invoke-Sqlcmd -ServerInstance $serverInstance -Query $query
