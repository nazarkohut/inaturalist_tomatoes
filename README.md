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
