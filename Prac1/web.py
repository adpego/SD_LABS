from flask import Flask, send_from_directory
import os
app = Flask(__name__, static_url_path='')


'''@app.route('/')
def hello():
    tree = dict(name='files', children=[])
    try: lst = os.listdir('files')
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join('files', name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=fn))
    return tree

@app.route('/<name>')
def hello_name(name):
    return "Hello "+name'''

@app.route("/")
def static_dir():
    path = "files/"
    aux = ""
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            aux += name + "<br>"
    return aux

if __name__ == '__main__':
    app.run(debug=True)

