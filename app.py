from flask import Flask, request, render_template, make_response


app = Flask(__name__)

@app.route('/hello/get/', methods=['GET'])
def hello_get():
    return render_template('hello.html', params=request.args.items())

@app.route('/hello/post/', methods=['POST'])
def hello_post():
    return render_template('hello.html', params=request.form.items())


@app.route('/hello/cookie/')
def cookies():
    try:
        cookie_counter = int(request.cookies.get('page_visits'))
    except Exception:
        cookie_counter = 0

    cookie_counter += 1
    
    resp = make_response(render_template('cookies.html', cookies=cookie_counter))
    resp.set_cookie('page_visits', str(cookie_counter))
    
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=80)