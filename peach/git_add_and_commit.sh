#!/bin/bash

msg=""

while getopts ":m:" opt; do
  case $opt in
    m)
      msg="$OPTARG" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

echo "$msg"
eval "python ./dev_changeLogs/scripts/changelog_gen_args.py \"$msg\""
eval "python ./dev_changeLogs/scripts/changelog_combine.py"

cd ..
eval "git add --all"
eval "git status"

echo "git-commit message: $msg"


eval "git commit -m \"$msg\""

while true; do
    read -p "Do you want to Push? [Y/N]" yn
    case $yn in
        [Yy]* ) git push; git gc; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done