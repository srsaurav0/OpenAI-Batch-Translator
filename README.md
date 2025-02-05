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

### **Access Output**
Open contents in ***results/list*** to access the results. The results are saved according to `batch_id`s.

---

## Batch Process Summary

This table provides a summary of batch processing details, including IDs, durations, and token usage.

| Batch ID | Output File ID | Task            | No. of Requests | Duration        | Prompt Tokens | Completion Tokens | Total Tokens |
|----------|----------------|-----------------|-----------------|-----------------|---------------|-------------------|--------------|
| batch_67a35b88d6548190bdcb2ff989522703  | output_1       | en to es        | 5        | 2 hours         | 150           | 450               | 600          |
| batch_67a337076e3c8190ae1af48092425fbc  | output_2       | en to de        | 5        | 3 hours 30 mins | 200           | 550               | 750          |
| batch_67a35b7efe80819084d38722746c71da  | output_3       | en to fr         | 5        | 1 hour 45 mins  | 100           | 300               | 400          |


## API Limits
- Single batch max requests: 50,000
- Max batch input size: 200MB
- Batch queue limits: 200,000 TPD


## Issues

1. API Key Permissions (Fixed)
2. Input format (Fixed)
3. Output format (Fixed)
4. Handling new lines and indentation (Fixed)

## Drawbacks

1. Variable batch processing time (Within 24 hours)
2. Batch cancel time up to 10 minutes


<!-- batch_67a336c572e8819083eb902a3a5f99fe -> Spanish
batch_67a337076e3c8190ae1af48092425fbc -> German
batch_67a337b4d33881908a099fe5e81e579c -> French -->