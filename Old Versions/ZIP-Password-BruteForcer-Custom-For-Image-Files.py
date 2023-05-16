from PIL import Image



import os
def cls():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])

banner = '\n ###################################\n'
banner += ' # ZIP Password BruteForcer        #\n'
banner += ' ###################################\n'
banner += ' # Coded By Sir.4m1R               #\n'
banner += ' # The404Hacking                   #\n'
banner += ' # Digital Security ReSearch Group #\n'
banner += ' # T.me/The404Hacking              #\n'
banner += ' ###################################\n'
banner += ' GitHub:\n'
banner += ' https://github.com/The404Hacking/ZIP-Password-BruteForcer\n\n'
banner += ' [1] Zip Password Cracker\n'
banner += ' [0] Exit\n'
print banner

a=1
if a==0:
 import os
 print " [!] Good Bye :)"
 quit()
elif a==1:
 #!/usr/bin/python

 import zipfile
 import os
 from time import time
 

 textzippass = '''
 #########################################
 # Zip Password Brute Forcer (Top Speed) #
 #########################################
 # The404Hacking                         #
 # Digital Security ReSearch Group       #
 # T.me/The404Hacking                    #
 #########################################
 '''
 print textzippass
 file_path = "flag.zip"
 print ""
 word_list = "rockyou.txt"
 def main(file_path, word_list):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print " [!] Please check the file's Path. It doesn't seem to be a ZIP file."
		quit()

	password = None 
	i = 0 
	c_t = time()
	with open(word_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				print("Trying: " + password)
				zip_.extractall(pwd=password)
				t_t = time() - c_t 
				with Image.open("flag.jpg") as im:
					im.verify()
					if img.format == 'JPEG':
						print('JPEG image')
					else:
						break
				print "\n [*] Password Found :)\n" + " [*] Password: "+password+"\n" 
				print " [***] Took %f seconds to Srack the Password. That is, %i attempts per second." % (t_t,i/t_t)
				quit()
			except Exception:
				pass
		print " [X] Sorry, Password Not Found :("
		quit()
 main(file_path, word_list)

try:
	with Image.open("flag.jpg") as im:
		im.verify()
		if img.format == 'JPEG':
			print('JPEG image')
		else:
			print('Invalid image type')
except Exception:
	print('Invalid image')