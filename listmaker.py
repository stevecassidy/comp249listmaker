from bottle import Bottle, request, redirect, template, HTTPError

from database import COMP249Db
from interface import *

app = Bottle()

@app.route('/')
def index():
    """Home page"""

    db = COMP249Db()

    info = dict()
    # get the list of likes from the database
    info['lists'] = get_lists(db)

    return template('lists.tpl', info)

@app.route('/list/<listname>')
def showlist(listname):
    """Generate a page for this list"""

    db = COMP249Db()
    info = dict()
    info['things'] = get_things(db, listname)
    info['listname'] = listname
    info['description'] = get_list_description(db, listname)

    return template('showlist.tpl', info)


@app.post('/list')
def create_list():
    """Create a new list"""

    listname = request.forms.get('listname')
    description = request.forms.get('description')

    if listname and description:
        db = COMP249Db()
        new_list(db, listname, description)
        redirect("/list/"+listname)
    else:
        return redirect('/')


@app.post('/list/<listname>')
def add_to_list(listname):
    """Add a new thing to a list"""

    # get the form field
    thing = request.forms.get('thing')

    if thing:
        db = COMP249Db()
        if not store_thing(db, listname, thing):
            raise HTTPError(status=404, body="Page not found")

    return redirect('/list/' + listname)
    

# Extend this application to support a JSON API
# write views for the following routes that return JSON
# you can decide the format of the JSON that is exchanged

# @app.route('/api/list')
# returns a JSON list of listnames

# @app.route('/api/list/<listname>')
# returns a JSON list of the contents of this list

# @app.post('/api/list')
# create a new list, accept a JSON document that contains
#  the name and description of the list

# @app.post('/api/list/<listname>')
# add a new thing to the named list
#   accepts a JSON document containing the thing



if __name__ == "__main__":
    dbase = COMP249Db()
    create_tables(dbase)
    app.run()