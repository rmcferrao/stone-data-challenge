import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix

def confusion_matrix_plot(y_true, y_pred):
    fig, ax = plt.subplots()

    sns.heatmap(confusion_matrix(y_true, y_pred), ax=ax, annot=True, fmt="d", cmap="Blues")

    ax.set(title="Confusion Matrix", xlabel="Predicted", ylabel="Actual")

    return fig, ax

def return_key_if_contains_value(dictionary, my_value):
    for key, value in dictionary.items():
        if my_value in value:
            return key


def confusion_matrix_plot(y_true, y_pred):
    fig, ax = plt.subplots()

    sns.heatmap(
        confusion_matrix(y_true, y_pred), ax=ax, annot=True, fmt="d", cmap="Blues"
    )

    ax.set(title="Confusion Matrix", xlabel="Previsao", ylabel="Atual")

    return fig, ax


def grid_results(model, param_1, param_2):
    df_results = pd.DataFrame(model.cv_results_)

    return (
        df_results.pivot(
            index=f"param_{param_1}",
            columns=f"param_{param_2}",
            values="mean_test_score",
        )
        .round(3)
        .style.background_gradient("Blues", axis=None)
    )
