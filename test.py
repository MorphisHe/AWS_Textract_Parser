'''
Providing example of usage

Requirments: you need to have aws config file set up correctly.
'''

import sys
from DocumentProcessor import SingleDocumentProcessor, BatchDocumentProcessor
from TextractParser import Document


if __name__ == "__main__":
    # s3_bucket_name, s3_doc_name, process_type, mode
    args = sys.argv[2:]

    s3_bucket_name = args[0]
    s3_doc_name = args[1]

    # DETECTION, ANALYSIS
    process_type = args[2]

    # single, batch
    mode = args[3]

    results = []
    if mode == "single":
        sdp = SingleDocumentProcessor(s3_bucket_name, s3_doc_name)
        results = sdp.get_results()
    else:
        bdp = BatchDocumentProcessor()
        bdp.start_textract_job(s3_bucket_name, [s3_doc_name], [process_type])
        results = bdp.get_results()

    # parser the json responses
    doc = Document(results)

    print(doc)






