from django.db import models
from django.contrib.auth.models import User

class NexusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    quota = models.IntegerField()

class ActualTotalLoad(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    ActionTaskID = models.BigIntegerField()
    Status = models.CharField(max_length=10, blank=True, null=True)
    Year = models.IntegerField()
    Month = models.IntegerField()
    Day = models.IntegerField()
    DateTime = models.DateTimeField()
    AreaName = models.CharField(max_length=200, blank=True, null=True)
    UpdateTime = models.DateTimeField()
    TotalLoadValue = models.DecimalField(max_digits=24, decimal_places=2)
    AreaTypeCodeId = models.ForeignKey('AreaTypeCode', models.DO_NOTHING, db_column='AreaTypeCodeId', blank=True, null=True)
    MapCodeId = models.ForeignKey('MapCode', models.DO_NOTHING, db_column='MapCodeId', blank=True, null=True)
    AreaCodeId = models.ForeignKey('AllocatedEICDetail', models.DO_NOTHING, db_column='AreaCodeId')
    ResolutionCodeId = models.ForeignKey('ResolutionCode', models.DO_NOTHING, db_column='ResolutionCodeId', blank=True, null=True)
    RowHash = models.CharField(max_length=255, blank=True, null=True)

class AggregatedGenerationPerType(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    ActionTaskID = models.BigIntegerField()
    Status = models.CharField(max_length=10, blank=True, null=True)
    Year = models.IntegerField()
    Month = models.IntegerField()
    Day = models.IntegerField()
    DateTime = models.DateTimeField()
    AreaName = models.CharField(max_length=200, blank=True, null=True)
    UpdateTime = models.DateTimeField()
    ActualGenerationOutput = models.DecimalField(max_digits=24, decimal_places=2)
    ActualConsuption = models.DecimalField(max_digits=24, decimal_places=2)
    AreaTypeCodeId = models.ForeignKey('AreaTypeCode', models.DO_NOTHING, db_column='AreaTypeCodeId', blank=True, null=True)
    ProductionTypeId = models.ForeignKey('ProductionType', models.DO_NOTHING, db_column='ProductionTypeId', blank=True, null=True)
    ResolutionCodeId = models.ForeignKey('ResolutionCode', models.DO_NOTHING, db_column='ResolutionCodeId', blank=True, null=True)
    MapCodeId = models.ForeignKey('MapCode', models.DO_NOTHING, db_column='MapCodeId', blank=True, null=True)
    AreaCodeId = models.ForeignKey('AllocatedEICDetail', models.DO_NOTHING, db_column='AreaCodeId')
    RowHash = models.CharField(max_length=255, blank=True, null=True)

class AllocatedEICDetail(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    MRID = models.CharField(max_length=250, blank=True, null=True)
    DocStatusValue = models.CharField(max_length=250, blank=True, null=True)
    AttributeInstanceComponent = models.CharField(max_length=250, blank=True, null=True)
    LongNames = models.CharField(max_length=250, blank=True, null=True)
    DisplayNames = models.CharField(max_length=250, blank=True, null=True)
    LastRequestDateAndOrTime = models.DateTimeField(blank=True, null=True)
    DeactivateRequestDateAndOrTime = models.DateTimeField(blank=True, null=True)
    MarketParticipantStreetAddressCountry = models.CharField(max_length=250, blank=True, null=True)
    MarketParticipantACERCode = models.CharField(max_length=250, blank=True, null=True)
    MarketParticipantVATcode = models.CharField(max_length=250, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    EICParentMarketDocumentMRID = models.CharField(max_length=250, blank=True, null=True)
    ELCResponsibleMarketParticipantMRID = models.CharField(max_length=250, blank=True, null=True)
    IsDeleted = models.BooleanField()
    AllocatedEICID = models.IntegerField()

class AreaTypeCode(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    AreaTypeCodeText = models.CharField(unique=True, max_length=255, blank=True, null=True)
    AreaTypeCodeNote = models.CharField(max_length=255, blank=True, null=True)

class DayAheadTotalLoadForecast(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    ActionTaskID = models.BigIntegerField()
    Status = models.CharField(max_length=10, blank=True, null=True)
    Year = models.IntegerField()
    Month = models.IntegerField()
    Day = models.IntegerField()
    DateTime = models.DateTimeField()
    AreaName = models.CharField(max_length=200, blank=True, null=True)
    UpdateTime = models.DateTimeField()
    TotalLoadValue = models.DecimalField(max_digits=24, decimal_places=2)
    AreaTypeCodeId = models.ForeignKey(AreaTypeCode, models.DO_NOTHING, db_column='AreaTypeCodeId', blank=True, null=True)
    MapCodeId = models.ForeignKey('MapCode', models.DO_NOTHING, db_column='MapCodeId', blank=True, null=True)
    AreaCodeId = models.ForeignKey(AllocatedEICDetail, models.DO_NOTHING, db_column='AreaCodeId')
    ResolutionCodeId = models.ForeignKey('ResolutionCode', models.DO_NOTHING, db_column='ResolutionCodeId', blank=True, null=True)
    RowHash = models.CharField(max_length=255, blank=True, null=True)

class MapCode(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    MapCodeText = models.CharField(unique=True, max_length=255, blank=True, null=True)
    MapCodeNote = models.CharField(max_length=255, blank=True, null=True)

class ProductionType(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    ProductionTypeText = models.CharField(unique=True, max_length=255, blank=True, null=True)
    ProductionTypeNote = models.CharField(max_length=255, blank=True, null=True)

class ResolutionCode(models.Model):
    Id = models.AutoField(primary_key=True)
    EntityCreatedAt = models.DateTimeField()
    EntityModifiedAt = models.DateTimeField()
    ResolutionCodeText = models.CharField(unique=True, max_length=255, blank=True, null=True)
    ResolutionCodeNote = models.CharField(max_length=255, blank=True, null=True)