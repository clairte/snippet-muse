from flask import Blueprint, request, jsonify 
from services.file_handler import save_audio_file

upload_blueprint = Blueprint('upload', __name__)

# upload file route 
@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files: 
        return jsonify({'error': 'No file uploaded'}), 400

    audio_file = request.files['audio']

    # save uploaded file
    audio_path = save_audio_file(audio_file)

    return jsonify({'message': 'File received', 'audio_path': audio_path})