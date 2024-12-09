### AWS:

Initial idea was to parse data with Lambda functions invoked by State Machine(Step functions) leveraging block for DynamoDB batch writes. 
This flow can be found in aws_code.README.mc file, however this flow will be adjusted, 
because current functionality of step function DynamoDB write does not support dynamic arrays of objects.
Current idea to adjustments: replace DynamoDB writing block with another lambda function which pushes batches to DynamoDB.
Another step to perform is use of AWS GLUE to retrieve files into S3 in format of chunked parquet files, 
which could be processed and analyzed.


Currently, we perform only parallel execution by licence codes, making it 4 nodes to parse data with cons of uneven load.


### Local code:

At the moment parsing is performed in one machine and personal computer. 
Some of parsed files are empty and only include column names which helps with future processing.

In order to analyze data and perform operations quickly we use DBeaver and DuckDB.

#### How to use?

##### Get data from Inaturalist
Current pipeline is semi-automatic, 
meaning we go to Inaturalist for taxon_id and other fields, 
adjust config for one of the diseases, species, etc., and 
run data retrieval for this query only.

**Steps to run data retrival script:**
1. Adjust global config in local code as well as data_preprocessors config.
2. Run `main.py` to parse and slightly preprocess data.
3. Use DBeaver and DuckDB to get merged parquet.

**Possible improvements:** integrate data_preprocessors into `parse.py` script.

**Download to local and Upload to Roboflow:**
1. Open roboflow directory and adjust upload_config.py to suit your needs.
2. Run `download_images.py` to download images to local machine.
3. Run `upload_images.py` to upload images to roboflow repository.

