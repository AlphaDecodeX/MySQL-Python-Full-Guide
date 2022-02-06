import MySQLdb
# File Csv_Sql_Tables.py is a python script present in the same directory
# Which is used to make SQL Tables after pre-data processing using Pandas in Python.. 
# Questions Start from Here .....
class DbStreamer:

    @staticmethod
    def get_rows(data):
        data_rows = []
        for row in data:
            data_rows.append(row)
        return data_rows


    def __init__(self, host, user, password, database):
        self.conn = MySQLdb.Connection(host=host,
                                       user=user,
                                       passwd=password,
                                       db=database,
                                       charset="utf8",
                                       use_unicode=True)
        _cursor = self.conn.cursor()
        return

    def get_connection(self):
        return self.conn

    def close_connection(self):
        self.conn.commit()
        self.conn.close()
        return
    
    def get_tables(self):
        sql = "SHOW TABLES;"
        
        _cursor = self.conn.cursor()
        _cursor.execute(sql)
        data = _cursor.fetchall()

        return data

    def q0(self):
        sql = "SELECT DATE('2020-01-23');"
        _cursor = self.conn.cursor()
        _cursor.execute(sql)
        data = _cursor.fetchall()
        return data

    # TODO: Add your logic for each of the questions in the corresponding methods provided below. Each method should return a list of tuples/rows without the header.
    def q1(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("SELECT id FROM movies ORDER BY movies.vote_count DESC LIMIT 5")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q2(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("SELECT id FROM movies ORDER BY movies.budget DESC LIMIT 1")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q3(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("SELECT movie, runtime from movies where (runtime = (select max(runtime) from movies)) OR (runtime = (select min(runtime) from movies where runtime > 0) ) LIMIT 2")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q4(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute('select id , release_date from movies where (release_date = (select Max(release_date) from movies)) OR (release_date = (select Min(release_date) from movies where release_date > 0) ) order by release_date ASC limit 2;')    
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q5(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("select movie as movies_name, budget from movies where (popularity = (select Max(popularity) from movies))")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q6(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("select id from companies_movies where (movie = (select movie from movies where popularity = (select Max(popularity) from movies)))")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q7(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("SELECT count(*) as NUM FROM companies_movies GROUP BY movie HAVING NUM > 2")    
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return [len(data)+1]

    def q8(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("Select movie from ( select movie, (budget-revenue) as substraction from movies ) as child ORDER BY substraction DESC LIMIT 1")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q9(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("Select movie, genre from genres_movies where movie = (Select movie from ( SELECT movie, genre, count(*) as NUM FROM genres_movies GROUP BY movie ) as child ORDER BY NUM DESC LIMIT 1)")

        for row in _cursor:
            data.append(row)

        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q10(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("Select x.id from (select p.id, count(m.movie) as Total from movies as m, companies_movies as p where m.movie = p.movie group by p.id order by Total DESC limit 4 ) as x LIMIT 1")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q11(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("select distinct company from companies_movies as p , movies as m where m.movie = p.movie order by vote_count desc limit 19")
        for row in _cursor:
            data.append(row)

        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q12(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("select distinct cm.id from companies_movies as cm where cm.id not in ( select distinct(p.id) from movies as m, companies_movies as p where m.movie = p.movie and vote_average < 7 )")
        for row in _cursor:
            data.append(row)

        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q13(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q14(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("select genre, AVG(vote_count) from movies as m , genres_movies as g where m.movie = g.movie group by genre")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q15(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------
        data = []
        _cursor.execute("select m.movie, g.genre from movies as m, genres_movies as g where g.movie = m.movie  Order by budget DESC limit 20")
        for row in _cursor:
            data.append(row)


        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data


if __name__ == "__main__":
    ## ToDO: Init the DbStreamer object
    db_streamer = DbStreamer('localhost', 'root', '1552454fghLPSK@$', 'moviesDb')
    print(db_streamer.q0())
    print(db_streamer.q1())
    print(db_streamer.q2())
    print(db_streamer.q3())
    print(db_streamer.q4())
    print(db_streamer.q5())
    print(db_streamer.q6())
    print(db_streamer.q7())
    print(db_streamer.q8())
    print(db_streamer.q15())
