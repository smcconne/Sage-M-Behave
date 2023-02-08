# Behave automation

## Dependencies

### Install the following dependencies before running tests:

```
Python 3.10.9
selenium 4.8.0
webdriver_manager 3.8.5
Faker 16.6.1
behave 1.2.6
```

## Running tests

### First you will have to register the standard user by running this command:

```
behave --tags="@register"
```

Users are frequently deleted, so re-run the above command if the tests stop working.

The website often goes offline; just wait 5 mins and it will come back up.

### Run the smoke test with this command:

```
behave --tags="@smoke_test"
```
