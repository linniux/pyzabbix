
from pyzabbix import ZabbixAPI,ZabbixAPIException

import sys

ZABBIX_SERVER = 'http://10.16.18.5'

def main():

    autonavi_zabbix_api = ZabbixAPI(ZABBIX_SERVER)
    autonavi_zabbix_api.login('wangzhiqian','wangzhiqian')
    print "Connected to Zabbix API Version %s" % autonavi_zabbix_api.api_version()

    host_name = 'aes'
    #print autonavi_zabbix_api.host.get(filter={"host": host_name},selectInterfaces=["interfaceid"])
    v = autonavi_zabbix_api.hostgroup.getobjects(groupids=["213"])
    print v
    sys.exit(3)
    print type(v)
    for i in v:
        #print "hostgroup:  \033[31m%s\033[0m \tgroupid : %s" %(group['name'],group['groupid'])
        print "hostgroup: \033[31m %s\033[0m \tgroupid: %s" % (i['name'],i['groupid'])

def disable():
    autonavi_zabbix_api = ZabbixAPI(ZABBIX_SERVER)
    autonavi_zabbix_api.login('wangzhiqian','wangzhiqian')
    print "Connected to Zabbix API Version %s" % autonavi_zabbix_api.api_version()
    #autonavi_zabbix_api.hostgroup.update(groupid='213',)    


if __name__ == '__main__':
    main()