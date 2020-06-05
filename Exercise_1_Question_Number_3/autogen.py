print ('Input the Number of Records')
n = int(input())

unique_router_details = []
host_name_1=10
host_name_2=192
host_name_3=186
host_name_4=23

for i in range(n):
    childrecord = dict()
    childrecord['sapid']='SAP'+str(i)

    host_name_1 += 1 
    host_name_2 += 1 
    host_name_3 += 1 
    host_name_4 += 1

    childrecord['hostname']=str(host_name_1) + '.' + str(host_name_2) + '.' + str(host_name_3) + '.' + str(host_name_4) 
    unique_router_details.append(childrecord)


print (unique_router_details)
