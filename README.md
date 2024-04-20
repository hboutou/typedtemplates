A simple pattern to define typed templates in python projects.


### Pros:
1) A central location for reading templates and generating templated-based content (SQL or anything really).
2) Generating content becomes a single function call with typed parameters.
3) Typehints in your favorite IDE.
4) Stop the speard of boilerplate especialy when a template is used in multiple places.
5) Modifying template parameters is easier since the IDE shows everywhere the template is used and the params passed.


### Cons:
1) None

### Run example

1) clone repo and cd into the repo root folder
```
git clone github.com/hboutou/typedtemplates.git
cd typedtemplates
```
2) create virtual environment and activate it
```
python -m venv .venv
source .venv/bin/activate
```
3) install the project package

```
pip install .
```

4) run
```
python app.py
```


