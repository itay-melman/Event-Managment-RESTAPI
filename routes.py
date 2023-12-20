from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Event
from flask_limiter import Limiter

limiter = Limiter(key_func=get_remote_address)

class EventListResource(Resource):
    @limiter.limit("5 per minute")
    def get(self):
        events = Event.query.all()
        return jsonify(events=[event.serialize() for event in events])

    @limiter.limit("20 per minute")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name of the event')
        parser.add_argument('location', type=str, required=True, help='Location of the event')
        args = parser.parse_args()

        new_event = Event(name=args['name'], location=args['location'])
        db.session.add(new_event)
        db.session.commit()

        return jsonify(message="Event created successfully")

class EventResource(Resource):
    @limiter.limit("5 per minute")
    def get(self, event_id):
        event = Event.query.get(event_id)
        if event:
            return jsonify(event.serialize())
        return jsonify(message="Event not found"), 404

    @limiter.limit("20 per minute")
    def put(self, event_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name of the event')
        parser.add_argument('location', type=str, required=True, help='Location of the event')
        args = parser.parse_args()

        event = Event.query.get(event_id)
        if event:
            event.name = args['name']
            event.location = args['location']
            db.session.commit()
            return jsonify(message="Event updated successfully")

        return jsonify(message="Event not found"), 404

    @limiter.limit("20 per minute")
    def delete(self, event_id):
        event = Event.query.get(event_id)
        if event:
            db.session.delete(event)
            db.session.commit()
            return jsonify(message="Event deleted successfully")

        return jsonify(message="Event not found"), 404
