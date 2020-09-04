from database.database import Database
import psycopg2.extras as extras


class DatabaseCursor(Database):
    def batch_insert(self, sql, data_lst, page_size=100):
        conn = self.get_connection()
        curs = conn.cursor()
        print('Beginning batch insertion for {} entries and page size {}'.format(len(data_lst), page_size))
        extras.execute_values(curs, sql, data_lst, page_size=page_size)
        conn.commit()
        print('Successfully committed transaction for {} entries'.format(len(data_lst)))
        conn.close()
