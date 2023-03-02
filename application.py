from flask import Flask
from Housing.logger import logging
import sys 
from Housing.exception import HousingException

application= Flask(__name__)
app=application


@app.route("/",methods=['GET' , 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging info")
    return "Starting Machine Learning Project"


if __name__=="__main__":
    app.run(debug=True)
    