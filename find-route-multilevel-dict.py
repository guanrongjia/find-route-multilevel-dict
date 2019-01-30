# coding=utf8
'''
date: 2019/01/30
powered by guanrongjia
all rights reserved

ability:
this demo show you how to sacn a dict to find the value that you given.
it records the value and the router of zhe key you given .
there are a lot of ways to realize it,
hrer is just one way ,
enjoy coding!

if there is any thing you want to communicate with me ,
leave message in my git:

'''
import copy


demo_dect = {
    'TASKBAR': {
        'WINKEY': {
            'CLOUDMUSIC': 0
        },
        'POWER': {
            'POWER_OPTIONS': 0
        }

    },
    'DESKTOP': {
        'THIS_PC': {
            'TUDOU': 0
        }
    }
}


def find_by_exhaustion(input_key, current_dict, router):
    '''
    :param input_key:  the key you given
    :param current_dict: the dict you have to scan
    :param router: record your route to reach here
    :return:
    '''
    router = copy.deepcopy(router)
    for index, key in enumerate(current_dict):
        val = current_dict.get(key)
        if input_key == key:
            router.append(key)
            return val, router
        elif type(val) == type({}):
            router.append(key)
            result_tuple = find_by_exhaustion(input_key, val, router)
            if result_tuple:
                return result_tuple[0], result_tuple[1]
            else:
                if router:
                    router = router[0:len(router) - 1]


def test_fun():
    '''
    this function show you how to use and test your program.
    :return:
    '''
    key_list = ['TASKBAR', 'WINKEY', 'CLOUDMUSIC', 'POWER', 'POWER_OPTIONS', 'DESKTOP', 'THIS_PC', 'TUDOU',
                '', None, 0, 'no_match_str'
                ]
    for input_key in key_list:
        print '*' * 25,
        print input_key,
        print '*' * 25

        router = []
        result = find_by_exhaustion(input_key, demo_dect, router)
        if result:
            print 'value:'
            print result[0]
            print 'router:'
            print result[1]

if __name__ == '__main__':
    test_fun()
