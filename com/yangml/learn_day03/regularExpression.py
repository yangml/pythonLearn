#coding=gbk
'''
Created on 2014��3��23��

@author: bling
'''
#�﷨
import re
m = re.search('[0-9]', 'dcnf5mggk9')
print m.group(0),m.group(0)
#������ʽ�ĺ���
'''
m = re.search(pattern, string)  # ���������ַ�����ֱ�����ַ��ϵ����ַ�����
m = re.match(pattern, string)   # ��ͷ��ʼ����ַ����Ƿ����������ʽ��������ַ����ĵ�һ���ַ���ʼ�������
str = re.sub(pattern, replacement, string) 
# ��string����������任pattern�����������������������ַ���������һ�ַ���replacement�滻�������滻����ַ�����
re.split()    # ����������ʽ�ָ��ַ����� ���ָ����������ַ�������һ����(list)�з���
re.split()    # ����������ʽ�ָ��ַ����� ���ָ����������ַ�������һ����(list)�з���
'''
'''
1�������ַ�:

.          �����һ���ַ�

a|b        �ַ�a���ַ�b
[afg]      a����f����g��һ���ַ�        
[0-4]      0-4��Χ�ڵ�һ���ַ�
[a-f]      a-f��Χ�ڵ�һ���ַ�
[^m]       ����m��һ���ַ�
\s         һ���ո�
\S         һ���ǿո�
\d         [0-9]
\D         [^0-9]
\w         [0-9a-zA-Z]
\W         [^0-9a-zA-Z]
2���ظ�
�����ڵ����ַ�֮�󣬱�ʾ����������Ƶ��ַ�
*         �ظ� >=0 ��
+         �ظ� >=1 ��
?         �ظ� 0����1 ��
{m}       �ظ�m�Ρ�����˵ a{4}�൱��aaaa���ٱ���˵[1-3]{2}�൱��[1-3][1-3]
{m, n}    �ظ�m��n�Ρ�����˵a{2, 5}��ʾa�ظ�2��5�Ρ�С��m�ε��ظ������ߴ���n�ε��ظ���������������
������          ������ַ�������

[0-9]{3,5}       9678

a?b              b

a+b              aaaaab
3) λ��
^         �ַ�������ʼλ��
$         �ַ����Ľ�βλ��
������                          ������ַ�������                            ������ַ���

^ab.*c$          abeec               cabeec (�����re.search(), ���޷��ҵ���)
4�����ؿ���

�����п��ܶ������Ľ�����н�һ��������Ϣ����������һ��������ʽ��

output_(\d{4})
'''
m = re.search("output_(\d{4})", "output_1986.txt")
print m.group(1);

m = re.search("output_(?P<year>\d{4})", "output_1999.txt")
print m.group("year")

import datetime

filename ="output_2014.03.23.txt" 
gettime = re.search("(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})\.", filename)
year = gettime.group("year")
mounth = gettime.group("month")
day = gettime.group("day")
print year,'-',mounth,'-',day
date = datetime.date(int(year),int(mounth),int(day))
wd = date.weekday()+1
print str(wd)
filename = "output_"+year+"-"+mounth+"-"+day+"-"+str(wd)+".txt"
#os.rename(filename, "output_"+year+"-"+mounth+"-"+day+"-"+str(wd)+".txt")
print filename

