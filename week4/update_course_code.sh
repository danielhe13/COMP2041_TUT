#! /bin/dash

for file in "$@"
do

  if [ -d "$file" ]
  then
    # this recursively runs update_course_code.sh on all the files and subdirectories in the current directory
    ./"$0" "$file"/* "$file"/.[!.]* "$file"/..?*
  fi

  if [ ! -f "$file" ]
  then
    continue
  fi

  temporary_file="$(mktemp)"

  sed -E 's/COMP2041/COMP2042/g; s/COMP9044/COMP9042/g' "$file" > "$temporary_file" &&
  mv "$temporary_file" "$file"

  rm -f "$temporary_file"

done
