from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organization.models import CourseOrg,Teacher
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"课程名")
    desc = models.CharField(max_length=300,verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    is_banner = models.BooleanField(default=False,verbose_name=u"是否为轮播图")
    degree = models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=50,verbose_name="难度")
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长（分钟数）")
    teachers = models.ForeignKey(Teacher,verbose_name=u"讲师",blank=True,null=True)
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m",verbose_name=u"封面图",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    course_org = models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True)
    category = models.CharField(default="后端开发 ", max_length=20,verbose_name="课程类别")
    tag = models.CharField(default="",verbose_name="课程标签",max_length=10)
    youneed_now = models.CharField(default="",max_length=300,verbose_name="课程须知")
    teacher_tell = models.CharField(default="",max_length=300,verbose_name="老师告诉你")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return  self.lesson_set.all()


    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name

    def get_lesson_video(self):
        # 获取章节视频
        return  self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100,verbose_name=u"视频名称")
    url = models.CharField(default="",max_length=200,verbose_name=u"访问地址")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"名称")
    download = models.FileField(upload_to="coruse/resource/%Y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

