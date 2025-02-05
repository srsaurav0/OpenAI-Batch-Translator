# Batch Translation with OpenAI API

This project uses the **OpenAI Batch API** to translate a list of sentences from one language to another. The workflow involves preparing a `.jsonl` file containing translation requests, uploading the file to OpenAI's servers, and using the Batch API to handle translation asynchronously.

---

## Workflow Overview

1. **Prepare Input Data**: The script takes a list of texts and creates a `.jsonl` file. Each text is translated according to the specified source and target languages. The `.jsonl` file contains all translation requests for batch processing.
2. **Upload Input File**: The prepared `.jsonl` file is uploaded to OpenAI's server.
3. **Create Batch Job**: A batch job is created using the uploaded file. This job processes all the translation requests asynchronously.
4. **Check Batch Status**: The script periodically checks the status of the batch job to track when it's completed.
5. **Retrieve Translated Results**: Once the batch job is completed, the translated sentences are retrieved and printed.

---

## Setup and Instructions

### **Clone the Repository**
```
git clone https://github.com/srsaurav0/OpenAI-Batch-Translator.git
cd OpenAI-Batch-Translator
```

### **Create Virtual Environment**
```
python3 -m venv .venv
source .venv/bin/activate
```

### **Install Dependencies**   
Install the required packages:
```bash
pip install -r requirements.txt
```

### **Update API Key**
Create a **config.yml** file at root:
```
touch config.yml
```
Copy content from `config.yml.example` and update the `OpenAI_API_KEY`.

### **Run Project**
```
python3 main.py
```
