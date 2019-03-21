from django.db import models

class SlideShow(models.Model):
    '''轮播图表'''
    name = models.CharField(max_length=32,verbose_name='图片名称',unique=True)
    img = models.ImageField(upload_to='static/img/sliders',verbose_name='图片路径')
    target = models.CharField(max_length=256,verbose_name='跳转路径')
    status = models.IntegerField(
        choices=[(1,'上线'),(2,'下线')],
        verbose_name='状态',
        default=1
    )
    weight = models.IntegerField(verbose_name='权重')
    create_date = models.DateTimeField(auto_now_add=True)#默认当前时间
    class Meta:
        verbose_name_plural = '轮播图'  #admin显示表名
    def __str__(self):
        return self.name

class Course(models.Model):
    '''课程表'''
    name = models.CharField(max_length=32,verbose_name='课程',unique=True)
    summary = models.CharField(max_length=150,verbose_name='简介')
    img = models.ImageField(upload_to='static/img/course', verbose_name='图片路径')
    status_choice = [(1, '上线'), (2, '下线')]
    status = models.IntegerField(
        choices=status_choice,
        verbose_name='状态',
        default=1
    )
    weight = models.IntegerField(verbose_name='权重')
    class Meta:
        verbose_name_plural = '课程'
    def __str__(self):
        return self.name

class Direction(models.Model):
    '''视频方向'''
    name = models.CharField(max_length=32, verbose_name='名称')
    classification = models.ManyToManyField('Classification')
    class Meta:
        verbose_name_plural = '方向'
    def __str__(self):
        return self.name

class Classification(models.Model):
    '''视频分类'''
    name = models.CharField(max_length=32, verbose_name='名称')
    class Meta:
        verbose_name_plural = '分类'
    def __str__(self):
        return self.name

class Video(models.Model):
    '''视频信息'''
    status_choice = [(1, '上线'), (2, '下线')]
    weight = models.IntegerField(verbose_name='权重',default=0)
    name = models.CharField(max_length=32, verbose_name='名称')
    status = models.IntegerField(
        choices=status_choice,
        verbose_name='状态',
        default=1
    )
    level = models.ForeignKey('Level',on_delete=models.CASCADE)
    classification = models.ForeignKey('Classification',on_delete=models.CASCADE,null=True,blank=True)
    summary = models.CharField(max_length=150, verbose_name='简介')
    detail = models.CharField(max_length=1000, verbose_name='详细')
    img = models.ImageField(upload_to='static/img/course', verbose_name='视频图片')
    class Meta:
        verbose_name_plural = '视频'
    def __str__(self):
        return self.name

class Level(models.Model):
    '''难度级别'''
    title = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = '难度级别'
    def __str__(self):
        return self.title

class Notice(models.Model):
    '''最新公告'''
    title = models.CharField(max_length=32,verbose_name='标题')
    summary = models.CharField(max_length=150, verbose_name='简介')
    detail = models.TextField(max_length=1000, verbose_name='详细')
    weight = models.IntegerField(verbose_name='权重', default=0)
    status_choice = [(1, '上线'), (2, '下线')]
    status = models.IntegerField(
        choices=status_choice,
        verbose_name='状态',
        default=1
    )
    class Meta:
        verbose_name_plural = '最新公告'
    def __str__(self):
        return self.title

class Student(models.Model):
    '''学生信息表'''
    name = models.CharField(max_length=32,verbose_name='姓名')
    company = models.CharField(max_length=64,verbose_name='就业单位')
    salary = models.CharField(max_length=32,verbose_name='薪资')
    img = models.ImageField(upload_to='static/img/students', verbose_name='图片路径',blank=True,null=True)
    letter = models.OneToOneField('LetterOfThanks',on_delete=models.CASCADE,blank=True,null=True)
    weight = models.IntegerField(verbose_name='权重', default=0)
    status_choice = [(1, '上线'), (2, '下线')]
    status = models.IntegerField(
        choices=status_choice,
        verbose_name='状态',
        default=1
    )
    class Meta:
        verbose_name_plural = '学生信息'
    def __str__(self):
        return self.name

class LetterOfThanks(models.Model):
    '''学生感谢信'''
    title = models.CharField(max_length=32,verbose_name='标题')
    content = models.TextField(max_length=5000,verbose_name='内容')
    class Meta:
        verbose_name_plural = '学生感谢信'
    def __str__(self):
        return self.title

class Teacher(models.Model):
    '''老师信息表'''
    name = models.CharField(max_length=32,verbose_name='姓名')
    age = models.CharField(max_length=20,verbose_name='年龄')
    course = models.ManyToManyField('Course',related_name='th',verbose_name='负责课程')
    summary = models.CharField(max_length=300, verbose_name='简介')
    weight = models.IntegerField(verbose_name='权重', default=0)
    status_choice = [(1, '上线'), (2, '下线')]
    status = models.IntegerField(
        choices=status_choice,
        verbose_name='状态',
        default=1
    )
    class Meta:
        verbose_name_plural = '老师信息'
    def __str__(self):
        return self.name