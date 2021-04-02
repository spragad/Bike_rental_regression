from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

file = open('bike_rent.pkl','rb')
model = pickle.load(file)
file.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        #Date
        date=request.form["Date"]
        date=pd.to_datetime(date, format="%Y-%m-%dT%H:%M")
        Rented_month=int(date.month)
        Rented_day=int(date.day)
        Rented_Hour=int(date.hour)
        
        #Temperature
        temp=request.form["Temperature"]
        day_temp=float(temp)
        if day_temp < 1.26666667:
            #Low
            Temperature_Low	= 1
            Temperature_Medium = 0	
            
        elif day_temp >= 1.26666667 and day_temp < 20.33333333:
            #Medium
            Temperature_Low	= 0
            Temperature_Medium = 1
            
        elif day_temp >=  20.33333333 :
            #High
            Temperature_Low	= 0
            Temperature_Medium = 0
        
        #Humidity
        humid=request.form["Humidity"]
        hum=float(humid)
        if hum == 0:
            #No_Humidity
            Humidity_No_Humidity=1
            Humidity_Low=0
            Humidity_Medium=0
            
        elif hum > 0 and hum < 32.66666667:
            #Low
            Humidity_No_Humidity=0
            Humidity_Low=1
            Humidity_Medium=0
            
        elif hum >= 32.66666667 and hum < 65.33333333:
            #Medium
            Humidity_No_Humidity=0
            Humidity_Low=0
            Humidity_Medium=1
            
        elif hum >= 65.33333333:
            #High
            Humidity_No_Humidity=0
            Humidity_Low=0
            Humidity_Medium=0
        
        #Wind Speed
        wind=request.form["Wind speed"]
        winds=float(wind)
        if winds == 0:
            #No_wind
            Wind_speed_No_wind=1
            Wind_speed_Low=0	
            Wind_speed_Medium=0	
            
        elif winds > 0 and winds < 2.46666667:
            #Low
            Wind_speed_No_wind=0
            Wind_speed_Low=1
            Wind_speed_Medium=0
            
        elif winds >= 2.46666667 and winds < 4.93333333:
            #Medium
            Wind_speed_No_wind=0
            Wind_speed_Low=0	
            Wind_speed_Medium=1
            
        elif winds >= 4.93333333:
            #High
            Wind_speed_No_wind=0
            Wind_speed_Low=0	
            Wind_speed_Medium=0
        
        #Visibility
        visible=request.form["Visibility"]
        vis=float(visible)
        if vis < 684.66666667:
            #Low
            visibility_Low=1
            visibility_Medium=0
            
        elif vis >= 684.66666667 and vis < 1342.33333333:
            #Medium
            visibility_Low=0
            visibility_Medium=1
            
        elif vis >= 1342.33333333 :
            #High
            visibility_Low=0
            visibility_Medium=0
        
        #Dew Point Temperature
        dewpt=request.form["Dew Point Temperature"]
        dew=float(dewpt)
        if dew < -11.33333333:
             #Low
             Dew_temp_Low=1
             Dew_temp_Medium=0
             
        elif dew >= -11.33333333 and dew < 7.93333333:
            #Medium
             Dew_temp_Low=0
             Dew_temp_Medium=1
             
        elif dew >=  7.93333333 :
            #High
             Dew_temp_Low=0
             Dew_temp_Medium=0            
        
        #Solar Radiation
        solarad=request.form["Solar Radiation"]
        sun=float(solarad)
        if sun == 0:
            #No_sun
            Solar_radiation_No_sun=1
            Solar_radiation_Low=0
            Solar_radiation_Medium=0
            
        elif sun > 0 and sun < 1.17333333:
            #Low
            Solar_radiation_No_sun=0
            Solar_radiation_Low=1
            Solar_radiation_Medium=0
            
        elif sun >= 1.17333333 and sun < 2.34666667:
            #Medium
            Solar_radiation_No_sun=0
            Solar_radiation_Low=0
            Solar_radiation_Medium=1
            
        elif sun >= 2.34666667:
            #High
            Solar_radiation_No_sun=0
            Solar_radiation_Low=0
            Solar_radiation_Medium=0
            
        #Snowfall
        snowfall=request.form["Snow fall"]
        snow=float(snowfall)
        if snow == 0:
            #No_snow
            Snowfall_No_snow=1
            Snowfall_Low=0
            Snowfall_Medium=0
            
        elif snow > 0 and snow < 2.93333333:
            #Low
            Snowfall_No_snow=0
            Snowfall_Low=1
            Snowfall_Medium=0
            
        elif snow >= 2.93333333 and snow < 5.86666667:
            #Medium
            Snowfall_No_snow=0
            Snowfall_Low=0
            Snowfall_Medium=1
            
        elif snow >= 5.86666667:
            #High
            Snowfall_No_snow=0
            Snowfall_Low=0
            Snowfall_Medium=0
        
        #Rainfall
        rainfall=request.form["Rain fall"]
        rain=float(rainfall)
        if rain == 0:
            #No_Rain
            Rainfall_No_Rain=1
            Rainfall_Low=0
            Rainfall_Medium=0
        elif rain > 0 and rain < 11.66666667:
            #Low
            Rainfall_No_Rain=0
            Rainfall_Low=1
            Rainfall_Medium=0
            
        elif rain >= 11.66666667 and rain < 23.33333333:
            #Medium
            Rainfall_No_Rain=0
            Rainfall_Low=0
            Rainfall_Medium=1
            
        elif rain >= 23.33333333:
            #High
            Rainfall_No_Rain=0
            Rainfall_Low=0
            Rainfall_Medium=0

        #Functioning Day
        fnday=request.form["Functioning Day"]
        fn=str(fnday)
        if fn=='Yes':
            Functioning_day_Yes=1
        else:
            Functioning_day_Yes=0
            
        #Season
        season=request.form["Season"]
        sn=str(season)
        if sn == 'Summer':
            Spring=0
            Summer=1	
            Winter=0
            
        elif sn == 'Spring':
            Spring=1
            Summer=0	
            Winter=0
            
        elif sn == 'Winter':
            Spring=0
            Summer=0	
            Winter=1
            
        else:
            Spring=0
            Summer=0	
            Winter=0
        
        #Holiday
        holiday=request.form["Holiday"]
        hd=str(holiday)
        if hd=='Yes':
            Holiday=1
        else:
            Holiday=0
            
        prediction=model.predict([[Rented_month, Rented_day, Rented_Hour, Temperature_Low, Temperature_Medium,
                                    Humidity_Low, Humidity_Medium, Humidity_No_Humidity, Wind_speed_Low,
                                    Wind_speed_Medium, Wind_speed_No_wind, visibility_Low, visibility_Medium,
                                    Dew_temp_Low, Dew_temp_Medium, Solar_radiation_Low, Solar_radiation_Medium,
                                    Solar_radiation_No_sun, Rainfall_Low, Rainfall_Medium, Rainfall_No_Rain,
                                    Snowfall_Low, Snowfall_Medium, Snowfall_No_snow, Spring, Summer, Winter,
                                    Holiday, Functioning_day_Yes]])

        output=int(prediction[0])

        return render_template('home.html',prediction_text="Expected number of bike to be rented : {}".format(output))

    return render_template("home.html")        
        
if __name__ == "__main__":
    app.run(debug=True)
