#!/bin/bash

for d in ~/workspace/github/*/ ; do
        cd $d
        if [[ -n $(git status | grep -e 'Changes not staged for commit' -e 'Untracked files') ]]
        then
                echo $d
        fi
done

