from app import app

@app.route('/health')
def health():
    return "tech Challenge"  + " Version 1.0" 