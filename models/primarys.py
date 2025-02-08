from django.db import models
import cuid2
from snowflake import SnowflakeGenerator
import os
import random

# ? LLL
from logger.logger import logger

class CUIDPrimaryKey(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("primary_key", True)
        kwargs.setdefault("max_length", 25)
        kwargs.setdefault("default", cuid2.Cuid().generate)
        super().__init__(*args, **kwargs)


    def db_type(self, connection):
        # Use VARCHAR(25) type in the database
        return f"varchar({self.max_length})"

    def get_prep_value(self, value):
        if not value:
            return cuid2.Cuid().generate()
        return str(value)

    def to_python(self, value):
        if value is None:
            return None
        return str(value)

class SnowflakePrimaryKey(models.BigAutoField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("primary_key", True)
        kwargs.setdefault("editable", False)  # AutoField should not be editable
        kwargs.setdefault("default", self.generate_snowflake)  # Set the default
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_snowflake():
        seed = os.urandom(16)
        random.seed(seed)
        gen = SnowflakeGenerator(random.randint(1, 100))
        snowflake = next(gen)
        logger.info(f"Generated snowflake: {snowflake}")
        return snowflake

    def get_internal_type(self):
        return "BigIntegerField"

    def get_prep_value(self, value):
        if value is None:
            return self.generate_snowflake()
        return value

    def to_python(self, value):
        if value is None:
            return None
        return int(value)


