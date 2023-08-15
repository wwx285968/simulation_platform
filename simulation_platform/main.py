import uvicorn
from simulation_platform.apis.restful_api import app


def main():
    uvicorn.run(app, host="127.0.0.1", port=9000)


if __name__ == "__main__":
    main()
