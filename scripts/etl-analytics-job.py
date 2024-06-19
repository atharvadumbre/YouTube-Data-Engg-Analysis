import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1718470627157 = glueContext.create_dynamic_frame.from_catalog(database="db-yt-data-clean", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1718470627157")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1718470625750 = glueContext.create_dynamic_frame.from_catalog(database="db-yt-data-clean", table_name="clean_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1718470625750")

# Script generated for node Join
Join_node1718470689671 = Join.apply(frame1=AWSGlueDataCatalog_node1718470625750, frame2=AWSGlueDataCatalog_node1718470627157, keys1=["id"], keys2=["category_id"], transformation_ctx="Join_node1718470689671")

# Script generated for node Amazon S3
AmazonS3_node1718471311832 = glueContext.getSink(path="s3://yt-data-engg-analytics", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1718471311832")
AmazonS3_node1718471311832.setCatalogInfo(catalogDatabase="db-yt-data-analytics",catalogTableName="yt-data-analytics")
AmazonS3_node1718471311832.setFormat("glueparquet", compression="snappy")
AmazonS3_node1718471311832.writeFrame(Join_node1718470689671)
job.commit()
