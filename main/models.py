from django.db import models


# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    action_flag = models.PositiveSmallIntegerField()
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


class TAdmin(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    salt = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_admin'


class TAlbum(models.Model):
    album_title = models.CharField(max_length=50, blank=True, null=True)
    thumbnail_url = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    bordcaster = models.CharField(max_length=50, blank=True, null=True)
    chapter_num = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    rating = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_album'


class TArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    thumbnail_url = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    teacher = models.ForeignKey('TTeacher', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pic_urls = models.CharField(max_length=100, blank=True, null=True)
    article_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_article'


class TAudioChapter(models.Model):
    chapter_name = models.CharField(max_length=50, blank=True, null=True)
    audio_size = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    audio_duration = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    audio_url = models.CharField(max_length=100, blank=True, null=True)
    audio = models.ForeignKey(TAlbum, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_audio_chapter'


class TSlidpic(models.Model):
    url = models.ImageField(upload_to='slidpic')
    title = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 't_slidpic'


class TTask(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    task_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_task'


class TTaskCounter(models.Model):
    count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    crate_date = models.DateTimeField(blank=True, null=True)
    task = models.ForeignKey(TTask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_task_counter'


class TTeacher(models.Model):
    thumbnail = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_teacher'


class TUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    thumbnail_url = models.CharField(max_length=100, blank=True, null=True)
    user_info = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    salt = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
