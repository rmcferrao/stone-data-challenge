import pandas as pd
import pickle

def from_sorted_df_split_between_constant_and_timeseries_attributes(
    df, constant_attributes, timeseries_attributes, id_column_name="id"
):

    unique_index = df[id_column_name].unique()
    unique_index.sort()

    df_constant_attributes = pd.DataFrame(
        columns=constant_attributes, index=unique_index.astype(int)
    )

    company_ids_in_df = df[id_column_name].to_numpy()
    history_loan = dict.fromkeys(set(unique_index))
    history_loan.update(dict(history_loan))
    i = 0

    for idx in unique_index:
        idx_boolean_list = company_ids_in_df == idx
        tmp_df = df.loc[idx_boolean_list]
        df_constant_attributes.loc[idx] = tmp_df[constant_attributes].iloc[-1]
        history_loan[idx] = tmp_df[timeseries_attributes].reset_index(drop=True)

    return df_constant_attributes, history_loan


def check_if_list_of_ints_start_0_and_is_sorted(int_list):
    ideal_list = list(range(0, max(int_list) + 1))

    if len(ideal_list) != len(int_list):
        return False

    if sorted(int_list) == ideal_list:
        return True
    else:
        return False


if __name__ == "__main__":
    test = pd.read_parquet("data/raw/test.parquet")
    train = pd.read_parquet("data/raw/train.parquet")

    constant_attributes = [
        "desembolso",
        "vencimento",
        "valor_emprestado",
        "pgto_diario_esperado",
        "subsegmento",
        "y",
    ]

    timeseries_attributes = [
        "dia",
        "dias_pos_desembolso",
        "divida_total",
        "divida_principal",
        "pagamento_diario",
        "amortizacao_principal_diario",
        "transacionado",
    ]

    train.sort_values(by=["id", "dias_pos_desembolso"], axis=0, inplace=True)
    test.sort_values(by=["id", "dias_pos_desembolso"], axis=0, inplace=True)

    (
        train_loans,
        train_dict_loan_timeseries,
    ) = from_sorted_df_split_between_constant_and_timeseries_attributes(
        train, constant_attributes, timeseries_attributes
    )

    (
        test_loans,
        test_dict_loan_timeseries,
    ) = from_sorted_df_split_between_constant_and_timeseries_attributes(
        test, constant_attributes[:-1], timeseries_attributes
    )

    # Saving data into `data/processed` folder dict as pickle and dtaframe as csv
    with open("data/processed/train_timeseries_attributes.p", "wb") as fp:
        pickle.dump(train_dict_loan_timeseries, fp, protocol=pickle.HIGHEST_PROTOCOL)

    train_loans.to_csv(
        "data/processed/train_constant_attributes.csv", index=True, index_label="id"
    )

    with open("data/processed/test_timeseries_attributes.p", "wb") as fp:
        pickle.dump(test_dict_loan_timeseries, fp, protocol=pickle.HIGHEST_PROTOCOL)

    test_loans.to_csv(
        "data/processed/test_constant_attributes.csv", index=True, index_label="id"
    )