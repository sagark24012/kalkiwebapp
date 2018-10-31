# Create your views here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Genpntdatatable(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=100)  # Field name made lowercase.
    pointid = models.FloatField(db_column='PointID', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.
    flags = models.BigIntegerField(db_column='Flags')  # Field name made lowercase.
    timetag = models.BigIntegerField(db_column='TimeTag')  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GenPntDataTable'
        unique_together = (('pointid', 'timetag'),)