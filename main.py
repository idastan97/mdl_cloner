from flask import Flask, request, jsonify, Response, render_template, redirect

app = Flask(__name__)


@app.route('/')
def page():
    print("adgadgdg")
    # app.send_static_file('./index.html')
    return render_template('index.html')
    # return redirect("http://www.example.com", code=302)


@app.route('/login', methods=["POST"])
def login():
    print(request.get_data())
    # print(request.get_json())
    # print(request)
    return render_template('index.html')


if __name__ == "__main__":
    # _thread.start_new_thread(app.run, (), {'host': '0.0.0.0'})
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))