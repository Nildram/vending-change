# Change Calculator

## Overview

The `change_calculator` python package provides functionality to calculate a specified
amount of change from a given set of coins (the 'float').

**For convenience, the package has been wrapped in a REST API with a swagger UI to allow
it to be accessed and tested from a browser. A version of the library can be found running
[here](https://oracle-vending.nw.r.appspot.com/swagger/).**

Note that there is a limit to the coins denominations, change amount and total 'float' of between
0 and 500,000 (to account for the largest current worldwide denomination of 500,000 VND).
The upper limit is currently hard coded, but could be added as a configurable value (for
example in the initialise API call). Coin counts must also be positive numbers.

## How do I use the package?

### Installation from source

The `change_calculator` package can be installed from source as follows:

```bash
python3 setup.py install
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
in terms of both time and space complexity than that used to calculate change for
non-canonical coin systems. With this in mind, you may want to use a canonical calculator
if you know the coin system is canonical. The canonical calculator is not recommended
for use with non-canonical coin systems as it will fail to calculate change for certain
combinations of coins and requested change.

Full documentation of public APIs included in the codebase.

```python
from change_calculator import Calculators

help(Calculators)
calculator = Calculators.non_canonical()
help(calculator)
```

## Testing the library via the REST API

For convenience, the library has been wrapped in a REST API with a swagger UI to allow it
to be tested via a browser. In order to provide access without having to build or run
this yourself, a version of the package with the REST wrapper can been provided
[here](https://oracle-vending.nw.r.appspot.com/swagger/).

If you would rather run the code locally, there are two supported ways to do this:

### Run from docker

The `Dockerfile` provided along with this `README.md` will build an image to run the
application with the REST API and swagger UI included. This is the recommended way
to run the REST application locally.

```
docker build . -t change-calculator
docker run -p 5000:80 -e WEB_CONCURRENCY="1" change-calculator
```

You can then browse to `http://127.0.0.1:5000/swagger/` to view the swagger UI and
interact with the code.

### Run natively

Requires the following pre-requisites:

* `python3 (minimum 3.6)`
* `pip3`

Once the pre-requisites are satisfied, install the necessary package dependencies
and run the application with the REST interface.

```bash
pip3 install -r requirements.txt
export FLASK_APP=flask_app.py && python -m flask run
```

You can then browse to `http://127.0.0.1:5000/swagger/` to view the swagger UI and
interact with the code.

## Implementation discussion

### API

For all API calls, coins are represented using a dictionary. A list could have been used
with each index being the value of a coin, but the use of a duct is much easier to manage
and debug. Also, the dict will take up less space, assuming the average case includes
many coins of each denomination and will avoid us having to sum all the instances of each
coin before use in the algorithm.

Additionally, for the `add_coins` API call, the use of a container rather than a single
numeric value for the parameter allows multiple coins to be added with a single call as
opposed to having to repeat the call for each coin in a batch. Of course, it's still
possible to add coins one at a time using the container.

### Algorithm

An initial TDD approach led me to develop a greedy algorithm to calculate the change.
This works for UK denominations, as specified in the exercise and any others that are
considered canonical. This would be sufficient to meet the definition of done in terms of
functionality for the exercise (along with the API and test harness).

Although the product is currently for the UK market, I chose to take some time to work on
a more general algorithm that could be used for any coin system, canonical and non-canonical.
Note that, in the real world, I would stick with the initial requirement.

A brute force approach could be used to gather all coin combinations for the given set and
select the minimum one from there. Such an algorithm would have an exponential complexity of
*O(S<sup>n</sup>)*, where *S* is the amount and *n* is the number of coin denominations.
Space complexity would be *O(n)*.

We can improve on the brute force approach by using dynamic programming. Here the complexity
can be reduced to *O(S* * *n)*, where *S* is the amount and *n* is the number of coin
denominations. The space complexity increases slightly over the brute force approach to
*O(S* * *2)* due to the use of a mamoization table.

### Dependency injection

Dependency injection is used to decouple the components and provide the calculator with
the necessary algorithm depending on whether the coin system used is canonical or
non-canonical.

Furthermore, I added a simple static factory method (`create`) to the `ChangeAlgorithm`
class to allow it to do the creation of subclasses based on the `canonical_coin_system`
parameter. A further improvement on this would be to nest the subclasses within the
factory method to disallow direct access. After implementing the
`ChangeCalculatorFactory` class to perform the top level dependency injection, the
`ChangeAlgorithm` factory method could have be removed entirely (dealt with by the
`ChangeCalculatorFactory` itself). I chose to leave the original implementation as is,
leaving `ChangeCalculatorFactory` ignorant to the subclasses, which I believe is the
cleaner approach.

### Testing

Unit tests are provided for all classes, with the top level API tested as an integration
test, using the standard `unittest` framework. Following the standard 'test pyramid',
there are more class and function level unit tests than there are integration tests.

Unit tests can be run with the following command from the root of the source directory:

```python3 -m unittest discover test```

For a larger, more complex codebase with multiple components I would consider including
BDD tests for higher level component and integration tests using an appropriate framework
that supports gherkin syntax.

### Documentation

All classes include `docstrings` to document their public methods. A future improvement
would be to generate more accessible documentation from these `docstrings` with a tool such
as sphinx.