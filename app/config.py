class Config:
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///events.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATE_LIMITS = {"create_event": "5 per minute", "other": "20 per minute"}
	
