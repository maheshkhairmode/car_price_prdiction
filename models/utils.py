import pandas as pd 
import numpy as np 
import pickle 
import json


class CarPrice():
    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,engine_location,
                 wheel_base,length,width,height,curb_weight,bore,stroke,compression_ratio,horsepower,peak_rpm,
                 city_mpg,highway_mpg,fuel_system,make,body_style,drive_wheels,engine_type,num_of_cylinders):

        self.symboling=symboling
        self.normalized_losses=normalized_losses
        self.fuel_type=fuel_type
        self.aspiration=aspiration
        self.num_of_doors=num_of_doors
        self.engine_location=engine_location
        self.wheel_base=wheel_base
        self.length=length
        self.width=width
        self.height=height
        self.curb_weight=curb_weight
        self.bore=bore
        self.stroke=stroke
        self.compression_ratio=compression_ratio
        self.horsepower=horsepower
        self.peak_rpm=peak_rpm
        self.city_mpg=city_mpg
        self.highway_mpg=highway_mpg
        self.fuel_system="fuel-system_"+fuel_system
        self.make="make_"+make
        self.body_style="body-style_"+body_style
        self.drive_wheels="drive-wheels_"+drive_wheels
        self.engine_type="engine-type_"+engine_type
        self.num_of_cylinders="num-of-cylinders_"+num_of_cylinders
        
         







    

    def Load_model(self):

        with open("models/linear_autos_model1.pkl","rb")as f:
            self.linear_model=pickle.load(f)

        with open("models/project_data_autos1","r")as f:
            self.project_data=json.load(f)

    def Predict_car_price(self):

        self.Load_model()

        index_value1=self.project_data["columns"].index(self.fuel_system)
        index_value2=self.project_data["columns"].index(self.make)
        index_value3=self.project_data["columns"].index(self.body_style)
        index_value4=self.project_data["columns"].index(self.drive_wheels)
        index_value5=self.project_data["columns"].index(self.engine_type)
        index_value6=self.project_data["columns"].index(self.num_of_cylinders)
        


        array=np.zeros(len(self.project_data["columns"]))

        array[0]=self.symboling
        array[1]=self.normalized_losses
        array[2]=self.project_data["fuel-type"][self.fuel_type]
        array[3]=self.project_data["aspiration"][self.aspiration]
        array[4]=self.project_data["num-of-doors"][self.num_of_doors]
        array[5]=self.project_data["engine-location"][self.engine_location]
        array[6]=self.wheel_base
        array[7]=self.length
        array[8]=self.width
        array[9]=self.height
        array[10]=self.curb_weight
        array[11]=self.bore
        array[12]=self.stroke
        array[13]=self.compression_ratio
        array[14]=self.horsepower
        array[15]=self.peak_rpm
        array[16]=self.city_mpg
        array[17]=self.highway_mpg
        array[index_value1]=1
        array[index_value2]=1
        array[index_value3]=1
        array[index_value4]=1
        array[index_value5]=1
        array[index_value6]=1
        

        prediction=self.linear_model.predict([array])[0]
        print("predicted price of car is",prediction)

        return np.around(prediction,2)


if __name__=="__main__":

    symboling=3
    normalized_losses=115
    fuel_type="gas"
    aspiration="turbo"
    num_of_doors="two"
    engine_location="front"
    wheel_base=88.6
    length=168.8
    width=64.1
    height=48
    curb_weight=2548
    bore=3.47
    stroke=2.68
    compression_ratio=9
    horsepower=111
    peak_rpm=5000
    city_mpg=21
    highway_mpg=27


    fuel_system="mpfi"
    make="bmw"
    body_style="convertible"
    drive_wheels="fwd"
    engine_type="ohcv"
    num_of_cylinders="six"
    

    pred=CarPrice(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,engine_location,
                 wheel_base,length,width,height,curb_weight,bore,stroke,compression_ratio,horsepower,peak_rpm,
                 city_mpg,highway_mpg,fuel_system,make,body_style,drive_wheels,engine_type,num_of_cylinders)

    
    predicted_price=pred.Predict_car_price()
    print("predicted_price",predicted_price)










