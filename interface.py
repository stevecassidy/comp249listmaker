"""
  Database interface layer for the listmaker application.
"""

__author__ = 'steve'


def create_tables(db):
    """Create database tables for the likes application
    given a database connection 'db'.
    Removes any existing data that might be in the
    database."""

    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS lists")
    cursor.execute("""
    CREATE TABLE lists (
              listname text,
              description text
           )
    """)

    cursor.execute("DROP TABLE IF EXISTS things")
    cursor.execute("""
    CREATE TABLE things (
              listname text,
              thing text
           )
    """)


def new_list(db, listname, description):
    """Create a new list"""

    cursor = db.cursor()
    cursor.execute("INSERT INTO lists (listname, description) VALUES (?, ?)", (listname, description))
    db.commit()


def store_thing(db, listname, thing):
    """Store a new list entry in the database,
    return True if it works, False if the list doesn't exist """

    cursor = db.cursor()
    # check that list exists
    cursor.execute("SELECT listname FROM lists WHERE listname=?", (listname,))

    if cursor.fetchone() is None:
        return False

    cursor.execute("INSERT INTO things (listname, thing) VALUES (?, ?)", (listname, thing))
    db.commit()

    return True


def get_lists(db):
    """Return a list of the listnames we know about"""

    cursor = db.cursor()
    cursor.execute("SELECT listname FROM lists")
    result = []
    for row in cursor:
        result.append(row[0])
    return result

def get_list_description(db, listname):
    """Return the description of a list, '' if this isn't a valid list name"""

    cursor = db.cursor()
    cursor.execute("SELECT description FROM lists WHERE listname=?", (listname,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return ''


def get_things(db, listname):
    """Return a list of things from the database given a name"""

    cursor = db.cursor()
    cursor.execute("SELECT thing FROM things WHERE listname=?", (listname,))
    result = []
    for row in cursor:
        result.append(row[0])
    return result