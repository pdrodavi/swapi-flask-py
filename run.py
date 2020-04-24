from app import app

if __name__ == '__main__':
  from app import *
  app.run(debug=True, host='0.0.0.0', port=5000)