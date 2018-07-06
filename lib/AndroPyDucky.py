# coding: utf-8
''' andropyducky '''

'''
	@Author: Daniel Victor Freire Feitosa
	@Version: 1.0.0

	Twitter: @DanielFreire00
	Github: github.com/proxyanon
	<danielfrerie56@hotmail.com>

'''

from sys import exit, argv
from os import path, popen
from platform import *

class AndroPyDucky():

	''' Informacoes do sistema '''
	sys = system()
	arch = machine()
	ver = version()

	''' Construtor '''
	def __init__(self, duckyfile='scripts/script.dd', output='output/payload.sh', banners=True):
		self.duckyfile = duckyfile
		self.output = output
		self.banners = banners

	def verifyadb(self):
		cmd_read = popen('adb devices').read().split("\n")[1]

		if "device" in cmd_read or "unauthorized" in cmd_read:
			return True
		else:
			return False

	def adbpush(self, path):
		if self.banners:
			print("\nTransferindo {output} para {path} ...".format(output=self.output, path=path))
		
		try:
			cmd = popen('adb push {output} {path}'.format(output=self.output, path=path))
		except:
			if self.banners:
				print("Erro ao transferir o arquivo ...")
			exit()

		if self.banners:
			print(cmd.read())

	''' Funcao que faz a primeira conversao do arquivo .dd para o formato andropyducky (ex: RDcmdED) '''
	def duck2andro(self):
		
		if self.banners:
			print("\n")
			print("██      ▄   ██▄   █▄▄▄▄ ████▄ █ ▄▄ ▀▄    ▄ ██▄     ▄   ▄█▄    █  █▀ ▀▄    ▄ ")
			print("█ █      █  █  █  █  ▄▀ █   █ █   █  █  █  █  █     █  █▀ ▀▄  █▄█     █  █  ")
			print("█▄▄█ ██   █ █   █ █▀▀▌  █   █ █▀▀▀    ▀█   █   █ █   █ █   ▀  █▀▄      ▀█   ")
			print("█  █ █ █  █ █  █  █  █  ▀████ █       █    █  █  █   █ █▄  ▄▀ █  █     █    ")
   			print("█ █  █ █ ███▀    █          █    ▄▀     ███▀  █▄ ▄█ ▀███▀    █    ▄▀     ")
  			print("█  █   ██        ▀            ▀                 ▀▀▀          ▀            ")
 			print("▀                                                                          \n")

        	print("[-] Twitter ....: @DanielFreire00")
        	print("[-] YouTube ....: ProxySec\n")

        	print("Operation system .......: {sys}".format(sys=self.sys))
        	print("System version  ........: {ver}".format(ver=self.ver))
        	print("Arch    ................: {arch}\n".format(arch=self.arch))

		array_andro = [{"GUI r": "R", "GUI x": "X", "GUI t": "T", "ENTER": "E", "DOWNARROW": "D", "UPARROW": "U", "DELAY": "L", "ALT TAB": "F"}] # array contendo as strings que serao convertidas
		try: # tenta abrir o arquivo ducky
			handle = open(self.duckyfile, 'r')
		except: # se nao conseguir sai do programa
			if self.banners:
				print("[x] I/O erro, arquivo nao encontrado: {duckyfile}".format(duckyfile=self.duckyfile))
			exit()

		content = "" # variavel que vai armazenar o conteudo convertido

		if self.banners:
			print("[#] Convertendo arquivo Ducky para o formato AndroPyDucky ...")

		for r in handle:

			row = r.strip() # linha do arquivo ducky

			if 'STRING ' in row: # se contiver STRING na linha ele vai fazer o replace
				content += row.strip('STRING ') # retira o STRING e deixa somente o que tem na linha
			else: # se nao
				try: # tenta substituir as strings do ducky por strings do andropyducky
					content += array_andro[0][row]
				except:
					pass

		handle.close() # fecha o arquivo ducky

		if self.banners:
			print("[#] Primeira conversao concluida com sucesso !\n")

		return content.replace(" ", "P") # retorna o conteudo convertido para o formato andropyducky


	''' Funcao que faz a conversao do andropyducky para o do hid-keyboard '''
	def andro2hid(self):
		conversion = self.duck2andro() # executa a funcao da primeira conversao
		array_andro = [{"R": "left-meta r", "X": "left-meta x", "F": "left-alt tab", "T": "left-ctrl left-alt t", "@": "left-shift 2", "&": "left-shift 7", "%": "left-shift 5", "(": "left-shift 9", ")": "left-shift 0", "*": "left-shift 8", "!": "left-shift 1", "#": "left-shift 3", '"': "left-shift tilde", "S": "", "E": "enter", "P": "space", "\r\n": "", "\n": "", "D": "down", "U": "up", "'": "tilde", ".": "stop", ",": "comma", ":": "left-shift slash", ";": "slash", ">": "left-shift period", "<": "left-shift comma", "-": "minus", "+": "kp-plus", "/": "right-alt q"}]
		content = ""

		if self.banners:
			print("[#] Convertendo AndroPyDucky para o formato do hid-keyboard ...")

		for x in range(0, len(conversion)):
				
			if conversion[x] == 'L':
				content += "ping -c 5 localhost > null\n" # essa string faz o delay de 6ms

			try: # tenta substituir a string do andropyducky pela do hid-keyboard
				content += "echo {conversion} | ./hid-keyboard /dev/hidg0 keyboard > null\n".format(conversion=array_andro[0][conversion[x]])
			except:
				if conversion[x] != 'L': # se a string for diferente do comando de delay
					content += "echo {conversion} | ./hid-keyboard /dev/hidg0 keyboard > null\n".format(conversion=conversion[x])

		if self.banners:
			print("[#] Segunda conversao concluida com sucesso !\n")

		if self.banners:
			print("[#] Criando payload ...")
		
		try: # vai tentar escrever o arquivo para o hid-keyboard
			handle = open(self.output, 'w')
			handle.write(content)
			handle.close()

			if self.banners:
				print("\nPayload criado com sucesso !")
				print("------------------------------------------")
				print("[+] Nome: {output}".format(output=self.output))
				print("[+] Caminho: {path}".format(path=path.abspath(self.output)))
				print("[+] Tamanho: {size} bytes".format(size=path.getsize(self.output)))
				print("------------------------------------------\n")

		except: # se nao conseguir abrir o arquivo ele sai do programa
			if self.banners:
				print("\n[x] I/O erro, Nao foi possivel criar o arquivo: {output}\n".format(output=self.output))
			exit()