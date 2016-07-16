#!/bin/bash
# Do not check these directories or files for changes:
DO_NOT_CHECK=(
	Readme.md
)

# Get the top-level file list
check=`ls -x`
# Remove DO_NOT_CHECK from CHECK
for i in ${DO_NOT_CHECK[@]}; do
	check=${check/ ${i} / }
done
# Put into an array
check=( $check )

# Check if there were any changes since the last commit
! git diff `echo "$CIRCLE_COMPARE_URL" | cut -d '/' -f 7` --name-only --exit-code ${check[*]}
