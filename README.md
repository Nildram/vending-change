# Change Calculator

## Overview

The `change_calculator` python package provides functionality to calculate change for a
specified amount from a given set of coins (the 'float').

At it's core the package contains

**For convenience, the library has been wrapped in a REST API with a swagger UI to allow
it to be accessed and tested more easily. A version of the library can be found running
[here](https://oracle-vending.nw.r.appspot.com/swagger/).**

## How do I use the package?

### Installation from source

The `change_calculator` package can be installed from source as follows:

```bash
$ python3 setup.py install
```

### Using the package

Here's a quick example of using a calculator to calculate some change from a given
collection of coins.

```python
from change_calculator import Calculators

calculator = Calculators.non_canonical()

calculator.initialise({1:10, 2:10, 5:10, 10:10, 20:10, 50:10})
calculator.add_coins({1:10, 100:10, 200:10})
change = calculator.get_change(388)
```

The package contains calculators for both canonical and non-canonical coin systems.
The algorithm used to calculate change for canonical coins systems is more efficient
in terms of both complexity and space that that used to calculate change for
non-canonical coin systems. With this in mind, you may want to use a canonical calculator
if you know the coin system is canonical. The canonical calculator is not recommended
for use with non-canonical coin systems as it may fail to calculate change for certain
combinations of coins and amount.

Full documentation of public APIs included in the codebase.

```python
from change_calculator import Calculators

help(Calculators)
calculator = Calculators.non_canonical()
help(calculator)
```

## I just want to play with the code, how do I that?

For convenience, the library has been wrapped in a REST API with a swagger UI to allow it
to be tested via a browser. In order to provide access without having to build or run
this yourself, a version of the package with the REST wrapper can been provided
[here](https://oracle-vending.nw.r.appspot.com/swagger/).

If you would rather run the code locally, there are two supported ways to do this:

### Run natively

Requires the following pre-requisites:

* `python3`
* `pip3`

Once the pre-requisites are satisfied, install the necessary package dependencies
and run the application with the REST interface.

```bash
$ pip3 install -r requirements.txt
$ export FLASK_APP=hello.py && python -m flask run
```

You can then browse to the `http://127.0.0.1:5000/swagger/` to view the swagger UI and interact with the code.

### Run from docker

The `Dockerfile` provided along with this `README.md` will build an image to run the
application with the REST API and swagger UI included. This is the recommended way
to run the REST application
locally.

```
docker build . -t change-calculator
docker run -p 5000:80 -e WEB_CONCURRENCY="1" change-calculator
```

You can then browse to the `http://127.0.0.1:5000/swagger/` to view the swagger UI and interact with the code.

## Implementation discussion

### API
