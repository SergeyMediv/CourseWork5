from cls import Employer, Vacancy
from cfg import config
from utils import create_database, save_data_to_database

if __name__ == '__main__':
    employers_ids = ['1226057',  # Полимер-Групп
                     '4820587',  # REWOOD
                     '9794662',  # Автошкола РЕАЛ
                     '4562617',  # Интеллектуальные Коммунальные Системы
                     '2131486',  # Веб-Агентство Текстерра
                     '5746940',  # ООО Сталепромышленная компания Регион
                     '1440228',  # Акзо Нобель Лакокраска
                     '3196647',  # КАМПО
                     '713307',  # Карболит
                     '7564'  # ВКС-International House
                     ]

    params = config()

    create_database("cw_5", params)
    save_data_to_database(employers_ids, "cw_5", params)
