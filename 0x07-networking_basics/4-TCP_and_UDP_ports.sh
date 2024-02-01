#!/bin/bash

# Display column headers
printf "%-20s %-10s %-20s\n" "Port" "PID" "Program"

# Iterate over each listening port
netstat -tuln | awk '$NF == "LISTEN" {print $4}' | while read -r line; do
    # Extract port number
    port=$(echo "$line" | awk -F ":" '{print $NF}')
    
    # Get PID and program name associated with the port
    pid=$(lsof -i :$port -t)
    if [ -n "$pid" ]; then
        program=$(ps -p $pid -o comm=)
        printf "%-20s %-10s %-20s\n" "$port" "$pid" "$program"
    fi
done

