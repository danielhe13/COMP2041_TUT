#!/bin/dash

# =========================================
# test0.sh
# testing turnip-add command
#
# Written by Wayne z5555555
# On date 17/03/2025
# For COMP2041/9044 Assignment 1
# =========================================


# Add the current directory to the PATH so scripts can still be executed from it after we cd
PATH="$PATH:$(pwd)"

test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1
2041 fetch turnip

ref_dir="$(mktemp -d)"
cd "$ref_dir" || exit 1
2041 fetch turnip

expected_stdout="$(mktemp)"
expected_stderr="$(mktemp)"
actual_stdout="$(mktemp)"
actual_stderr="$(mktemp)"

trap "rm $expected_stdout $expected_stderr $actual_stdout $actual_stderr -r $test_dir $ref_dir" EXIT INT QUIT TERM

# Testing turnip-add

cd "$ref_dir" || exit 1
2041 turnip-add lab1 multiply.tests > "$expected_stdout" 2> "$expected_stderr"
ref_exit_code=$?

cd "$test_dir" || exit 1
turnip-add lab1 multiply.tests > "$actual_stdout" 2> "$actual_stderr"
exit_code=$?

if ! diff "$expected_stdout" "$actual_stdout" > /dev/null; then
    echo "Failed test - stdout differs"
    diff "$expected_stdout" "$actual_stdout"
    exit 1
fi

if ! diff "$expected_stderr" "$actual_stderr" > /dev/null; then
    echo "Failed test - stderr differs"
    diff "$expected_stderr" "$actual_stderr"
    exit 1
fi

if [ "$exit_code" -ne "$ref_exit_code" ]; then
    echo "Failed test - exit code differs"
    echo "Expected: $ref_exit_code"
    echo "Got: $exit_code"
    exit 1
fi

# Testing submition

cd "$ref_dir" || exit 1
2041 turnip-add lab1 multiply.tests > "$expected_stdout" 2> "$expected_stderr"
ref_exit_code=$?

cd "$test_dir" || exit 1
turnip-add lab1 multiply.tests > "$actual_stdout" 2> "$actual_stderr"
exit_code=$?

if ! diff "$expected_stdout" "$actual_stdout" > /dev/null; then
    echo "Failed test - stdout differs"
    diff "$expected_stdout" "$actual_stdout"
    exit 1
fi

if ! diff "$expected_stderr" "$actual_stderr" > /dev/null; then
    echo "Failed test - stderr differs"
    diff "$expected_stderr" "$actual_stderr"
    exit 1
fi

if [ "$exit_code" -ne "$ref_exit_code" ]; then
    echo "Failed test - exit code differs"
    echo "Expected: $ref_exit_code"
    echo "Got: $exit_code"
    exit 1
fi
