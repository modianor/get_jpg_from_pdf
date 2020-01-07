# *_*coding:utf-8 *_*
#
path = 'D:\\pycharm_workspace\\get_jpg_from_pdf\\data\\01 CN201822117441-一种可调节角度的家用高清实时监控设备-实用新型.pdf'

print(path)
print(path.rfind('\\'))
print(path.rfind('.'))
print(path[path.rfind('/') + 1:path.find('.')])
