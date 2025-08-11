#!/usr/bin/env bash

# Display search prompt
search="echo -e "\ue745  Firefox" | $(wofi -d -i -p "Web Search: " -W 500 -H 175)"

# check if string is empty
if [ -z "$search" ]; then
	# search is empty
	echo "search string empty"
else
	# Use firefox to search 
	firefox --search "$search"
fi
