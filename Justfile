set dotenv-load

[no-cd]
default:
	@just solve 1 input.txt
	@just solve 2 input.txt

[no-cd]
input day:
	curl --cookie session=$SESSION_COOKIE https://adventofcode.com/2022/day/{{day}}/input > input.txt

[no-cd]
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

[no-cd]
test:
	python3 test.py

[no-cd]
solve part file:
	@echo -n {{file}} '(Part {{part}}): '
	@python3 main.py --part={{part}} {{file}}
