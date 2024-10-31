Idea is to parse data with Lambda functions invoked by State Machine(Step functions). 
Current flow can be found in aws_code.README.mc file, however this flow is not complete and will be adjusted.
Main adjustments will include writing data to Dynamo in batches and retrieval of parsed data will be performed by AWS GLUE; 
in other words we will retrieve files to S3 in format of chunked parquet files.


Currently, we only parallel execution by licence codes, making it 4 nodes to parse data with cons of uneven load.


