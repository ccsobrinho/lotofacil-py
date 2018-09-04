results = {}

def loadfile(results):
	print('loading file lotofacil-resultados.txt')
	try:
		with open('lotofacil-resultados.txt','r') as f:
			for fline in f:
				concurso = int(fline.split('-')[0].strip())
				dezenas = list(fline.split('-')[1].strip().split(','))
				results[concurso] = dezenas
	except:
		print('Erro ao carregar resultados')
		raise
	else:
		print('loadfile done!')

def get_concurso():
	while True:
		try:
			conc = int(input('Digite numero do concurso ou 0 para sair: '))
		except ValueError:
			print('Numero invalido!')
		else:
			break
	
	return conc


def main():
	loadfile(results)
	concurso = get_concurso()
	print(results[concurso])

if __name__ == '__main__':
    main()


