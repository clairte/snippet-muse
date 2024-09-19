from flask import Flask, request, jsonify 
import os

# initiate flask application 
app = Flask(__name__)

# set the path for the temporary upload directory 
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'temp')

# ensure directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# test route 
@app.route('/')
def home(): 
    return "Server is running!"

# upload file route 
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files: 
        return jsonify({'error': 'No file uploaded'}), 400

    audio_file = request.files['audio']

    # save uploaded file
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(audio_path)

    # TODO: add midi conversion and magenta logic 

    return jsonify({'message': 'File received', 'audio_path': audio_path})

if __name__ == '__main__':
    app.run(debug=True)


