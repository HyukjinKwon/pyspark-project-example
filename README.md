# pyspark-project-example [![Build Status](https://travis-ci.org/HyukjinKwon/pyspark-project-example.svg?branch=master)](https://travis-ci.org/HyukjinKwon/pyspark-project-example) [![codecov.io](https://codecov.io/github/HyukjinKwon/pyspark-project-example/coverage.svg?branch=master)](https://codecov.io/github/HyukjinKwon/pyspark-project-example?branch=master)

A simple example for PySpark based project.

## Prerequisites

- JDK (>=7) (as the local test downloads Spark 1.6.0, which dropped JDK 6 support)

- Python PEP 8 (for checking code-style in local test)

  ```bash
  pip install pep8
  ```
- Python Py4J == 0.9.0 (for initiating Spark in local test)

  ```bash
  pip install -r requirements.txt
  ```

## Test

- For test in your local, just run below:

    ```
    ./dev/run_tests
    ```

    This contains some codes to download Spark 1.6.0 to run tests. So, it is okay to run the script without some specific modifications.

## Warnings

- As currently PySpark cannot be installed via `pip install` due to [this issue](https://issues.apache.org/jira/browse/SPARK-1267),
Spark has to be installed and `SPARK_HOME="your Spark path"` and `PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH` should be set in order to use this library outside after building.
