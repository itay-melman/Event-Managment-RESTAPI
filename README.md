## Event Management RestAPI

This project implements a RESTful API for managing events with additional features.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Setup

1. Clone the repo
2. Navigate to the project directory
3. Install dependencies from requirements.txt
4. Run the application: run the file main.py

## API Endpoints
Schedule a new event:

Endpoint: POST /events
Request body: JSON with event details (title, location, venue, date_time)
Retrieve a list of all scheduled events:

Endpoint: GET /events
Retrieve details of a specific event:

Endpoint: GET /events/<event_id>
Update details of a specific event:

Endpoint: PUT /events/<event_id>
Request body: JSON with updated event details
Delete a specific event:

Endpoint: DELETE /events/<event_id>
Batch Operations:

Endpoint: POST /events/batch
Request body: JSON array for batch operations (create, update, delete)
Subscribe to an event:

Endpoint: POST /events/<event_id>/subscribe
Request body: JSON with subscriber details
