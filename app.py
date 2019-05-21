from flask import Flask
from flask_restful import Api, Resource
import smbus
app = Flask(__name__)
api = Api(app)

class heartRate(Resource):
    def get(self):
        bus = smbus.SMBus(2)
        curBPM = bus.read_byte_data(0xA0,0x50)
        retJson = {"curBPM":curBPM}
        return retJson, 200

api.add_resource(heartRate, "/")
# api.add_resource(addTwoNumber, "/addTwoNumber")
# api.add_resource(sumAll, "/sumAll")
# api.add_resource(isPalindrome, "/isPalindrome")
# api.add_resource(divideTwoNum, "/divideTwoNum")

if __name__ =="__main__":
    app.run(debug=True)