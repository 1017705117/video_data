from django.db import models


# Create your models here.

# 数据测试表
class Data(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)


# 违规view
class IllegalData(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=30)
    upload_time = models.CharField(max_length=30)
    illegal_time = models.CharField(max_length=30)
    illegal = models.CharField(max_length=30)
    img = models.CharField(max_length=70)


# 视频Video表
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    upload_time = models.DateTimeField()
    video_name = models.CharField(max_length=30)
    video_name = models.CharField(max_length=30)


# 违规信息illegal表：
class Illegal(models.Model):
    id = models.IntegerField(primary_key=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    illegal_time = models.CharField(max_length=30)
    illegal_carplate = models.CharField(max_length=30)
    illegal_info = models.CharField(max_length=30)
    illegalImage = models.ForeignKey('IllegalImage',on_delete=models.CASCADE)


# 路口车流量统计表
class TrafficFlow(models.Model):
    id = models.IntegerField(primary_key=True)
    # video = models.ForeignKey('Video', on_delete=models.CASCADE)
    car_number = models.IntegerField()
    motor_number = models.IntegerField()
    people_number = models.IntegerField()


# 违规车辆图片表
class IllegalImage(models.Model):
    id = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=30)