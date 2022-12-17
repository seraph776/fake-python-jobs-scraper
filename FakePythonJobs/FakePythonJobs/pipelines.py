import sqlite3


class SQLiteDatabasePipeline:

    def __init__(self):
        self.conn = sqlite3.connect('jobs.db')
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        SQL = """CREATE TABLE IF NOT EXISTS jobs_tb(
                    date_posted TEXT,
                    job_name TEXT,
                    company TEXT,
                    location TEXT,                    
                    apply_link TEXT        
        )"""
        self.curr.execute(SQL)

    def store_db(self, item):
        SQL = """INSERT INTO jobs_tb VALUES (?,?,?,?,?)"""
        self.curr.execute(SQL, (item['date_posted'],
                                item['job_name'],
                                item['company'],
                                item['location'],
                                item['apply_link']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
