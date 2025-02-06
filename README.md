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

### **Prepare Input**
Insert input in dictionary (key-value) format inside ***batch_helpers/batch_inputs.py*** file. It returns a list of dictionaries as input to the main translator.

### **Run Project**
```
python3 main.py
```

### **Access Output**
Open contents in ***results/list*** to access the results. The results are saved according to `batch_id`s. Each request is saved with the corresponding `tpl/ini-key.txt` format for future use cases.

---

## Batch Process Test Summary

- For this test, 3 batches of 5 requests are created.
- In each request, a **tpl** in converted to English to other language.

- This table provides a summary of batch processing details, including IDs, durations, and token usage.

| Batch ID | Output File ID | Task            | No. of Requests | Duration (HH:MM:SS)        | Prompt Tokens | Completion Tokens | Total Tokens |
|----------|----------------|-----------------|-----------------|-----------------|---------------|-------------------|--------------|
| batch_67a35b88d6548190bdcb2ff989522703  | output_1       | en to es        | 5        | 10:56:36         | 4513           | 4301               | 8414          |
| batch_67a337076e3c8190ae1af48092425fbc  | output_2       | en to de        | 5        | 14:24:34 | 4513           | 4378               | 8591          |
| batch_67a35b7efe80819084d38722746c71da  | output_3       | en to fr         | 5        | 10:51:19  | 4513           | 4396               | 7909          |

---

## **Samples**

### Input Jsonl File Sample

```jsonl
{"custom_id": "rentbyowner.com-key_1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o-mini", "messages": [{"role": "system", "content": "Translate the sentence from English to French. \nKeep all HTML tags, attributes, and links intact. \nKeep all templates intact. \nTranslate only the visible text between the tags. \nPreserve the exact text of 'Rent By Owner\u2122' and 'Rent by Owner' without translation or modification.\nPreserve original spacing and line breaks without adding or removing any. \nEnsure that the original formatting, including indentation and line breaks, is preserved in the output."}, {"role": "user", "content": "{{template \"common/redirect/redirect.tpl\" .}}\n\n{{define \"site_common_preload\"}}\n    <link rel=\"preload\" href=\"{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>\n{{end}}\n\n{{define \"site_css\"}}\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css\"/>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css\"/>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css\"/>\n{{end}}\n\n{{define \"site_preload\"}}\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css\" as=\"style\"/>\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css\" as=\"style\"/>\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css\" as=\"style\"/>\n{{end}}\n\n{{define \"site_header_logo_redirect\"}}\n    <a href=\"/\" class=\"align-item-center\">\n        <img src=\"{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg\" alt=\"{{i18n .Lang \"brand\"}}\" width=\"182\" height=\"26\">\n    </a>\n{{end}}\n\n{{define \"site_redirect_container_logo\"}}\n    <div class=\"box logo-area\">\n        <img src=\"{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg\" alt=\"{{i18n .Lang \"brand\"}}\" width=\"182\" height=\"26\" />\n    </div>\n{{end}}"}], "max_tokens": 5000}}

{"custom_id": "rentbyowner.com-key_2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o-mini", "messages": [{"role": "system", "content": "Translate the sentence from English to Spanish. \nKeep all HTML tags, attributes, and links intact. \nKeep all templates intact. \nTranslate only the visible text between the tags. \nPreserve the exact text of 'Rent By Owner\u2122' and 'Rent by Owner' without translation or modification.\nPreserve original spacing and line breaks without adding or removing any. \nEnsure that the original formatting, including indentation and line breaks, is preserved in the output."}, {"role": "user", "content": "{{if eq .pageLayout \"SubLocation:Hotel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/hotels.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:VacationRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Cottage\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/cottages.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Cabin\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/cabins.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Villa\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/villas.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Resort\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/resorts.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:FamilyRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/family_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:PetFriendly\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/pet_friendly.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Pool\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/rentals_with_pools.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Oceanfront\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/oceanfront.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Beach\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/beach_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:LuxuryRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/luxury_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:DiscountRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/discount_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:BusinessTravel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/business_travel.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:ShortTermStay\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/short_term_stays.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:SustainableTravel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/sustainable_travel.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:SkiChalet\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/ski_chalets.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Timeshare\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/timeshares.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:GroupTravel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/group_travel.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:WinterRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/winter_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:SummerRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/summer_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:MonthlyStay\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/monthly_stays.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:HolidayHomes\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/holiday_homes.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:UniqueVacationRentals\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/unique_vacation_rentals.tpl\" .}}\n{{else}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl\" .}}\n{{end}}"}], "max_tokens": 5000}}
```

### Output Jsonl File Sample

