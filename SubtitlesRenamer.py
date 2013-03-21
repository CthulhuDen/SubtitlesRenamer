from os import *
import string,re

print "Welcome user!\nYou may choose some options below but beware!\nAll changes are irreversible so take care!"

def checkOnZero(a,n):
	if a=='':
		a=([r'(\d+).(\d+)','.avi','.srt'])[n]
	return a
		
a=[r"Now enter media file pattern (empty for '(\d+).(\d+)'): ",
r"Media file extension (empty for '.avi'): ",
r"Now enter sub file pattern (empty for '(\d+).(\d+)'):",
r"Sub file extension (empty for '.srt'): "]

med=re.compile(checkOnZero(raw_input(a[0]),0))
med_ext=checkOnZero(raw_input(a[1]),1)
sub=re.compile(checkOnZero(raw_input(a[2]),0))
sub_ext=checkOnZero(raw_input(a[3]),2)
rec=raw_input("Is underdirectories processing needed?(y/n): ")
c=-1

def processdir(wdir):
	global c
	files=listdir(wdir)
	for file in files:
		fullname=path.join(wdir,file)
		if path.isdir(fullname) and (rec=="y"):
			processdir(fullname)
		if path.isfile(fullname) and (file[(-1)*len(med_ext):]==med_ext):
			tmp=med.search(file)
			if tmp:
				med_pure=()
				for i in tmp.groups():
					med_pure=med_pure+(int(i),)
				for file1 in files:
					fullname1=path.join(wdir,file1)
					if path.isfile(fullname1) and (file1[(-1)*len(sub_ext):]==sub_ext):
						tmp=sub.search(file1)
						if tmp:
							sub_pure=()
							for i in tmp.groups():
								sub_pure=sub_pure+(int(i),)
							if med_pure==sub_pure:
								print fullname1," -> ",path.join(wdir,file.replace(med_ext,sub_ext))
								if not path.isfile(path.join(wdir,file.replace(med_ext,sub_ext))):
									rename(fullname1,path.join(wdir,file.replace(med_ext,sub_ext)))
									c=c+1
									print ""
								else:
									print("Not copied, file exists.\n")
if not raw_input("Ok, now it is your very last chance to enter \"cancel\"\n").lower()=="cancel":
	c=0
	processdir(curdir)
	
if c>=0:
	print c,"files were processed."
	
print "Cthulhu 2011-2013"
system("pause")
