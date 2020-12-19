# Textract Parser
    - DocumentProcessor: extract result from pdf or image using AWS Textract
        - SingleDocumentProcessor:
            - takes either image or pdf as input
            - extracts text in real time
        - BatchDocumentProcessor:
            - takes only pdf as input
            - async call, not real time
            - you can pass in list of s3_doc_name and process_type_list for each document to process all documents at same time
    
    - TextractParser: parsing AWS Textract response
        - Document: the top level class
        - parse_para: this parameter for Document class.
            - pass in as dict
            - "non_char": discard paragraph by percentage of non char characters
                - value: [0.0, 1.0]
            - "single_char": discard paragraph by percentage of single char words
                - value: [0.0, 1.0]
            - "min_word_count": discard paragraph if word_count < min_word_count
                - value: any int

### !! This is actually a module in my other project. I found this reusable, so I moved it to an individual repo. !! ###


## requirments
    - install all packages in requirment.txt
    - set up aws config for textract. (check on AWS source page on how to do this)

## Test
    - python3 test.py s3_bucket_name s3_doc_name [process_type (DETECTION | ANALYSIS)] [mode (single | batch)]
