from flask import Flask, reender_template

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return """
        <form action="/login" method="post">
            Pasword:<input type="password" name="password"><br>
            <input type="submit">
        </form>
        """
    return 


if __name__ == "__main__":
    app.run(port=8000)
