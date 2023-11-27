import numpy as np
import scipy.stats as stats
from scipy.stats import norm
import math
from statsmodels.sandbox.stats.runs import runstest_1samp
from statsmodels.stats.descriptivestats import sign_test
from termcolor import colored


def left_tailed_z_test(sample_dataset, null_hypothesis_mean, pop_variance, alpha):
    z_critical = norm.ppf(alpha)
    SEM = pop_variance/math.pow(len(sample_dataset),0.5)
    z_value = (np.mean(sample_dataset)-null_hypothesis_mean)/SEM
    if z_value < z_critical:
        print(colored("left tailed test at alpha %.2f: Hypothesis rejected | H0: mean >= %d"%(alpha,null_hypothesis_mean), 'green'))
    else:
        print(colored("left tailed test at alpha %.2f: Hypothesis accepted | H0: mean >= %d"%(alpha,null_hypothesis_mean), 'green'))

def right_tailed_z_test(sample_dataset, null_hypothesis_mean, pop_variance, alpha):
    z_critical = norm.ppf(1-alpha)
    SEM = pop_variance/math.pow(len(sample_dataset),0.5)
    z_value = (np.mean(sample_dataset)-null_hypothesis_mean)/SEM
    if z_value > z_critical:
        print(colored("right tailed test at alpha %.2f: Hypothesis rejected | H0: mean <= %d"%(alpha,null_hypothesis_mean), 'green'))
    else:
        print(colored("right tailed test at alpha %.2f: Hypothesis accepted | H0: mean <= %d"%(alpha,null_hypothesis_mean), 'green'))

def two_tailed_z_test(sample_dataset, null_hypothesis_mean, pop_variance, alpha):
    z_critical = norm.ppf(1 - alpha/2)
    SEM = pop_variance/math.pow(len(sample_dataset),0.5)
    z_value = (np.mean(sample_dataset)-null_hypothesis_mean)/SEM
    if abs(z_value) > z_critical:
        print(colored("two tailed test at alpha %.2f: Hypothesis rejected | H0: mean = %d"%(alpha,null_hypothesis_mean), 'green'))
    else:
        print(colored("two tailed test at alpha %.2f: Hypothesis accepted | H0: mean = %d"%(alpha,null_hypothesis_mean), 'green'))


def two_sample_test(sample_dataset, sample_dataset_2, alpha):
    SE1 = np.std(sample_dataset, ddof=1)
    SE2 = np.std(sample_dataset_2, ddof=1)
    n1 = len(sample_dataset)
    n2 = len(sample_dataset_2)
    SE = math.pow(SE1**2/n1 + SE2**2/n2, 0.5)
    z_critical = norm.ppf(1 - alpha/2)

    z_value = (np.mean(sample_dataset)-np.mean(sample_dataset_2))/SE

    if abs(z_value) > z_critical:
        print(colored("two sample z test at alpha %.2f: Hypothesis rejected | H0: mean1 = mean2"%alpha, 'green'))
    else:
        print(colored("two sample z test at alpha %.2f: Hypothesis accepted | H0: mean1 = mean2"%alpha, 'green'))

def two_sample_t_value_test(sample_dataset, sample_dataset_2, alpha):
    df = 10
    t_critical = stats.t.ppf(1 - alpha / 2, df)

    SE1 = np.std(sample_dataset)**2/len(sample_dataset)
    SE2 = np.std(sample_dataset_2)**2/len(sample_dataset_2)
    SE = math.pow(SE1+SE2, 0.5)
    t_value = (np.mean(sample_dataset)-np.mean(sample_dataset_2))/SE

    if abs(t_value) > t_critical:
        print(colored("two sample t test at alpha %.2f: Hypothesis rejected | H0: mean1 = mean2"%alpha, 'green'))
    else:
        print(colored("two sample t test at alpha %.2f: Hypothesis accepted | H0: mean1 = mean2"%alpha, 'green'))

def runs_test(sample_data):
    median_value = np.median(sample_data)
    binary_data = [1 if x > median_value else 0 for x in sample_data]

    runs_count = 0
    current_run = None

    for bit in binary_data:
        if bit != current_run:
            runs_count += 1
            current_run = bit

    print("Number of runs: ", runs_count)
    result = runstest_1samp(binary_data, cutoff='median')

    print(colored("Result at alpha = 0.05:", "The sample is not random" if result[1] < 0.05 else "The sample is random", 'green'))

def sign_test_one_sample(sample_data, hyp_median, alpha):
    _, p_value = sign_test(sample_data, mu0=hyp_median)

    if p_value <= alpha:
        print(colored("one sample sign test at alpha %.2f: Hypothesis rejected | H0: median=%.1f"%(alpha, hyp_median), 'green'))
    else:
        print(colored("one sample sign test at alpha %.2f: Hypothesis accepted | H0: median=%.1f"%(alpha, hyp_median), 'green'))