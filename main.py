import matplotlib.pyplot as plt
from collections import Counter

import sampling as sm
import hypothesis_tests as test
import movie_sample as movies

if __name__ == "__main__":

    filename = 'combined_data_1.csv'
    random_movies1 = movies.select_random_movies1('movie_titles.csv', 10) #array of movie ids before 2000s
    random_movies2 = movies.select_random_movies2('movie_titles.csv', 10) #array of movie ids after 2000s

    pop_mean1 = sm.population_mean1() #pop1 = movies before 2000
    pop_mean2 = sm.population_mean2() #pop2 = movies after 2000

    print(pop_mean1)
    print(pop_mean2)
    pop_variance1 = sm.population_variance1(pop_mean1)
    pop_variance2 = sm.population_variance2(pop_mean2)
    print(pop_variance1)
    print(pop_variance2)
    # pop_variance = sm.1(dataset, pop_mean)

    sample_dataset1 = sm.get_sample(filename, random_movies1)
    sample_dataset2 = sm.get_sample(filename, random_movies2)

    # ratings_array = [int(d["Rating"]) for d in sample_dataset]
    # ratings_array_2 = [int(d["Rating"]) for d in sample_dataset]

    null_hypothesis_mean = 3

    print("-----------------------Z-TEST 1 SAMPLE----------------------")
    print("Movies before 2000 had an average rating at least %d"%null_hypothesis_mean)
    # #TEST 1 Single Sample left-tailed ztest
    test.left_tailed_z_test(sample_dataset1, null_hypothesis_mean, pop_variance1, 0.05)
    print("---------------------------------------------")
    # #TEST 2 Single Sample right-tailed ztest
    print("Movies before 2000 had an average rating at most %d"%null_hypothesis_mean)
    test.right_tailed_z_test(sample_dataset1, null_hypothesis_mean, pop_variance1, 0.05)
    print("---------------------------------------------")
    # #TEST 3 Single Sample two-tailed ztest
    print("Movies before 2000 had an average rating equal to %d"%null_hypothesis_mean)
    test.two_tailed_z_test(sample_dataset1, null_hypothesis_mean, pop_variance1, 0.05)
    print("\n-----------------------Z-TEST 2 SAMPLE----------------------")
    #TEST 4 Single Sample pvalue ztest
    # p_value_test(ratings_array, null_hypothesis_mean, pop_variance, alpha=0.05)
    #TEST 5 Two Sample ztest
    print("Movies were equally rated before and after year 2000")
    test.two_sample_test(sample_dataset1, sample_dataset2, 0.05)
    print("\n-----------------------T-TEST----------------------")
    # #TEST 5 Two Sample ztest
    test.two_sample_t_value_test(sample_dataset1, sample_dataset2, alpha=0.01)
