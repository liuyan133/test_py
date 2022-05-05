# coding:utf8

class Mysql():

    HOST = "192.168.10.6"
    PASSWORD = ""


class Web():
    HOST = "192.168.10.6"
    PORT = 5000


class Config():
    mysql = Mysql
    web = Web


