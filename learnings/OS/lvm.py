### Version 2.0

import os
import sys

disk=input("enter a disk to format :")
cmd="gdisk "+disk
#print(cmd)
os.system(cmd)
if cmd:
    partition_number=input("enter the partition number you want to format :")
    mkfs="mkfs.ext4 "+disk+partition_number
    print("Creating a LVM :")
    pv="pvcreate "+disk+partition_number
    print ("Creating a LVM now :")
    os.system(pv)
    vg_name=input("enter a VG name :")
    vg_create="vgcreate "+vg_name+" "+disk+partition_number
    os.system(vg_create)
    print("Creating LVM now : ")
    lv_name=input("enter LV name :")
    lv_size=input("enter the size of LV in M or G like 110M or 2G :")
    lv_create="lvcreate "+"--size"+" "+lv_size+" "+"--name "+lv_name+" "+vg_name
    os.system(lv_create)
    lvdisp="lvdisplay"+" "+lv_name
    os.system(lvdisp)
else:
    print("disk entered is wrong try to enter corect disk")
    exit()
lvremov=input("want to remove created LVM y|n : ")

if lvremov=='y':
    lv_rm_cmd="lvremove "+"/dev/"+vg_name+"/"+lv_name
    os.system(lv_rm_cmd)
    vg_rm_cmd="vgremove "+vg_name
    os.system(vg_rm_cmd)
    pv_rm_cmd="pvremove "+disk+partition_number
    os.system(pv_rm_cmd)
else:
    print ("your LVM is /dev/{}/{}".format(vg_name,lv_name))

