# activation_code.py
"""
a simple example of creating activation codes.
"""

import random
import string
import connect_mysql
import connect_mongodb

# digits and letters type:str
field = string.digits + string.letters

# get random from field using random.choice
def get_random(number):
    """
    Get number random from field using random.choice.
    :param number: int
    :return:str
    """
    s = ''
    for i in xrange(number):
        s = s + str(random.choice(field))
    return  s

# get random from field using random.sample
def get_random_2(number):
    """
    Get number random from field using random.sample.
    :param number: int
    :return: str
    """
    return ''.join(random.sample(field, number))

# get group randoms from get_random(number)
def get_group(group, number):
    """
    Get group random numbers from get_random(number).
    :param group: int
    :param number: int
    :return: str
    """
    return '-'.join([get_random_2(number) for i in xrange(group)])

# get how number of group number from get_group(group, number)
def generate(group, number, n):
    """
    Get n-group random number from get_group(group,number).
    how number
    how groups with number
    how n with group
    :param group: int
    :param number: int
    :param n: int
    :return: list
    """
    return [get_group(group, number) for i in xrange(n)]

# save activation_code into mysql
def save_to_mysql(lst):
    """
    save lst with activation_codes into mysql
    :param lst: list
    :return:
    """
    # init database
    db = connect_mysql.connect_mysql('localhost', '3306', 'python', 'root', '829157')
    # get connect
    db_connect = db.get_connect
    # whether or not db_connect is None
    if db_connect is None:
        print 'connect mysql database error'
        return None
    db_cursor = db.get_cursor(db_connect)
    # whether or not db_cursor is None
    if db_cursor is None:
        print 'get cursor error'
        return None
    # sql
    sql = 'insert into activation_code(code) values(%s)'
    # execute
    for item in lst:
        params = (item,)
        result = db_cursor.execute(sql, params)
        db_connect.commit()
    # close
    db.close_all(db_cursor, db_connect)

# save activation_code into mongodb
def save_to_mongodb(lst):
    """
    save lst with activation_codes into mongodb
    :param lst: list
    :return:
    """
    # deaulft using host='localhost' and port=27107
    db_object = connect_mongodb.connect_mongodb()
    # mongodb'connect
    connect = db_object.get_connect()
    # whether or not db is None
    if connect is None:
        print 'connect to mongodb database error'
        return None
    # db.python of mongodb'database
    database = connect['python']
    # batch insert
    index = 0
    lt = []
    for item in lst:
        # index must to convert string
        dt = {str(index): item}
        lt.append(dt)
        index += 1
    database.activation_code.insert(lt)

if __name__ == '__main__':
    # save_to_mysql(generate(4, 6, 10))
    save_to_mongodb(generate(4, 6, 10))

