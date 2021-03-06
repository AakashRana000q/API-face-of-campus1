import pickle
import base64
import io
from PIL import Image
from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['POST'])
def predict():
    user_data = pickle.loads(open('user_data (5)', "rb").read())
    name=request.form.get('name')
    place = request.form.get('place')
    branch = request.form.get('branch')
    names=[]
    places=[]
    branches=[]
    images=[]
    year=[]
    if(name!=''):
        for (i,namee) in enumerate(user_data['name']):
            if namee==name:
                names.append(namee)
                places.append(user_data['place'][i])
                branches.append(user_data['branch'][i])
                year.append(user_data['year'][i])
                img=user_data['image'][i]
                rawBytes = io.BytesIO()
                img.save(rawBytes, "JPEG")
                rawBytes.seek(0)
                img_base64 = base64.b64encode(rawBytes.read())
                images.append(str(img_base64))
        result={'name':names,'place':places,'branch':branches,'image':images,'year':year}
        return jsonify(result)
    elif(place!=''):
        for (i,placee) in enumerate(user_data['place']):
            if placee==place:
                places.append(placee)
                names.append(user_data['name'][i])
                branches.append(user_data['branch'][i])
                year.append(user_data['year'][i])
                img = user_data['image'][i]
                rawBytes = io.BytesIO()
                img.save(rawBytes, "JPEG")
                rawBytes.seek(0)
                img_base64 = base64.b64encode(rawBytes.read())
                images.append(str(img_base64))
        result={'name':names,'place':places,'branch':branches,'image':images,'year':year}
        return jsonify(result)
    elif (branch != ''):
        for (i, branchee) in enumerate(user_data['branch']):
            if branchee == branch:
                branches.append(branchee)
                names.append(user_data['name'][i])
                places.append(user_data['place'][i])
                year.append(user_data['year'][i])
                img = user_data['image'][i]
                rawBytes = io.BytesIO()
                img.save(rawBytes, "JPEG")
                rawBytes.seek(0)
                img_base64 = base64.b64encode(rawBytes.read())
                images.append(str(img_base64))
        result = {'name': names, 'place': places, 'branch': branches,'image':images,'year':year}
        return jsonify(result)


if __name__=='__main__':
    app.run(debug=True)

