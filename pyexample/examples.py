from pyspark import SparkContext


def example():
    sc = SparkContext('local')
    words = sc.parallelize(["scala", "java", "hadoop", "spark", "akka"])
    return words.count()
