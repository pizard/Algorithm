from Programmers.Alignment import H_Index
from Programmers.Alignment import H_Index_BinarySearch
from Programmers.Alignment import H_index_Efficient
import random

# command : pytest --benchmark-only main.py

testData = [random.randint(0, 1000) for r in range(random.randint(0, 1000))]

ITERATIONS = 300
ROUNDS = 100

def test_H_Index_Efficient(benchmark):
    benchmark.pedantic(H_index_Efficient.solution, kwargs={'citations' : testData}, iterations=ITERATIONS, rounds=ROUNDS)
#    benchmark(H_index_Efficient.solution, testData)

def test_H_Index(benchmark):
    benchmark.pedantic(H_Index.solution, kwargs={'citations' : testData}, iterations=ITERATIONS, rounds=ROUNDS)
#    benchmark(H_Index.solution, testData)

def test_H_Index_BinarySearch(benchmark):
    benchmark.pedantic(H_Index_BinarySearch.solution, kwargs={'citations' : testData}, iterations=ITERATIONS, rounds=ROUNDS)
#    benchmark(H_Index_BinarySearch.solution, testData)