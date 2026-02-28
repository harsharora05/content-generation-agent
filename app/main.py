from server import app
from uvicorn import run

def main():
    run(app=app,host="127.0.0.1",port=8000)    


if __name__ == "__main__":
    main()
