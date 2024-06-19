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
predicate_pushdown = "region in ('ca','gb','us')"
AWSGlueDataCatalog_node1718411714188 = glueContext.create_dynamic_frame.from_catalog(database="yt_data_engg_raw", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1718411714188", push_down_predicate = predicate_pushdown)

# Script generated for node Change Schema
ChangeSchema_node1718411731138 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1718411714188, mappings=[("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "long", "category_id", "bigint"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "long", "views", "bigint"), ("likes", "long", "likes", "bigint"), ("dislikes", "long", "dislikes", "bigint"), ("comment_count", "long", "comment_count", "bigint"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "boolean", "comments_disabled", "boolean"), ("ratings_disabled", "boolean", "ratings_disabled", "boolean"), ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"), ("description", "string", "description", "string"), ("region", "string", "region", "string")], transformation_ctx="ChangeSchema_node1718411731138")

# Script generated for node Amazon S3
AmazonS3_node1718411754788 = glueContext.getSink(path="s3://yt-data-engg-clean-useast1-dev/youtube/raw_statistics/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1718411754788")
AmazonS3_node1718411754788.setCatalogInfo(catalogDatabase="db-yt-data-clean",catalogTableName="yt-data-engg-etl")
AmazonS3_node1718411754788.setFormat("glueparquet", compression="snappy")
AmazonS3_node1718411754788.writeFrame(ChangeSchema_node1718411731138)
job.commit()
