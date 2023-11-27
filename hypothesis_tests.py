import numpy as np
import scipy.stats as stats
from scipy.stats import norm
import math
from statsmodels.sandbox.stats.runs import runstest_1samp
from statsmodels.stats.descriptivestats import sign_test


def left_tailed_z_test(sample_dataset, null_hypothesis_mean, pop_variance, alpha):
    z_critical = norm.ppf(alpha)
    SEM = pop_variance/math.pow(len(sample_dataset),0.5)
    z_value = (np.mean(sample_dataset)-null_hypothesis_mean)/SEM
    if z_value < z_critical:
        print("left tailed test at alpha %.2f: Hypothesis rejected | H0: mean >= %d"%(alpha,null_hypothesis_mean))
    else:
        print("left tailed test at alpha %.2f: Hypothesis accepted | H0: mean >= %d"%(alpha,null_hypothesis_mean))

def right_tailed_z_test(sample_dataset, null_hypothesis_mean, pop_variance, alpha):
    z_critical = norm.ppf(1-alpha)
    SEM = pop_variance/math.pow(len(sample_dataset),0.5)
    z_value = (np.mean(sample_dataset)-null_hypothesis_mean)/SEM
    if z_value > z_critical:
        print("right tailed test at alpha %.2f: Hypothesis rejected | H0: mean <= %d"%(alpha,null_hypothesis_mean))
    else:
        print("right tailed test at alpha %.2f: Hypothesis accepted | H0: mean <= %d"%(alpha,null_hypothesis_mean))

def two_tailed_z_test(sample_dataset, null_hypothesis_mean, pop_variance, alpha):
    z_critical = norm.ppf(1 - alpha/2)
    SEM = pop_variance/math.pow(len(sample_dataset),0.5)
    z_value = (np.mean(sample_dataset)-null_hypothesis_mean)/SEM
    if abs(z_value) > z_critical:
        print("two tailed test at alpha %.2f: Hypothesis rejected | H0: mean = %d"%(alpha,null_hypothesis_mean))
    else:
        print("two tailed test at alpha %.2f: Hypothesis accepted | H0: mean = %d"%(alpha,null_hypothesis_mean))


def two_sample_test(sample_dataset, sample_dataset_2, alpha):
    SE1 = np.std(sample_dataset, ddof=1)
    SE2 = np.std(sample_dataset_2, ddof=1)
    n1 = len(sample_dataset)
    n2 = len(sample_dataset_2)
    SE = math.pow(SE1**2/n1 + SE2**2/n2, 0.5)
    z_critical = norm.ppf(1 - alpha/2)

    z_value = (np.mean(sample_dataset)-np.mean(sample_dataset_2))/SE

    if abs(z_value) > z_critical:
        print("two sample z test at alpha %.2f: Hypothesis rejected | H0: mean1 = mean2"%alpha)
    else:
        print("two sample z test at alpha %.2f: Hypothesis accepted | H0: mean1 = mean2"%alpha)

def two_sample_t_value_test(sample_dataset, sample_dataset_2, alpha):
    df = 10
    t_critical = stats.t.ppf(1 - alpha / 2, df)

    SE1 = np.std(sample_dataset)**2/len(sample_dataset)
    SE2 = np.std(sample_dataset_2)**2/len(sample_dataset_2)
    SE = math.pow(SE1+SE2, 0.5)
    t_value = (np.mean(sample_dataset)-np.mean(sample_dataset_2))/SE

    if abs(t_value) > t_critical:
        print("two sample t test at alpha %.2f: Hypothesis rejected | H0: mean1 = mean2"%alpha)
    else:
        print("two sample t test at alpha %.2f: Hypothesis accepted | H0: mean1 = mean2"%alpha)

def runs_test(sample_data):
    median_value = np.median(sample_data)
    binary_data = [1 if x > median_value else 0 for x in sample_data]
    result = runstest_1samp(binary_data)
    print("Result:", "The sample is not random" if result[1] < 0.05 else "The sample is random")

def sign_test_one_sample(sample_data):
    median_value = np.median(sample_data)
    sign_test(sample_data, mu0=median_value)