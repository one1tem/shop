from shop import app

@app.route("/")
def home():
    return "<p>Willkommen auf meinem Online-Shop</p>"
