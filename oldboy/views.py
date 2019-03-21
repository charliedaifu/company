from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from oldboy.models import *
import json

def index(request):
    slider_obj = SlideShow.objects.all()
    course_obj = Course.objects.all()
    notice_obj = Notice.objects.all()
    return render(request,'index.html',locals())

def video(request,*args,**kwargs):
    '''按照分类、等级筛选（只有一对多）：/video-0-0-0.html'''
    condition = {}
    print(kwargs)
    for k,v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp
        if temp:   # 如果请求的ID不为0，就加入筛选字典中，如果请求ID为0，筛选字典就为空，查询的就是全部video
            condition[k] = temp
    class_list = Classification.objects.all()
    level_list = Level.objects.all()
    '''
    status_choice = [(1, '上线'), (2, '下线')]
    '''
    #列表转字典
    # status_list = list(map(lambda x:{'id':x[0],'name':x[1]},Video.status_choice))
    #{{ item.name }}
    status_list = Video.status_choice
    video_list = Video.objects.filter(**condition)
    print(video_list)
    return render(
        request,
        'video.html',
        {
            'class_list':class_list,
            'level_list':level_list,
            'kwargs':kwargs,
            'video_list':video_list,
            'status_list':status_list
        }
    )

def video2(request,*args,**kwargs):
    '''
    按照方向、分类、等级筛选（一对多，多对多）
    如果direction_id = 0： 列出所有分类
        如果 classification_id = 0：pass
        否则：condition['classification_id'] = classification_id
    否则：列出该方向下的所有分类
        如果 classification_id = 0：获取当前方向下的所有分类[1,2,3,4]
            condition['classification_id__in'] = [1,2,3,4]
        否则：获取当前方向下的所有分类[1,2,3,4]
            classification_id 是否在[1,2,3,4]中：
                如果在：condition['classification_id'] = classification_id
                否则：condition['classification_id__in'] = [1,2,3,4]
    '''
    condition = {}
    print(kwargs)
    for k, v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp

    direction_id = kwargs.get('direction_id')
    classification_id = kwargs.get('classification_id')
    level_id = kwargs.get('level_id')

    direction_list = Direction.objects.all()
    level_list = Level.objects.all()
    if direction_id == 0:
        # 如果方向ID为0，获取所有的分类
        class_list = Classification.objects.all()
        if classification_id == 0:
            # 如果分类ID也为0，还是获取所有分类
            pass
        else:
            # 如果分类ID不为0，按照当前分类ID筛选
            condition['classification_id'] = classification_id
    else:
        # 如果方向ID不为0，先获取当前方向下的所有分类
        direction_obj = Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()
        vlist = direction_obj.classification.all().values_list('id')  # QeurySet[(1,),(2,)]
        if not vlist:
            # 如果当前方向下没有任何分类
            classification_id_list = []
        else:
            classification_id_list = list(zip(*vlist))[0]
        if classification_id == 0:
            # 如果方向ID不是0，分类ID是0，就显示当前方向下所有分类
            condition['classification_id__in'] = classification_id_list
        else:
            # 如果方向和分类都不是0
            if classification_id in classification_id_list:
                #如果当前分类在当前方向中，就按照当前分类ID查询
                condition['classification_id'] = classification_id
            else:
                #如果当前分类不在当前方向中，就按照当前方向查询，忽略当前分类
                #当你只选中方向，还没有选中分类时，让分类ID=0，就是选择全部
                kwargs['classification_id'] = 0
                condition['classification_id__in'] = classification_id_list
    if level_id == 0:
        pass
    else:
        condition['level_id'] = level_id

    video_list = Video.objects.filter(**condition)
    return render(
        request,
        'video2.html',
        {
            'direction_list':direction_list,
            'class_list':class_list,
            'level_list': level_list,
            'video_list': video_list,
            'kwargs':kwargs
        }
    )

def course(request):
    course_list = Course.objects.all()
    return render(request,'course.html',locals())

def get_course(request):
    nid = request.GET.get('nid')
    #每次只取大于nid的数据，就是从上一次最后一张的下一张开始
    course_list = Course.objects.filter(id__gt=nid).values('id','img','name','summary')
    print(course_list)
    course_list = list(course_list)
    ret = {
        'status':True,
        'data':course_list
    }
    #JsonResponse默认只能发送字典，如果是列表，需要加参数safe=False
    return JsonResponse(ret)

def aboutUs(request):
    '''关于我们'''
    return render(request,'aboutUs.html')

def teachers(request):
    '''师资团队'''
    # th_list = Teacher.objects.values('name','age','summary')
    th_list = Teacher.objects.all()
    '''
    course_list = {}
    for item in th_list:
        if item['name'] not in course_list.keys():
            course_list[item['name']] = [item['course__name'],]
        else:
            course_list[item['name']].append(item['course__name'])
    print(course_list)
    '''
    return render(request,'teachers.html',locals())

def students(request):
    '''学员就业'''
    st_list = Student.objects.all()
    slider_obj = SlideShow.objects.all()
    return render(request,'students.html',locals())

def more_info(request):
    '''学员更多信息'''
    st_id = request.GET.get('p')
    more_info = Student.objects.filter(id=st_id).values('letter__title','letter__content')
    print(more_info)
    return render(request,'more_info.html',{'more_info':more_info})

