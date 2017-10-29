
.PHONY: test run

run:
	        @python3 run.py $(filename)

test:
	        @python3 -m unittest discover 
