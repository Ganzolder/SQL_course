"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os

start = input('Прежде чем программа начнет заполнение базы данных, убедитесь что имена файлов для заполняемых таблиц '
      'строго соответсвуют названиям таблиц БД.\n\nНапример: если имя таблицы в БД table_name, то имя файла с данными должно быть '
      'table_name.csv.\n\nНажите Enter для продолжения.')

if start == '':

    try:
        conn = psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password='12345'
        )
        conn.autocommit = True



        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

        # Извлекаем названия таблиц из результата запроса
        table_names = cursor.fetchall()

        # Задаем имена файлов, которые ищем
        db_files = []

        for t_name in table_names:
            file_name = f'{t_name[0]}.csv'
            db_files.append(file_name)

        db_files.sort()

        file_path = ''

        # Получаем текущую директорию проекта
        project_directory = os.path.abspath(os.path.dirname(__file__))

        j = 0
        # Идем по всем файлам в директории проекта и найдите нужный файл
        for db_file_name in db_files:

            for root, dirs, files in os.walk(project_directory):
                if db_file_name in files:
                    file_path = os.path.join(root, db_file_name)
                    break

            # Формируем путь для загрузки
            data = file_path

            for db_file_name in files:

                if db_file_name in data:

                    files_for_upload = {db_file_name.split('.')[0]: data}
                    break

            try:
                rows = 0
                for key, value in files_for_upload.items():

                    with open(value, 'r') as db:

                        db_reader = csv.reader(db)

                        with conn.cursor() as cur:

                            for string in db_reader:

                                if '_id' in string[0]:
                                    pass
                                else:
                                    num_of_args = len(string) - 1
                                    sql_comm = f'INSERT INTO {key} VALUES ({"%s, " * num_of_args}%s)'
                                    cur.execute(sql_comm, string)
                                    rows += 1
                            print(f'{db_file_name} загружен. Добавлено {rows} строк')
            finally:
                pass
    except:
        print('Не смог подключиться к БД')
else:
    pass



