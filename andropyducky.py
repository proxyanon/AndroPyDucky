''' andropyducky '''

'''
	@Author: Daniel Victor Freire Feitosa
	@Version: 1.0.0

	Twitter: @DanielFreire00
	Github: github.com/proxyanon
	<danielfrerie56@hotmail.com>
	
'''

from lib.AndroPyDucky import *

index = 1

help_banner  = "\n"
help_banner += ("██      ▄   ██▄   █▄▄▄▄ ████▄ █ ▄▄ ▀▄    ▄ ██▄     ▄   ▄█▄    █  █▀ ▀▄    ▄ \n")
help_banner += ("█ █      █  █  █  █  ▄▀ █   █ █   █  █  █  █  █     █  █▀ ▀▄  █▄█     █  █  \n")
help_banner += ("█▄▄█ ██   █ █   █ █▀▀▌  █   █ █▀▀▀    ▀█   █   █ █   █ █   ▀  █▀▄      ▀█   \n")
help_banner += ("█  █ █ █  █ █  █  █  █  ▀████ █       █    █  █  █   █ █▄  ▄▀ █  █     █    \n")
help_banner += ("█ █  █ █ ███▀    █          █    ▄▀     ███▀  █▄ ▄█ ▀███▀    █    ▄▀     \n")
help_banner += ("█  █   ██        ▀            ▀                 ▀▀▀          ▀            \n")
help_banner += ("▀                                                                          \n\n")

help_banner += ("Uso: python {scriptname} --duckyfile script.dd --output payload.sh\n".format(scriptname=argv[0].split("\\")[len(argv[0].split("\\"))-1]))
help_banner += ("Opcoes:\n")
help_banner += (" -d, -D, --duckyfile   Arquivo ducky para ser convertido\n")
help_banner += (" -o, -O, --output      Arquivo que de saida da conversao\n\n")


for arg in argv:
	
	if arg == "--duckyfile" or arg == "-d" or arg == "-D":
		duckyfile = argv[index+1]
		index += 2
	elif arg == "--output" or arg == "-o" or arg == "-O":
		output = argv[index+1]
		index += 2
	elif arg == "--help" or arg == "-h" or arg == "-H":
		print help_banner
		exit()

try:
	andropyducky = AndroPyDucky(duckyfile, output)
	andropyducky.andro2hid()

	if andropyducky.verifyadb():
		if andropyducky.banners:
			print("\n[$] ADB detectado ...")
		quiz = raw_input("Voce quer transferir o payload para seu aparelho [S/N] ? ")
		if quiz == 'S' or quiz == 's' or quiz == '':
			path = raw_input("Coloque a pasta onde o hid-keyboard (ex => /data/local/tmp): ")
			if path != '' and len(path) > 0:
				andropyducky.adbpush(path)
			else:
				if andropyducky.banners:
					print("Nenhum path indicado ...")
				exit()
		else:
			exit()

except:
	print("python {scriptname} --help\n".format(scriptname=argv[0].split("\\")[len(argv[0].split("\\"))-1]))
	exit()