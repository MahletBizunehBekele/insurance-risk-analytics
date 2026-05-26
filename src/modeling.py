from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

import numpy as np


def evaluate_regression(y_true, preds):

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            preds
        )
    )

    r2 = r2_score(
        y_true,
        preds
    )

    return {
        "RMSE": rmse,
        "R2": r2
    }


def evaluate_classification(y_true, preds):

    return {

        "Accuracy":
            accuracy_score(
                y_true,
                preds
            ),

        "Precision":
            precision_score(
                y_true,
                preds
            ),

        "Recall":
            recall_score(
                y_true,
                preds
            ),

        "F1":
            f1_score(
                y_true,
                preds
            )
    }