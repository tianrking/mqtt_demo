from flask import Flask, request, jsonify,render_template
import json
import base64
import pandas as pd
import datetime as dt
import time

app = Flask(__name__)
app.debug = True
 
 
@app.route('/tt',methods=['post'])
def add_stu():
    if  not request.data: 
        return ('fail')
    uplink_data = request.data.decode('utf-8')
    uplink_data = json.loads(uplink_data) 
    decode_data = base64.b64decode(uplink_data['payload'])
    print(uplink_data)
    print(decode_data.decode("utf-8"))
    
    try:
        df = pd.read_excel("test.xlsx",sheet_Value="Sheet1",header=0)
        df = df.append({'Time':dt.datetime.now(),'Value':1},ignore_index=True)
        df = df.set_index('Time')
        df.to_excel("test.xlsx")
    except:
        df = pd.DataFrame({'Time':[],'Value':[]})
        df = df.set_index('Time')
        df.to_excel('test.xlsx')

    print(data.shape)
    return 1

 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234)