```jsonl
{"custom_id": "rentbyowner.com-key_1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o-mini", "messages": [{"role": "system", "content": "Translate the sentence from English to French. \nKeep all HTML tags, attributes, and links intact. \nKeep all templates intact. \nTranslate only the visible text between the tags. \nPreserve the exact text of 'Rent By Owner\u2122' and 'Rent by Owner' without translation or modification.\nPreserve original spacing and line breaks without adding or removing any. \nEnsure that the original formatting, including indentation and line breaks, is preserved in the output."}, {"role": "user", "content": "{{template \"common/redirect/redirect.tpl\" .}}\n\n{{define \"site_common_preload\"}}\n    <link rel=\"preload\" href=\"{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>\n{{end}}\n\n{{define \"site_css\"}}\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css\"/>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css\"/>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css\"/>\n{{end}}\n\n{{define \"site_preload\"}}\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css\" as=\"style\"/>\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css\" as=\"style\"/>\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css\" as=\"style\"/>\n{{end}}\n\n{{define \"site_header_logo_redirect\"}}\n    <a href=\"/\" class=\"align-item-center\">\n        <img src=\"{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg\" alt=\"{{i18n .Lang \"brand\"}}\" width=\"182\" height=\"26\">\n    </a>\n{{end}}\n\n{{define \"site_redirect_container_logo\"}}\n    <div class=\"box logo-area\">\n        <img src=\"{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg\" alt=\"{{i18n .Lang \"brand\"}}\" width=\"182\" height=\"26\" />\n    </div>\n{{end}}"}], "max_tokens": 5000}}

{"custom_id": "rentbyowner.com-key_2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o-mini", "messages": [{"role": "system", "content": "Translate the sentence from English to Spanish. \nKeep all HTML tags, attributes, and links intact. \nKeep all templates intact. \nTranslate only the visible text between the tags. \nPreserve the exact text of 'Rent By Owner\u2122' and 'Rent by Owner' without translation or modification.\nPreserve original spacing and line breaks without adding or removing any. \nEnsure that the original formatting, including indentation and line breaks, is preserved in the output."}, {"role": "user", "content": "{{if eq .pageLayout \"SubLocation:Hotel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/hotels.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:VacationRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Cottage\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/cottages.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Cabin\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/cabins.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Villa\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/villas.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Resort\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/resorts.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:FamilyRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/family_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:PetFriendly\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/pet_friendly.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Pool\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/rentals_with_pools.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Oceanfront\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/oceanfront.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Beach\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/beach_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:LuxuryRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/luxury_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:DiscountRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/discount_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:BusinessTravel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/business_travel.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:ShortTermStay\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/short_term_stays.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:SustainableTravel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/sustainable_travel.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:SkiChalet\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/ski_chalets.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:Timeshare\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/timeshares.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:GroupTravel\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/group_travel.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:WinterRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/winter_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:SummerRental\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/summer_rentals.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:MonthlyStay\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/monthly_stays.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:HolidayHomes\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/holiday_homes.tpl\" .}}\n{{else if eq .pageLayout \"SubLocation:UniqueVacationRentals\"}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/unique_vacation_rentals.tpl\" .}}\n{{else}}\n    {{template \"sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl\" .}}\n{{end}}"}], "max_tokens": 5000}}
```

## API Limits
- Single batch max requests: 50,000
- Max batch input size: 200MB
- Batch queue limits: 200,000 TPD


## Issues

1.  API Key Permissions (Fixed)
    ```jsonl
    {"id": "batch_req_67a04e642a688190bbe5b708764f61e1", "custom_id": "request-0", "response": {"status_code": 403, "request_id": "51d7fe433d6a4b8cd9396f7a1a1d6b03", "body": {"error": {"message": "Project `proj_8kkVu5Y1unJ3VgMXOw0TGb6v` does not have access to model `gpt-4o-mini-2024-07-18-batch`", "type": "invalid_request_error", "param": null, "code": "model_not_found"}}}, "error": null}
    ```
2.  Input format (Fixed)
    Previous input format:
    ```python
    tpls = [
        """tpl1""",
        """tpl2"""
    ]
    ```
    Current input format:
    ```python
    tpls = {
        "key-1" : """tpl1""",
        "key-2" : """tpl2"""
    }
    ```
3.  Preserving new lines and indentation in output (Fixed)

    The `content` field in output ***.jsonl*** file is saved to ***.txt*** file with **utf-8** encoding.

    Previous output content:
    ```html
    "```html\n{{template \"common/redirect/redirect.tpl\" .}}\n\n{{define \"site_common_preload\"}}\n    <link rel=\"preload\" href=\"{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>\n{{end}}\n\n{{define \"site_css\"}}\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css\"/>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css\"/>\n    <link rel=\"stylesheet\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css\"/>\n{{end}}\n\n{{define \"site_preload\"}}\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css\" as=\"style\"/>\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css\" as=\"style\"/>\n    <link rel=\"preload\" type=\"text/css\" href=\"{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css\" as=\"style\"/>\n{{end}}\n\n{{define \"site_header_logo_redirect\"}}\n    <a href=\"/\" class=\"align-item-center\">\n        <img src=\"{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg\" alt=\"{{i18n .Lang \"brand\"}}\" width=\"182\" height=\"26\">\n    </a>\n{{end}}\n\n{{define \"site_redirect_container_logo\"}}\n    <div class=\"box logo-area\">\n        <img src=\"{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg\" alt=\"{{i18n .Lang \"brand\"}}\" width=\"182\" height=\"26\" />\n    </div>\n{{end}}\n```"
    ```
    Current output content:
    ```html
    ```html
    {{template "common/redirect/redirect.tpl" .}}

    {{define "site_common_preload"}}
        <link rel="preload" href="{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2" as="font" type="font/woff2" crossorigin>
    {{end}}

    {{define "site_css"}}
        <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
        <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
        <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css"/>
    {{end}}

    {{define "site_preload"}}
        <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
        <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
        <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css" as="style"/>
    {{end}}

    {{define "site_header_logo_redirect"}}
        <a href="/" class="align-item-center">
            <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26">
        </a>
    {{end}}

    {{define "site_redirect_container_logo"}}
        <div class="box logo-area">
            <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26" />
        </div>
    {{end}}```
    ```

## Drawbacks

1. Variable batch processing time (Within 24 hours)
2. Batch cancel time up to 10 minutes


<!-- batch_67a35b88d6548190bdcb2ff989522703 -> Spanish
batch_67a337076e3c8190ae1af48092425fbc -> German
batch_67a35b7efe80819084d38722746c71da -> French -->