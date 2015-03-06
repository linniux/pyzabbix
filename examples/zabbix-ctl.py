from pyzabbix import ZabbixAPI,ZabbixAPIException

import sys
from _warnings import filters

class AutoNaviZabbix(object):
    """docstring for AutoNaviZabbix"""

    version = 0.1
    
    def __init__(self, zabbix_server,user,password):
        super(AutoNaviZabbix, self).__init__()
        
        self.autonavi_zabbix_api = ZabbixAPI(zabbix_server)
        self.autonavi_zabbix_api.login(user,password)
     

    def get_group_and_id(self):
        """ return list """
        hostgroup_objects = self.autonavi_zabbix_api.hostgroup.getobjects()
        
        return hostgroup_objects
        
    def list_host_by_groupid(self,groupid):
        """ return list """
        hosts = self.autonavi_zabbix_api.host.get(output=["hostid","host","status","available"],groupid=groupid)
        
        return hosts
    
    def enable(self,id):

        self.autonavi_zabbix_api.host.update(hostid=id,status=0)
       

    def disable(self,id):

        self.autonavi_zabbix_api.host.update(hostid=id,status=1)




if __name__ == '__main__':
    ZABBIX_SERVER = 'http://10.16.18.5'
    t = AutoNaviZabbix(ZABBIX_SERVER,'wangzhiqian','wangzhiqian')
    
    
    hosts = t.list_host_by_groupid('213')
    status={"0":"OK","1":"Disabled"}
    available={"0":"Unknown","1":"available","2":"Unavailable"}
    
    for i in hosts:
        print "\\033[31m asdf "
        print "HostID : %s\t HostName : %s\t Status :\033[32m%s\033[0m \t Available :\033[31m%s\033[0m"
        print "hostid: \033[31m %s\033[0m \thost: %s\033[31m \tstatus: %s\033[31m \tavailable: %s\033[31m" % (i['hostid'],i['host'],status[i['status']],available[i['available']])
        t.enable(i['hostid'])
    
    sys.exit(3)
    
#############    get group and id #############    
    group_id = t.get_group_and_id()
    
    for i_dic in group_id:
        #i_dic.pop('internal')
        #i_dic.pop('flags')
        print "hostgroup: \033[31m %s\033[0m \tgroupid: %s" % (i_dic['name'],i_dic['groupid'])
        #for key in i_dic:
        #   print key,"\t->\t",i_dic[key],'\n'
   