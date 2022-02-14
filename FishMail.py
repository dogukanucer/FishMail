import itertools
import os

# TO DO:
# =====

# 1- threading
# 2- mail validations
# 3- adding most used mail patterns
# 4- [✓] writing output to a file in current directory
# 5- [OPTIONAL] argpass -> -d <domain_name>

def clear_screen():
	if 'Linux' in os.uname():
		os.system("clear")
	else:
		os.system("cls")

def print_banner():
	banner = """\
\033[1;31m
  _____.__       .__                   .__.__   
_/ ____\__| _____|  |__   _____ _____  |__|  |  
\   __\|  |/  ___/  |  \ /     \\\__  \ |  |  |  
 |  |  |  |\___ \|   Y  \  Y Y  \/ __ \|  |  |__
 |__|  |__/____  >___|  /__|_|  (____  /__|____/
               \/     \/      \/     \/         
\033[1;31m================================================\033[0;0m
"""
	print(banner)

def main():
	
	clear_screen()
	print_banner()

	info = """\
\033[1;34m[*]\033[0;0m Please enter credentials space seperated.

\033[1;34m[*]\033[0;0m Example: \033[1;33m>\033[1;32m david guetta 1966\033[0;0m 
"""
	print(info)

	cred_string = input("\033[1;33m >\033[1;32m ")
	
	fix_fonts = '\033[0;0m'
	# Turn fonts back to default color and style
	
	creds = cred_string.split()
	if len(creds) < 2:
		print("\n\033[1;31m[!]\033[0;0m At least 2 entries should be entered.")
		exit()

	answer = input("\n\033[1;34m[*]\033[0;0m Do you want to use specific domain ? (yes/no) > ")

	domains = ['gmail','yahoo','hotmail']
	patterns = ['%s.%s@%s.com','%s%s@%s.com']
	# filler.filler@domain.tld fillerfiller@domain.tld ...

	perm_creds = list(itertools.permutations(creds, r=2)) 
	# returns all permuatations of credentials in 2 elements tuple form
	# input: [1, 2, 3]
	# output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

	if answer.lower() == 'no':

		print("\n\033[1;32m[+]\033[0;0m Potential emails have been created: \n")

		for domain in domains:
			for pattern in patterns:
				for perm_cred in perm_creds:

					email = pattern % (perm_cred[0], perm_cred[1], domain)
					print(email)
					with open('mails.txt','a') as file:
						file.write(email+'\n')
	elif answer.lower() == 'yes':

		print("\n\033[1;34m[*]\033[0;0m Please enter domains space seperated.")
		specific_domain = input("\n\033[1;33m >\033[1;32m ")
		fix_fonts = '\033[0;0m'
		specific_domains = specific_domain.split()

		print("\n\033[1;32m[+]\033[0;0m Potential emails have been created: \n")

		for domain in specific_domains:
			for pattern in patterns:
				for perm_cred in perm_creds:

					email = pattern % (perm_cred[0], perm_cred[1], domain)
					print(email)
					with open('mails.txt','a') as file:
						file.write(email+'\n')
	
	print("\n\033[1;32m[+]\033[0;0m \033[0;1mmails.txt\033[0;0m has been created in current directory. \n")

try:
	main()
except KeyboardInterrupt:
	print("\n\033[1;31m[!]\033[0;0m Operation canceled.")
