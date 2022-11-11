install:
    pip install --upgrade pip &&\
    pip install -r requirements.txt

test: 
    python -m pytest -vv api_test.py

lint: 
    pylint --disable=R,C main.py

format:
    black*.py

run: 
    python main.py