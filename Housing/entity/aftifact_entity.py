from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["training_file_path","test_file_path","is_ingested","message"])
