<template>
    <div>
        <input type="file" @change="handleFileUpload" accept=".mp3, .wav"/> 
        <button @click="submitFile" :disabled="!file"> Upload snippet </button>
        <div v-if="processing">{{ statusMessage }} </div>
    </div>
</template>

<script>
export default{
    data(){
        return{
            file: null, // Stores the uploaded file (initially null).
            processing: false, // Indicates if the file is being processed (initially false).
            statusMessage: '' // Displays a message (e.g., error, success) related to the upload process.
        };
    }, 
    methods: {
        //handles frontend file upload logic 
        handleFileUpload(event){
            const selectedFile = event.target.files[0]; 
            const validTypes = ['audio/mpeg', 'audio/wav', 'audio/mp3']; 

            //if selectedFile exists and type is valid, handle upload 
            if (selectedFile && validTypes.includes(selectedFile.type)){
                this.file = selectedFile; 
                this.statusMessage = `Selected file: ${selectedFile.name}`; 
            } else {
                this.statusMessage = 'Please upload a valid .mp3 or .wav file'; 
                this.file = null; 
            }
        },

        //submit file to backend 
        async submitFile(){
            if (!this.file) {
                this.statusMessage = 'No file selected. Please choose a .mp3 or .wav file.';
                return;
            } 

            this.processing = true; 
            this.statusMessage = "Uploading..."; 

            try{
                const formData = new FormData(); //create form-like structure that can hold file to send to server 
                formData.append('audio', this.file); 

                //make request to backend 
                const submitResp = await this.$axios.post('/upload_api_TBD', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                this.statusMessage = 'Processing success!';
                //this.$emit('fileProcessed', response.data.midiUrl);
            } catch(error) {
                this.statusMessage = 'Error uploading file.';
            } finally {
                this.processing = false;
            }

        }
    }
}; 
</script>

<style>
input[type="file"] {
  margin: 10px 0;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

div {
  margin-top: 10px;
}

</style>