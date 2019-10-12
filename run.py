from app import app
import os, bottle

if __name__ == '__main__':
    bottle.TEMPLATE_PATH.insert(0, 'app/views/')  
    app.run(host='localhost', port=8080, debug=True, reloader=True)
        