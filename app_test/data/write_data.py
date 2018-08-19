#coding=utf-8
import yaml
import datetime

def write_data():
    data={
        "chinese":"事实上",
        "time":111,
        "date":[1, 2, 3, 4],
        "dat22": {'g1':1,'g2':2},
        't1':datetime.date(2017, 10, 1),
        't2':datetime.datetime(2017, 10, 1, 11,11,11),
        't2':datetime.time( 11,11,11),
        'null':None,
        'null2':''


    }
    with open("./write_data.yml","w") as f :
        yaml.dump(data,f,encoding="utf-8",allow_unicode=True)

if __name__ == '__main__':
    write_data()