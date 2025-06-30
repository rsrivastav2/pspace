$serverName = "localhost"          # Change to your SQL Server name
$databaseName = "MyNewDatabase"    # Your desired DB name

# SQL Query to create database
$sql = "CREATE DATABASE [$databaseName]"

# Run the query using Invoke-Sqlcmd
Invoke-Sqlcmd -ServerInstance $serverName -Query $sql
