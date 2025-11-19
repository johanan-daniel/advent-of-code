#!/bin/zsh

# Check if a number is given as an input
if [ -z "$1" ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# Create the new directory
dir_name="day_$1"
mkdir $dir_name

# Create the 3 files inside the directory
touch "$dir_name/day_${1}_example.txt"
touch "$dir_name/day_${1}_input.txt"
touch "$dir_name/day_${1}.py"

echo "Directory $dir_name with files created successfully."
