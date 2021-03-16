import os
import subprocess

print("\n\t\t\tWelcome to the LVM automation\n")
c = 'y'
c = input("press y to continue: ")
while(c == 'y'  or c == 'Y'):
   print("\nHere are your options:")
   print("1. To see the no. of disks attached..                                           2. to create a new physical volume..                                            3. To display physical volume..                                                 4. To create a new volume group..                                               5. To display volume group..                                                    6. To create a new logical volume..                                             7. To display logical volume..                                                  8. To extend the logical volume..")

   ch = input("\nPress any one of the above choice:")
   if ch == '1':
     os.system("fdisk -l")

   elif ch == '2':
       x2 = 'y'
       while(x2 == 'y' or x2 == 'Y'):
         disk = input("\nEnter the disk/device u want to create a PV(full device name):")
         os.system("pvcreate {}".format(disk))
         x2 = input("\nDo u want to create more PV's(y/n):")

   elif ch == '3':
       os.system("pvdisplay")

   elif ch == '4':
       x4 = 'y'
       count = 0 
       vg_d = ""
       vg_name = input("\nEnter the name of the VG u want to create:")

       while(x4 == 'y' or x4 == 'Y'):
         count = count + 1
         vg_d = vg_d  + " " + input( "Enter the PV{} u want to add:".format(count) )
         x4 = input("\nDo u want to add more PV's(y/n):")
         
       os.system( "vgcreate {} {}".format(vg_name,vg_d) ) 

   elif ch == '5':
       os.system('vgdisplay')
   
   elif ch == '6':
       x6 = 'y'
       vg_d = input("\nEnter the name of VG from which u want to create a LV:")
       lv_d = input("\nEnter the name of the LV:")
       size = input("\nEnter the size of the LV(+ve number):")
       unit = input("\nEnter the unit of storage(K, G, B):")
       fs_type = input("\nENter the type of format u want to do:")
       os.system( "lvcreate --size {}{} --name {} {}".format(size,unit,lv_d,vg_d  ) )
       os.system( "mkfs.{} /dev/{}/{}".format(fs_type,vg_d,lv_d) )

   elif ch == '7':
       os.system('lvdisplay')
       
   elif ch == '8':
       size = input("\nEnter the size by how much u want to increase with proper +ve and -ve sign:")
       unit = input("\nEnter the unit of storage(K, G, B):")
       lv_d = input("\nEnter the name of the LV:")
       vg_d = input("\nEnter the name of VG associated with LV provided above:")
       os.system( "lvextend --size {}{} /dev/{}/{}".format(size,unit,vg_d,lv_d) )
       os.system( "resize2fs /dev/{}/{}".format(vg_d,lv_d) )

   c = input("\nDo you want to continue(y/n):  ")
