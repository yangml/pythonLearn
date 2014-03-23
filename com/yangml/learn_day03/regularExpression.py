#coding=gbk
'''
Created on 2014年3月23日

@author: bling
'''
#语法
import re
m = re.search('[0-9]', 'dcnf5mggk9')
print m.group(0),m.group(0)
#正则表达式的函数
'''
m = re.search(pattern, string)  # 搜索整个字符串，直到发现符合的子字符串。
m = re.match(pattern, string)   # 从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
str = re.sub(pattern, replacement, string) 
# 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
re.split()    # 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
re.split()    # 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
'''
'''
1）单个字符:

.          任意的一个字符

a|b        字符a或字符b
[afg]      a或者f或者g的一个字符        
[0-4]      0-4范围内的一个字符
[a-f]      a-f范围内的一个字符
[^m]       不是m的一个字符
\s         一个空格
\S         一个非空格
\d         [0-9]
\D         [^0-9]
\w         [0-9a-zA-Z]
\W         [^0-9a-zA-Z]
2）重复
紧跟在单个字符之后，表示多个这样类似的字符
*         重复 >=0 次
+         重复 >=1 次
?         重复 0或者1 次
{m}       重复m次。比如说 a{4}相当于aaaa，再比如说[1-3]{2}相当于[1-3][1-3]
{m, n}    重复m到n次。比如说a{2, 5}表示a重复2到5次。小于m次的重复，或者大于n次的重复都不符合条件。
正则表达          相符的字符串举例

[0-9]{3,5}       9678

a?b              b

a+b              aaaaab
3) 位置
^         字符串的起始位置
$         字符串的结尾位置
正则表达                          相符的字符串举例                            不相符字符串

^ab.*c$          abeec               cabeec (如果用re.search(), 将无法找到。)
4）返回控制

我们有可能对搜索的结果进行进一步精简信息。比如下面一个正则表达式：

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

