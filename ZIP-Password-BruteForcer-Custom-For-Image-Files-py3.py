# Importing Modules
from PIL import Image
import os

# Clearing Screen Function
def cls():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])

# Banner
banner = """
 ###################################
 # ZIP Password BruteForcer        #
 ###################################
 [1] Zip Password Cracker
 [0] Exit\n"""

print(banner)

# Skip user input and set a=1 to run script
runScript=1
if runScript==0:
	print(" [!] Good Bye :)")
	quit()
elif runScript==1:
	# Importing Additional Modules
	import zipfile
	from time import time
 
	textzippass = """
	#########################################
	# Zip Password Brute Forcer (Top Speed) #
	"""
	print(textzippass, end="\n\n")
	
	filePath = "flag.zip"
	wordList = "rockyou.txt"

	# Main Function
	def main(filePath, wordList):
		try:
			zipFile = zipfile.ZipFile(filePath)
		except zipfile.BadZipfile:
			print(" [!] Please check the file's Path. It doesn't seem to be a ZIP file.")
			quit()

		password = None 
		i = 0 
		currentTime = time()
		with open(wordList, "r") as wordListFile: 
			words = wordListFile.readlines() 
			for word in words:
				i += 1
				password = word.split("\n")[0]
				try:
					print("Trying: " + password)
					zipFile.extractall(pwd=password)
					timeTaken = time() - currentTime 
					with Image.open("flag.jpg") as imageFile:
						imageFile.verify()
						if imageFile.format == 'JPEG':
							print('JPEG image')
						else:
							break
					print("\n [*] Password Found :)\n" + " [*] Password: "+password+"\n")
					print(" [***] Took %f seconds to Crack the Password. That is, %i attempts per second." % (timeTaken,i/timeTaken))
					quit()
				except Exception:
					pass
			print(" [X] Sorry, Password Not Found :(")
			quit()
	main(filePath, wordList)

try:
	with Image.open("flag.jpg") as imageFile:
		imageFile.verify()
		if imageFile.format == 'JPEG':
			print('JPEG image')
		else:
			print('Invalid image type')
except Exception:
	print('Invalid image')