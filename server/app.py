from factory import createApp
from extensions import db

# instance of createApp
app = createApp()
  
with app.app_context():
#     from app import db
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    
    