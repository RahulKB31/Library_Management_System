from app import create_app

app = create_app()  # Create and configure the Flask app

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application with debug mode enabled
