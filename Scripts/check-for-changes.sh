#!/bin/bash
# Check if there were any changes in the Source directory
! git diff `echo "$CIRCLE_COMPARE_URL" | cut -d '/' -f 7` --name-only --exit-code Source Scripts circle.yml
