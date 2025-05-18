Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import json as j
j
<module 'json' from 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\json\\__init__.py'>
li = [1,2,3,4, 5.6, 7.8, True, False, (12,34,56), None, 'asdasda']
li
[1, 2, 3, 4, 5.6, 7.8, True, False, (12, 34, 56), None, 'asdasda']
type(li)
<class 'list'>
res = j.dumps(li, indent=4)
print(res)
[
    1,
    2,
    3,
    4,
    5.6,
    7.8,
    true,
    false,
    [
        12,
        34,
        56
    ],
    null,
    "asdasda"
]
type(res)
<class 'str'>
res_list = j.loads(res)
res_list
[1, 2, 3, 4, 5.6, 7.8, True, False, [12, 34, 56], None, 'asdasda']
res_list[2]
3
res
'[\n    1,\n    2,\n    3,\n    4,\n    5.6,\n    7.8,\n    true,\n    false,\n    [\n        12,\n        34,\n        56\n    ],\n    null,\n    "asdasda"\n]'



>>> li = {1:2, 3:4, 5.6:7.8, "true":True, "f":False, "tulpe":(12, 34, 56), "none":None, "text":'asdasda'}
>>> type(li)
<class 'dict'>
>>> res_json = j.dumps(li, indent=4)
>>> print(res_json)
{
    "1": 2,
    "3": 4,
    "5.6": 7.8,
    "true": true,
    "f": false,
    "tulpe": [
        12,
        34,
        56
    ],
    "none": null,
    "text": "asdasda"
}
>>> 
>>> 
>>> 
>>> next_system = j.loads(res_json)
>>> next_system
{'1': 2, '3': 4, '5.6': 7.8, 'true': True, 'f': False, 'tulpe': [12, 34, 56], 'none': None, 'text': 'asdasda'}
>>> next_system["5,6"] = 555555
>>> next_system_to_send = j.dumps(next_system)
>>> print(next_system_to_send)
{"1": 2, "3": 4, "5.6": 7.8, "true": true, "f": false, "tulpe": [12, 34, 56], "none": null, "text": "asdasda", "5,6": 555555}
>>> next_system_to_send = j.dumps(next_system, indent=8)
>>> print(next_system_to_send)
{
        "1": 2,
        "3": 4,
        "5.6": 7.8,
        "true": true,
        "f": false,
        "tulpe": [
                12,
                34,
                56
        ],
        "none": null,
        "text": "asdasda",
        "5,6": 555555
}
