from flask import Flask
from services.db import init_db
from routes import init_routes  # Import routes to avoid circular dependencies

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)

    # Application configuration
    app.config["MONGO_URI"] = "mongodb://user_mongodb:27017/userdb"

    # Initialize database and routes
    init_db(app)
    init_routes(app)

    # Optional: Print all registered routes for debugging
    print("Registered Routes:")
    for rule in app.url_map.iter_rules():
         print(rule)

    return app

if __name__ == "__main__":
    # Create the application instance and run the development server
    app = create_app()
    app.run(host="0.0.0.0", port=8081)