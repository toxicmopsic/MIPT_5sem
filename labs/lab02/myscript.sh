#!/bin/zsh
while $(true); do
    count_folders=$(find ~/custom_tmp/* -maxdepth 0 -type d | wc -l)
    count_files=$(find ~/custom_tmp/* -maxdepth 0 -type f | wc -l)
    echo "Contents of custom_tmp:" $count_files "files," $count_folders "folders"
    sleep 10
done;
