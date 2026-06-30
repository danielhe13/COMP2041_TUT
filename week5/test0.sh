#! /usr/bin/env dash

# ==============================================================================
# test0.sh
# Test the svc-show command.
#
# Written by: Dylan Brotherston <d.brotherston@unsw.edu.au>
# Date: 2026-06-26
# For COMP2041/9044 Assignment 1
# ==============================================================================

# Add the current directory to the PATH so scripts
# can still be executed from it after we cd
PATH="$PATH:$(pwd)"

# Create a temporary directory for our solution.
test_dir="$(mktemp -d)"

# Create a temporary directory for the reference solution.
ref_dir="$(mktemp -d)"

# Create some files to hold output.
expected_output="$(mktemp)"
actual_output="$(mktemp)"

# Remove the temporary directories and files when the test is done.
trap 'rm "$expected_output" "$actual_output" -rf "$test_dir" "$ref_dir"' INT HUP QUIT TERM EXIT

# Create svc repository

cd "$ref_dir" || exit 1
2041 svc-init > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-init > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Create a simple file.

cd "$ref_dir" || exit 1
echo "line 1" > a

cd "$test_dir" || exit 1
echo "line 1" > a

# add a file to the repository staging area

cd "$ref_dir" || exit 1
2041 svc-add a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-add a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# commit the file to the repository history

cd "$ref_dir" || exit 1
2041 svc-commit -m 'first commit' > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-commit -m 'first commit' > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Update the file.

cd "$ref_dir" || exit 1
echo "line 2" >> a

cd "$test_dir" || exit 1
echo "line 2" >> a

# update the file in the repository staging area

cd "$ref_dir" || exit 1
2041 svc-add a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-add a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Update the file again.

cd "$ref_dir" || exit 1
echo "line 3" >> a

cd "$test_dir" || exit 1
echo "line 3" >> a

# Check that the file that has been commited hasn't been updated

cd "$ref_dir" || exit 1
2041 svc-show 0:a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show 0:a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Check that the file that is in the staging area hasn't been updated

cd "$ref_dir" || exit 1
2041 svc-show :a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show :a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Check that invalid uses of svc-show give an error

# incorrect argument

cd "$ref_dir" || exit 1
2041 svc-show a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# unknown commit number

cd "$ref_dir" || exit 1
2041 svc-show 2:a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show 2:a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# unknown commit name

cd "$ref_dir" || exit 1
2041 svc-show hello:a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show hello:a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# file not found in commit

cd "$ref_dir" || exit 1
2041 svc-show 0:b > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show 0:b > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# file not found in index

cd "$ref_dir" || exit 1
2041 svc-show :b > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show :b > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# no arguments

cd "$ref_dir" || exit 1
2041 svc-show > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# too many arguments

cd "$ref_dir" || exit 1
2041 svc-show 0:a 0:a > "$expected_output" 2>&1

cd "$test_dir" || exit 1
svc-show 0:a 0:a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0