import MySQLdb

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



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q2(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q3(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q4(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q5(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q6(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q7(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q8(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q9(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q10(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q11(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q12(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q13(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q14(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data

    def q15(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        return data


if __name__ == "__main__":
    ## ToDO: Init the DbStreamer object
    db_streamer = None

    print(db_streamer.q0())
