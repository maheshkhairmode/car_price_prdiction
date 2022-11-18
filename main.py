from distutils .command.config import config
from flask import Flask,render_template,request,jsonify
from models.utils import CarPrice
import config


app= Flask(__name__)

@app.route("/")
def hello_velocity():

    return render_template("index.html")

@app.route("/car_price",methods=["POST","GET"])
def predict_car_price():

    if request.method=="POST":

        symboling=int(request.form.get("symboling"))
        normalized_losses=int(request.form.get("normalized_losses"))
        fuel_type=request.form.get("fuel_type")
        aspiration=request.form.get("aspiration")
        num_of_doors=request.form.get("num_of_doors")
        engine_location=request.form.get("engine_location")
        wheel_base=float(request.form.get("wheel_base"))
        length=float(request.form.get("length"))
        width=float(request.form.get("width"))
        height=int(request.form.get("height"))
        curb_weight=int(request.form.get("curb_weight"))
        bore=float(request.form.get("bore"))
        stroke=float(request.form.get("stroke"))
        compression_ratio=int(request.form.get("compression_ratio"))
        horsepower=int(request.form.get("horsepower"))
        peak_rpm=int(request.form.get("peak_rpm"))
        city_mpg=int(request.form.get("city_mpg"))
        highway_mpg=int(request.form.get("highway_mpg"))
        fuel_system=request.form.get("fuel_system")
        make=request.form.get("make")
        body_style=request.form.get("body_style")
        drive_wheels=request.form.get("drive_wheels")
        engine_type=request.form.get("engine_type")
        num_of_cylinders=request.form.get("num_of_cylinders")


        pred=CarPrice(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,engine_location,
                 wheel_base,length,width,height,curb_weight,bore,stroke,compression_ratio,horsepower,peak_rpm,
                 city_mpg,highway_mpg,fuel_system,make,body_style,drive_wheels,engine_type,num_of_cylinders)

    
        predicted_price=pred.Predict_car_price()

        return render_template("index.html",prediction=predicted_price)


if __name__=="__main__":

    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)
    


