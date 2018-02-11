# -*- coding: utf-8 -*-
#! /usr/bin/env python3
import sys
from pymongo import MongoClient


def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    # 计算用户 user_id 的排名、总分数及花费的总时间
    TODO

    # 依次返回排名，分数和时间，不能修改顺序
    return rank, score, submit_time


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Parameter Error')

    try:
        user_id = int(sys.argv[1])
    except:
        print('Parameter Error')

    userdata = get_rank(user_id)
    print(userdata)
