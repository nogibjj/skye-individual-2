#!/bin/bash

    command=$1
    name=$2

    echo "Running $name..."

    # Start the command in the background and get its PID
    /usr/bin/time -p -o "${name}_time.log" $command &
    pid=$!
    echo "$name PID: $pid"


    # Monitor memory usage every 0.5 seconds until the process completes
    max_mem=0
    while ps -p $pid > /dev/null; do
        # Get memory usage of the process
        mem_usage=$(ps -o rss= -p $pid)  # Resident Set Size in KB
        if [[ $mem_usage -gt $max_mem ]]; then
            max_mem=$mem_usage
        fi
        sleep 0.5
    done

    # Output the results
    echo " " >> README.md
    echo "-----------------------------------------" >> README.md
    echo "# Perfomance Report for $name" >> README.md
    echo "Max memory usage by $name: $max_mem KB" >> README.md
    echo "Processing time for $name:$(awk 'NR==1 {print $2}' ${name}_time.log)" >> README.md
    echo "-----------------------------------------" >> README.md
    echo " " >> README.md