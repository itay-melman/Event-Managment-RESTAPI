from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from routes import EventListResource, EventResource
from scheduler import scheduler

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db.init_app(app)
with app.app_context():
    db.create_all()

api.add_resource(EventListResource, '/events')
api.add_resource(EventResource, '/events/<int:event_id>')

if __name__ == '__main__':
    scheduler.start()
    app.run(debug=True)
