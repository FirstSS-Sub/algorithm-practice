# Makefile for AtCoder tasks

# Variables for login
USERNAME = yogurrrt
PASSWORD = 3110Runassas

.PHONY: login
# Login to AtCoder
login:
	oj login -u $(USERNAME) -p $(PASSWORD) "https://atcoder.jp/"

.PHONY: problem
# Download problems
problem:
	oj-prepare "https://atcoder.jp/contests/$(id)"

.PHONY: test
# Run tests
test:
	oj t -c "python3 $(id)/main.py" -d $(id)/test

.PHONY: submit
# Submit code
submit:
	oj s "https://atcoder.jp/contests/$(shell echo $(id) | cut -d'_' -f1)/tasks/$(id)" $(id)/main.py -l 5078