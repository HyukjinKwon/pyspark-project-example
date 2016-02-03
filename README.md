# pyspark-project-example [![Build Status](https://travis-ci.org/HyukjinKwon/pyspark-project-example.svg?branch=master)](https://travis-ci.org/HyukjinKwon/pyspark-project-example) [![codecov.io](https://codecov.io/github/HyukjinKwon/pyspark-project-example/coverage.svg?branch=master)](https://codecov.io/github/HyukjinKwon/pyspark-project-example?branch=master)

An example for PySpark based project.

## Prerequisites

- JDK 7 (as the test downloads Spark 1.6.0, which dropped JDK 6 support)

## Test

- For test in your local, just run below:

    ```
    ./dev/run_tests
    ```

    This contains some codes to download Spark 1.6.0 to run tests. So, it is okay to run the script without some specific modifications.

## Warnings

- As currently PySpark cannot be installed via `pip install` due to [this issue](https://issues.apache.org/jira/browse/SPARK-1267),
Spark has to be installed and `SPARK_HOME="your Spark path"` and `PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH` should be set in order to use this library outside after building.
