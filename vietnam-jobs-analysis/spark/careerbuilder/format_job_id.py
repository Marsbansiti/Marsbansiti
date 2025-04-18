import pyspark.sql.functions as F
import pyspark.sql.types as T


@F.udf(returnType=T.StringType())
def format_job_id(job_id: str):
    try:
        return job_id[9:]
    except ValueError:
        return "not-found"
