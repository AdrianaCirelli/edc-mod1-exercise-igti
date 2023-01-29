import pyspark
from pyspark.sql import SparkSession

# %% [markdown]
# #### Inicia uma `Session` do Spark com `Delta Lake`

# %%
## create SparkSession
spark = (SparkSession.builder
                     .appName("DeltaFile")
                     .config("spark.jars.packages", "io.delta:delta-core_2.12:2.0.0")
                     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
                     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
                     .getOrCreate())


spark.stop()