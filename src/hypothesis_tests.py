from scipy.stats import ttest_ind, chi2_contingency
import pandas as pd


def run_ttest(group_a, group_b):
    stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy="omit"
    )

    return {
        "test": "Independent t-test",
        "p_value": p_value
    }


def run_chi2(contingency_table):
    stat, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return {
        "test": "Chi-squared",
        "p_value": p_value
    }