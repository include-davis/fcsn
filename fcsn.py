import os
from events_page import app

# if __name__ == '__main__':
#     app.run(debug=True, port=33507) # Allows 'python flaskblog.py' to be run flask with debugger continuously

port = int(os.environ.get('PORT', 5000)) 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)