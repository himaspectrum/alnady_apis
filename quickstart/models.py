# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cosmeticsshortname(models.Model):
    tradecode = models.IntegerField(db_column='TradeCode', blank=True, null=True)  # Field name made lowercase.
    shorttradename = models.CharField(db_column='ShortTradeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    trade_name = models.CharField(db_column='Trade_name', max_length=1500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CosmeticsShortName'


class Tempcompany(models.Model):
    company_code = models.AutoField(db_column='Company_code',primary_key=True)  # Field name made lowercase.
    arabicname = models.CharField(db_column='ArabicName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licensetypecode = models.DecimalField(db_column='LicenseTypeCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companytypecode = models.DecimalField(db_column='CompanyTypeCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    companytype = models.CharField(db_column='CompanyType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companystatus = models.CharField(db_column='CompanyStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempCompany'


class Tempdrug(models.Model):
    tradecode = models.DecimalField(db_column='TradeCode', primary_key=True, max_digits=12, decimal_places=0)  # Field name made lowercase.
    regno = models.CharField(db_column='RegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    license_type_code = models.DecimalField(db_column='License_type_code', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    license_type = models.CharField(db_column='License_type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licensestatuscode = models.DecimalField(db_column='LicenseStatusCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    licensestatus = models.CharField(db_column='LicenseStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dosage_formcode = models.DecimalField(db_column='Dosage_formCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dosage_form = models.CharField(db_column='Dosage_form', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shelflife = models.DecimalField(db_column='ShelfLife', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    markettypecode = models.DecimalField(db_column='MarketTypeCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    markettype = models.CharField(db_column='MarketType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licflagcode = models.DecimalField(db_column='LicFlagCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    licflag = models.CharField(db_column='LicFlag', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvenamea = models.CharField(db_column='ApproveNameA', max_length=300, blank=True, null=True)  # Field name made lowercase.
    manufcode = models.DecimalField(db_column='ManufCode', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manuf = models.CharField(db_column='Manuf', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_code = models.DecimalField(db_column='Company_code', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    legacystatus = models.DecimalField(db_column='LegacyStatus', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    drug_registration_date = models.DateTimeField(db_column='Drug_registration_date', blank=True, null=True)  # Field name made lowercase.
    drug_registration_expiration_date = models.DateTimeField(db_column='Drug_registration_expiration_date', blank=True, null=True)  # Field name made lowercase.
    company_profile_id = models.DecimalField(db_column='COMPANY_PROFILE_ID', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufcountryid = models.DecimalField(db_column='ManufCountryID', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufcountry = models.CharField(db_column='ManufCountry', max_length=350, blank=True, null=True)  # Field name made lowercase.
    license_holder_company_id = models.DecimalField(db_column='LICENSE_HOLDER_COMPANY_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    license_holder_company = models.CharField(db_column='LICENSE_HOLDER_COMPANY', max_length=350, blank=True, null=True)  # Field name made lowercase.
    license_holder_country_id = models.DecimalField(db_column='LICENSE_HOLDER_COUNTRY_ID', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    license_holder_country = models.CharField(db_column='LICENSE_HOLDER_COUNTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f_added = models.BooleanField(db_column='F_ADDED', blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempDrug'


class Tempdrugsmanufacture(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parent = models.ForeignKey(Tempdrug, models.DO_NOTHING, db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    manufcode = models.IntegerField(db_column='ManufCode', blank=True, null=True)  # Field name made lowercase.
    manuf = models.CharField(db_column='Manuf', max_length=300, blank=True, null=True)  # Field name made lowercase.
    manufcountryid = models.IntegerField(db_column='ManufCountryID', blank=True, null=True)  # Field name made lowercase.
    manufcountry = models.CharField(db_column='ManufCountry', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempDrugsManufacture'


class Vacation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vacation_date = models.DateTimeField(db_column='VACATION_DATE')  # Field name made lowercase.
    vacation_desc = models.TextField(db_column='VACATION_DESC', blank=True, null=True)  # Field name made lowercase.
    created_by = models.DecimalField(db_column='CREATED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.DecimalField(db_column='MODIFIED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='MODIFIED_DATE', blank=True, null=True)  # Field name made lowercase.
    f_delete = models.BooleanField(db_column='F_DELETE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VACATION'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:

        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Product(models.Model):
    id = models.DecimalField(db_column='ID', max_digits=12, decimal_places=0,primary_key=True)  # Field name made lowercase.
    old_product_id = models.DecimalField(db_column='OLD_PRODUCT_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    old_reg_no = models.DecimalField(db_column='OLD_REG_NO', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    notification_no = models.CharField(db_column='NOTIFICATION_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notification_date = models.DateTimeField(db_column='NOTIFICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    re_notification_date = models.DateTimeField(db_column='RE_NOTIFICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    product_type_id = models.DecimalField(db_column='PRODUCT_TYPE_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    arabic_name = models.CharField(db_column='ARABIC_NAME', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    english_name = models.CharField(db_column='ENGLISH_NAME', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    registration_type_id = models.DecimalField(db_column='REGISTRATION_TYPE_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    company_profile_id = models.DecimalField(db_column='COMPANY_PROFILE_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturing_company_id = models.DecimalField(db_column='MANUFACTURING_COMPANY_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturing_country_id = models.DecimalField(db_column='MANUFACTURING_COUNTRY_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    applicant_id = models.DecimalField(db_column='APPLICANT_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    license_holder_id = models.DecimalField(db_column='LICENSE_HOLDER_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    license_holder_other = models.CharField(db_column='LICENSE_HOLDER_OTHER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    license_holder_country_id = models.DecimalField(db_column='LICENSE_HOLDER_COUNTRY_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    trade_mark = models.CharField(db_column='TRADE_MARK', max_length=300, blank=True, null=True)  # Field name made lowercase.
    physical_state_id = models.DecimalField(db_column='PHYSICAL_STATE_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    physical_state_other = models.CharField(db_column='PHYSICAL_STATE_OTHER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    colour_id = models.DecimalField(db_column='COLOUR_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_purpose_id = models.DecimalField(db_column='USE_PURPOSE_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    purpose_of_use_other = models.CharField(db_column='PURPOSE_OF_USE_OTHER', max_length=300, blank=True, null=True)  # Field name made lowercase.
    storage_place_id = models.DecimalField(db_column='STORAGE_PLACE_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shelf_life = models.DecimalField(db_column='SHELF_LIFE', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateTimeField(db_column='EXPIRATION_DATE', blank=True, null=True)  # Field name made lowercase.
    appworks_id = models.CharField(db_column='APPWORKS_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    appworks_guid = models.CharField(db_column='APPWORKS_GUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f_expired = models.BooleanField(db_column='F_EXPIRED', blank=True, null=True)  # Field name made lowercase.
    f_confirmed = models.BooleanField(db_column='F_CONFIRMED', blank=True, null=True)  # Field name made lowercase.
    f_draft = models.BooleanField(db_column='F_DRAFT', blank=True, null=True)  # Field name made lowercase.
    f_kit = models.BooleanField(db_column='F_KIT', blank=True, null=True)  # Field name made lowercase.
    f_export_only = models.BooleanField(db_column='F_EXPORT_ONLY', blank=True, null=True)  # Field name made lowercase.
    f_flag = models.BooleanField(db_column='F_FLAG', blank=True, null=True)  # Field name made lowercase.
    f_flag_lab = models.BooleanField(db_column='F_FLAG_LAB', blank=True, null=True)  # Field name made lowercase.
    f_hold = models.BooleanField(db_column='F_HOLD', blank=True, null=True)  # Field name made lowercase.
    f_hold_lab = models.BooleanField(db_column='F_HOLD_LAB', blank=True, null=True)  # Field name made lowercase.
    f_block = models.BooleanField(db_column='F_BLOCK', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.DecimalField(db_column='CREATED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.DecimalField(db_column='MODIFIED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='MODIFIED_DATE', blank=True, null=True)  # Field name made lowercase.
    f_delete = models.BooleanField(db_column='F_DELETE', blank=True, null=True)  # Field name made lowercase.
    f_inprocess = models.BooleanField(db_column='F_INPROCESS', blank=True, null=True)  # Field name made lowercase.
    license_holder_syskey = models.DecimalField(db_column='LICENSE_HOLDER_syskey', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COSM].[PRODUCT'

class ProductDetails(models.Model):
    id = models.DecimalField(db_column='ID', max_digits=12, decimal_places=0,primary_key=True)  # Field name made lowercase.
    product_id = models.DecimalField(db_column='PRODUCT_ID', max_digits=12, decimal_places=0)  # Field name made lowercase.
    product_colour = models.CharField(db_column='PRODUCT_COLOUR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fragrance = models.CharField(db_column='FRAGRANCE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    flavor = models.CharField(db_column='FLAVOR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BARCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    appworks_id = models.CharField(db_column='APPWORKS_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    appworks_guid = models.CharField(db_column='APPWORKS_GUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_by = models.DecimalField(db_column='MODIFIED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='MODIFIED_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.DecimalField(db_column='CREATED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    f_delete = models.BooleanField(db_column='F_DELETE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COSM].[PRODUCT_DETAILS'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProductBatches(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.DecimalField(db_column='PRODUCT_ID', max_digits=12, decimal_places=0)  # Field name made lowercase.
    batch_no = models.CharField(db_column='BATCH_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    production_date = models.DateTimeField(db_column='PRODUCTION_DATE', blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateTimeField(db_column='EXPIRATION_DATE', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='QUANTITY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lkup_uom_id = models.DecimalField(db_column='LKUP_UOM_ID', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    created_by = models.DecimalField(db_column='CREATED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.DecimalField(db_column='MODIFIED_BY', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='MODIFIED_DATE', blank=True, null=True)  # Field name made lowercase.
    f_delete = models.BooleanField(db_column='F_DELETE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COSM].[PRODUCT_BATCHES'
