import pandas as pd
import os
import datetime as datetime

dataframe = pd.read_csv(
    'C:\\master_run\\data_history\\marketplaces\\wildberries\\sent_to\\2024-02-03\\df_final_stock.csv')
dataframe = dataframe.drop_duplicates(subset=['offer_id', 'warehouse_id']).reset_index(drop=True)
dataframe

history_dir = 'C://master_run//data_history//marketplaces//wildberries//sent_to//'
output_file = 'df_final_stock.csv'


def save_to_csv(dataframe, history_dir, output_file, result_dir='', is_only_history=True):
    """Сохранение датафрейма в указанную дирректорию маркетплейса

    Аргументы:
        dataframe (pd.DataFrame): датафрейм, который требуется сохранить
        output_dir (str): дирректория в которую сохраняем исторические данные
        output_file (str): название файла

    Примечания:
        - Если дирректория с указанным маркетплейсом отсутствует,
            то она создается
        - Если дирректория с текущей датой отсутствует, то она создается
        - Ежедневно создается одна директория с текущей датой,
            в которую помещаются исторические записи по определенному
            мпркетплейсу
    """
    logger.info(f"Начинаю сохранять данные в файл {output_file}")

    current_date = datetime.now().strftime("%Y-%m-%d")
    directory = f"{history_dir}{current_date}/"

    is_dir_mp = os.path.isdir(result_dir)
    if not is_only_history:
        if not is_dir_mp:
            logger.debug(f"Создаю дирректорию {result_dir}")
            os.makedirs(result_dir)

        is_dir_mp = os.path.isdir(history_dir)
        if not is_dir_mp:
            logger.debug(f"Создаю дирректорию {history_dir}")
            os.makedirs(history_dir)

        is_dir = os.path.isdir(directory)
        if not is_dir:
            logger.debug(f"Создаю дирректорию {directory}")
            os.makedirs(directory)

        dataframe.to_csv(f"{directory}{output_file}", index=False)
        dataframe.to_csv(f"{result_dir}{output_file}", index=False)

    else:
        is_dir = os.path.isdir(directory)
        if not is_dir:
            logger.debug(f"Создаю дирректорию {directory}")
            os.makedirs(directory)
        if os.path.isfile(f"{directory}{output_file}"):
            logger.debug(f"IN FILE: {directory}")
            past_df = pd.read_csv(
                'C:\\master_run\\data_history\\marketplaces\\wildberries\\sent_to\\2024-02-03\\df_final_stock.csv')
            past_df["offer_id"] = past_df["offer_id"].astype(str)
            if past_df.empty:
                dataframe = dataframe.drop_duplicates(subset=['offer_id', 'warehouse_id']).reset_index(drop=True)
                dataframe.to_csv(f"{directory}{output_file}", index=False)

            else:
                logger.debug(f"IN ELSE: {directory}")
                result_update_df = pd.concat([past_df,
                                              dataframe], axis=0).drop_duplicates(subset=['offer_id',
                                                                                          'warehouse_id']).reset_index(
                    drop=True)
                result_update_df.to_csv(f"{directory}{output_file}", index=False)

        elif not os.path.isfile(f"{directory}{output_file}"):
            dataframe.to_csv(f"{directory}{output_file}", index=False)


save_to_csv(dataframe, history_dir, output_file, result_dir='', is_only_history=True)
