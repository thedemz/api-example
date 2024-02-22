import flask
import pathlib
import sys


def abs_path():
    return pathlib.Path(__file__)


def root_dir():
    return abs_path().parent


def route_get_root():
    status = 200  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }  # https://www.iana.org/assignments/media-types/application/json
    body = '{"api": "0.0.1", "message": "hello"}'
    response = (body, status, headers)

    return response  # https://tedboy.github.io/flask/_modules/flask/app.html#Flask.make_response


def route_post_echo():
    # https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data
    data = flask.request.get_data(
        as_text=True
    )  # https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.get_data

    status = 200
    headers = {"Content-Type": "text/plain; charset=utf-8"}  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
    response = (data, status, headers)

    return response


def register_routes(server):
    server.add_url_rule("/", view_func=route_get_root, methods=["GET"])
    server.add_url_rule("/echo", view_func=route_post_echo, methods=["POST"])


def main():
    srv = flask.Flask("server", static_url_path=None, static_folder=None)
    register_routes(srv)
    srv.run(host="127.0.0.1", port=8080)  # This will block and catch KeyboardInterrupt


if __name__ == "__main__":
    dir_path = root_dir()
    print(dir_path)

    try:
        print("To test the endpoints use (the -vv is optional):")
        print(r"curl -w '\n' -X GET 127.0.0.1:8080 -vv")
        print(r"curl -w '\n' -X POST -H 'Content-Type: text/plain; charset=utf-8' -d 'sending some plain text' 127.0.0.1:8080/echo -vv")
        main()
    except Exception as e:
        print(e)
        sys.exit()
