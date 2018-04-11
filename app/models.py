# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#新增元祖设置消息类型枚举
KIND_CHOICES=(
	('Python技术','Python技术'),
	('数据库技术','经济学'),
	('文体咨询','文体咨询'),
	('个人心请','genrenxinqong'),)
# Create your models here.
class Moment(models.Model):
	content=models.CharField(max_length=200)
	user_name=models.CharField(max_length=20,default='匿名')
#修改kind类型，加入choice参数
	kind=models.CharField(max_length=20,choices=KIND_CHOICES,
	default=KIND_CHOICES[0])
