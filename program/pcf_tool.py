#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
import os
parameter1="f=mobilePlayInfo"
parameter2="token=853656fb7c61ba9d5aa99b9e9032e56"
parameter3="accessType=99"
parameter4="iosid"
parameter4="clienttype=5"
parameter5="plat=32"
parameter6="channelID=01788020"
parameter7="contentid=C39744665"
parameter8="devid=000001"
parameter9="pcode=4"
parameter10="appid=111010410087"
parameter11="ac=play"
parameter12="time=20170407003703"
#sign	918b6282e073d0e541026de548168834
"""
import time
import re

#配置shadowsocks流程	
def config_shadowsocks():
	shadowsocks_config=[]
	config_proxy_type="SHADOWSOCKS"
	config_proxy_host=raw_input("输入服务器地址：")
	config_proxy_port=raw_input("输入服务器端口：")
	print("============\n加密方式：\n1:aes-128-ctr\n2:aes-192-ctr\n3:aes-256-ctr\n4:aes-128-cfb\n5:aes-192-cfb\n6:aes-256-cfb\n7:bf-cfb\n8:camellia-128-cfb\n9:camellia-192-cfb\n10:camellia-256-cfb\n11:chacha20\n12:chacha20-ietf\n13:rc4-md5\n14salsa20\n")
	config_proxy_encryption=raw_input("加密方式（默认为6）：")
	if config_proxy_encryption == "1":
		config_proxy_encryption = "aes-128-ctr"
	elif config_proxy_encryption == "2":
		config_proxy_encryption = "aes-192-ctr"
	elif config_proxy_encryption == "3":
		config_proxy_encryption = "aes-256-ctr"
	elif config_proxy_encryption == "4":
		config_proxy_encryption = "aes-128-cfb"
	elif config_proxy_encryption == "5":
		config_proxy_encryption = "aes-192-cfb"
	elif config_proxy_encryption == "6":
		config_proxy_encryption = "aes-256-cfb"
	elif config_proxy_encryption == "7":
		config_proxy_encryption = "bf-cfb"
	elif config_proxy_encryption == "8":
		config_proxy_encryption = "camellia-128-cfb"
	elif config_proxy_encryption == "9":
		config_proxy_encryption = "camellia-192-cfb"
	elif config_proxy_encryption == "10":
		config_proxy_encryption = "camellia-256-cfb"
	elif config_proxy_encryption == "11":
		config_proxy_encryption = "chacha20"
	elif config_proxy_encryption == "12":
		config_proxy_encryption = "chacha20-ietf"
	elif config_proxy_encryption == "13":
		config_proxy_encryption = "rc4-md5"
	elif config_proxy_encryption == "14":
		config_proxy_encryption = "salsa20"
	else:
		config_proxy_encryption = "aes-256-cfb"
	config_proxy_password=raw_input("输入密码：")
	config_proxy_remark=raw_input("输入代理的备注名：")
	shadowsocks_config.extend([config_proxy_type,config_proxy_host,config_proxy_port,config_proxy_encryption,config_proxy_password,config_proxy_remark])
	return shadowsocks_config

#配置shadowsocksR流程
def config_shadowsocksR():
	shadowsocksR_config = []
	config_proxy_type="SHADOWSOCKSR"
	config_proxy_host=raw_input("输入服务器地址：")
	config_proxy_port=raw_input("输入服务器端口：")
	print("============\n加密方式：\n1:aes-128-ctr\n2:aes-192-ctr\n3:aes-256-ctr\n4:aes-128-cfb\n5:aes-192-cfb\n6:aes-256-cfb\n7:bf-cfb\n8:camellia-128-cfb\n9:camellia-192-cfb\n10:camellia-256-cfb\n11:chacha20\n12:chacha20-ietf\n13:rc4-md5\n14salsa20\n")
	config_proxy_encryption=raw_input("加密方式（默认为6）：")
	if config_proxy_encryption == "1":
		config_proxy_encryption = "aes-128-ctr"
	elif config_proxy_encryption == "2":
		config_proxy_encryption = "aes-192-ctr"
	elif config_proxy_encryption == "3":
		config_proxy_encryption = "aes-256-ctr"
	elif config_proxy_encryption == "4":
		config_proxy_encryption = "aes-128-cfb"
	elif config_proxy_encryption == "5":
		config_proxy_encryption = "aes-192-cfb"
	elif config_proxy_encryption == "6":
		config_proxy_encryption = "aes-256-cfb"
	elif config_proxy_encryption == "7":
		config_proxy_encryption = "bf-cfb"
	elif config_proxy_encryption == "8":
		config_proxy_encryption = "camellia-128-cfb"
	elif config_proxy_encryption == "9":
		config_proxy_encryption = "camellia-192-cfb"
	elif config_proxy_encryption == "10":
		config_proxy_encryption = "camellia-256-cfb"
	elif config_proxy_encryption == "11":
		config_proxy_encryption = "chacha20"
	elif config_proxy_encryption == "12":
		config_proxy_encryption = "chacha20-ietf"
	elif config_proxy_encryption == "13":
		config_proxy_encryption = "rc4-md5"
	elif config_proxy_encryption == "14":
		config_proxy_encryption = "salsa20"
	else:
		config_proxy_encryption = "aes-256-cfb"
	config_proxy_password=raw_input("输入密码：")
	print("============\n协议(protocol)类型：\n1:origin\n2:auth_sha1_v4\n3:auth_aes128_md5\n4:auth_aes128_sha1\n5:verify_simple(不推荐)\n6:verify_sha1(deprecated(不推荐)\n7:auth_simple(不推荐)\n8:auth_sha1(不推荐)\n9:auth_sha1_v2(不推荐)\n")
	config_proxy_protocol=raw_input("选择协议（默认为1）：")
	if config_proxy_protocol == "1":
		config_proxy_protocol = "origin"
	elif config_proxy_protocol == "2":
		config_proxy_protocol = "auth_sha1_v4"
	elif config_proxy_protocol == "3":
		config_proxy_protocol = "auth_aes128_md5"
	elif config_proxy_protocol == "4":
		config_proxy_protocol = "auth_aes128_sha1"
	elif config_proxy_protocol == "5":
		config_proxy_protocol = "verify_simple"
	elif config_proxy_protocol == "6":
		config_proxy_protocol = "verify_sha1"
	elif config_proxy_protocol == "7":
		config_proxy_protocol = "auth_simple"
	elif config_proxy_protocol == "8":
		config_proxy_protocol = "auth_sha1"
	elif config_proxy_protocol == "9":
		config_proxy_protocol = "auth_sha1_v2"
	else:
		config_proxy_protocol = "origin"
	config_proxy_protocolParam=raw_input("输入协议参数：")
	print("============\n混淆(Obfs)类型：\n1:plain\n2:tls1.2_ticket_auth\n3:http_simple\n4:http_post\n5:random_head(不推荐)\n")
	config_proxy_obfs=raw_input("选择混淆协议（默认为1）")
	if config_proxy_obfs == "1":
		config_proxy_obfs = "plain"
	elif config_proxy_obfs == "2":
		config_proxy_obfs = "tls1.2_ticket_auth"
	elif config_proxy_obfs == "3":
		config_proxy_obfs = "http_simple"
	elif config_proxy_obfs == "4":
		config_proxy_obfs = "http_post"
	elif config_proxy_obfs == "5":
		config_proxy_obfs = "random_head"
	else:
		config_proxy_obfs = "plain"
	config_proxy_obfsParam=raw_input("输入混淆参数：")
	config_proxy_remark=raw_input("输入代理的备注名：")
	shadowsocksR_config.extend([config_proxy_type,config_proxy_host,config_proxy_port,config_proxy_encryption,config_proxy_password,config_proxy_protocol,config_proxy_protocolParam,config_proxy_obfs,config_proxy_obfsParam,config_proxy_remark])
	return shadowsocksR_config

#配置SOCKS5流程
def config_socks5():
	socks_config = []
	config_proxy_type="SOCKS5"
	config_proxy_remark=raw_input("输入代理的备注名：")
	config_proxy_host=raw_input("输入服务器地址：")
	config_proxy_port=raw_input("输入服务器端口：")
	print("============\n是否需要认证\n0:不需要\n1:需要")
	config_proxy_confirm_method=raw_input("是否需要认证(默认为1)：")
	if config_proxy_confirm_method == 0:
		config_proxy_confirm_method = "NONE"
		socks_config.extend([config_proxy_type,config_proxy_host,config_proxy_port,config_proxy_confirm_method,config_proxy_remark])
	elif config_proxy_confirm_method == "1":
		config_proxy_confirm_method = "PASSWORD"
		config_proxy_user=raw_input("输入用户名：")
		config_proxy_password=raw_input("输入密码：")
		socks_config.extend([config_proxy_type,config_proxy_host,config_proxy_port,config_proxy_confirm_method,config_proxy_user,config_proxy_password,config_proxy_remark])
	else:
		config_proxy_confirm_method = "PASSWORD"
		config_proxy_user=raw_input("输入用户名：")
		config_proxy_password=raw_input("输入密码：")
		socks_config.extend([config_proxy_type,config_proxy_host,config_proxy_port,config_proxy_confirm_method,config_proxy_user,config_proxy_password,config_proxy_remark])
	return socks_config
	
config_Header="name = \"一名法学生的配置文档\"\nemail = \"a79865863@gmail.com\"\nwebsite = \"http://sharex.win:878\"\ndescription = \"一名法学生的代理配置\"\n\n"
config_proxy_number=raw_input("你需要设置的代理数量（如1个，就输入1）：")
config_proxy_array = [] #用以存放代理的配置
for num in range(0,int(config_proxy_number)):
	print("============\n代理的类型：\n1:SHADOWSOCKS\n2:SHADOWSOCKSR\n3:SOCKS5\n4:SOCKS5 over TLS\n")
	config_proxy_type=raw_input("输入代理的类型（默认为1）：")
	if config_proxy_type == "1":
		config_proxy_array.append(config_shadowsocks())
	elif config_proxy_type == "2":
		config_proxy_array.append(config_shadowsocksR())
	elif config_proxy_type == "3":
		config_proxy_array.append(config_socks5())
	elif config_proxy_type == "4":
		config_proxy_array.append(config_socks5())
	else:
		config_proxy_array.append(config_shadowsocks())
#获取规则列表文件
proxy_rules_file=open("PROXY.txt","r")
direct_rules_file=open("DIRECT.txt","r")
reject_rules_file=open("REJECT.txt","r")

#生成配置文件
generate_config_file=open("sharex_config.pcf","w")
header_content="".join(["##################################\n#                                #\n#    PCF生成器作者：一名法学生      #\n#    生成器出品时间：2017年4月7日   #\n#                                #\n###################################\n\n\n#配置参数生成时间：",time.strftime('%Y-%m-%d',time.localtime(time.time())),"\n",config_Header])
proxy_content="#代理（Proxy）\n"
#循环代理配置
for index in range(len(config_proxy_array)):
	if config_proxy_array[index][0] == "SHADOWSOCKS":
		proxy_content="".join([proxy_content,"[PROXY.sharex",str(index),"]\ntype = \"",config_proxy_array[index][0],"\"\nhost = \"",config_proxy_array[index][1],"\"\nport = ",config_proxy_array[index][2],"\nencryption = \"",config_proxy_array[index][3],"\"\npassword = \"",config_proxy_array[index][4],"\"\nremark = \"",config_proxy_array[index][5],"\"\n\n"])
		#proxy_content=config_proxy_array[index][1]+config_proxy_array[index][2]+config_proxy_array[index][3]+config_proxy_array[index][4]
	elif config_proxy_array[index][0] == "SHADOWSOCKSR":
		proxy_content="".join([proxy_content,"[PROXY.sharex",str(index),"]\ntype = \"",config_proxy_array[index][0],"\"\nhost = \"",config_proxy_array[index][1],"\"\nport = ",config_proxy_array[index][2],"\nencryption = \"",config_proxy_array[index][3],"\"\npassword = \"",config_proxy_array[index][4],"\"\nprotocol = \"",config_proxy_array[index][5],"\"\nprotocolParam = \"",config_proxy_array[index][6],"\"\nobfs = \"",config_proxy_array[index][7],"\"\nobfsParam = \"",config_proxy_array[index][8],"\"\nremark = \"",config_proxy_array[index][9],"\"\n\n"])
	elif config_proxy_array[index][0] == "SOCKS5":
		if config_proxy_array[index][3] == "NONE":
		 	proxy_content="".join([proxy_content,"[PROXY.sharex",str(index),"]\ntype = \"",config_proxy_array[index][0],"\"\nhost = \"",config_proxy_array[index][1],"\"\nport = ",config_proxy_array[index][2],"\nremark = \"",config_proxy_array[index][4],"\"\n\n"])
		elif config_proxy_array[index][3] == "PASSWORD":
			proxy_content="".join([proxy_content,"[PROXY.sharex",str(index),"]\ntype = \"",config_proxy_array[index][0],"\"\nhost = \"",config_proxy_array[index][1],"\"\nport = ",config_proxy_array[index][2],"\nuser = \"",config_proxy_array[index][4],"\"\npassword = \"",config_proxy_array[index][5],"\"\nremark = \"",config_proxy_array[index][6],"\"\n\n"])
#循环经过代理的规则
proxy_rules="\n\n# 规则集\n[RULESET.sharexproxy]\nname = \"代理路线\"\nrules = [\n"
for proxy_rule in proxy_rules_file:
	proxy_rule=re.sub(r'[\n|,]','',proxy_rule)
	if re.match(r'\|\||!|----|\/\^|\[',proxy_rule,re.S|re.M):
		continue
	elif proxy_rule == "":
		continue
	else:
		proxy_rule =  re.sub(r'@@|\?|\\','',proxy_rule)
		proxy_rules="".join([proxy_rules,"\"DOMAIN-MATCH, ",proxy_rule,", PROXY\",\n"])
proxy_rules=re.sub(r',$','',proxy_rules)
proxy_rules="".join([proxy_rules,"]\n\n"])

direct_rules="# 规则集\n[RULESET.sharexdirect]\nname = \"本地网络\"\nrules = [\n"
for direct_rule in direct_rules_file:
	direct_rule=re.sub(r'[\n|,]','',direct_rule)
	if re.match(r'\|\||!|----|\/\^|\[',direct_rule,re.S|re.M):
		continue
	elif direct_rule == "":
		continue
	else:
		direct_rule =  re.sub(r'@@|\?|\\','',direct_rule)
		direct_rules="".join([direct_rules,"\"DOMAIN-MATCH, ",direct_rule,", DIRECT\",\n"])
direct_rules=re.sub(r',$','',direct_rules)
direct_rules="".join([direct_rules,"]\n\n"])

reject_rules="# 规则集\n[RULESET.sharexreject]\nname = \"拒绝链接\"\nrules = [\n"
for reject_rule in reject_rules_file:
	reject_rule=re.sub(r'[\n|,]','',reject_rule)
	if re.match(r'\|\||!|----|\/\^|\[',reject_rule,re.S|re.M):
		continue
	elif reject_rule == "":
		continue
	else:
		reject_rule =  re.sub(r'@@|\?|\\','',reject_rule)
		reject_rules="".join([reject_rules,"\"DOMAIN-MATCH, ",reject_rule,", REJECT\",\n"])
reject_rules=re.sub(r',$','',reject_rules)
reject_rules="".join([reject_rules,"]\n\n"])

#设置用户默认配置
default_config="".join(["\n\n# 用户配置（Profile）\n[PROFILE.sharex]\nname = \"Sharex代理\"\ndns = [\"8.8.8.8\"]\ndefault = \"PROXY\"\nproxy = \"share0\"\nrulesets = [\n\"sharexdirect\",\n\"sharexproxy\",\n\"sharexreject\"\n]\n\n\n\n"])
full_content="".join([header_content,default_config,proxy_content,proxy_rules,direct_rules,reject_rules])
generate_config_file.write(full_content)
generate_config_file.close()

proxy_rules_file.close()
direct_rules_file.close()
reject_rules_file.close()
