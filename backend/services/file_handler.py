# services/file_handler.py
import os

# set the path for the temporary upload directory 
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'temp')
# ensure directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_audio_file(audio_file):
    """
    Save the uploaded audio file to a temporary directory.
    :param audio_file: File object uploaded by the user
    :return: Path to the saved audio file
    """
    # Define the path to save the audio file
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    
    # Save the file to the path
    audio_file.save(audio_path)
    
    # Return the file path
    return audio_path