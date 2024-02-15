from cfg import EMPLOYERS_URL
from cls import Employer, Vacancy

if __name__ == '__main__':
    hh_key = EMPLOYERS_URL
    employers_ids = ['1226057',
                     '4820587',
                     '9794662',
                     '4562617',
                     '2131486',
                     '3414',
                     '1440228',
                     '3196647',
                     '713307',
                     '7564'
                     ]

    employers_list = Employer.initiate_from_hh(employers_ids)
    print(employers_list[9].employer_name)

    vacancies_list = Vacancy.initiate_from_hh(employers_list[9].employer_id)
    for x in vacancies_list:
        print(x.currency)
