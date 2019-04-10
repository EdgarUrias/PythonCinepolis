import requests 
import json
import SMS

# url del Ajax
URL = "https://www.cinepolis.com/Cartelera.aspx/GetNowPlayingByCity"

# Define la ciudad a buscar
PARAMS = {'claveCiudad':'hermosillo', 'esVIP': 'true'} 
headers = {'content-type': 'application/json'}
f = open("jsonAvengers.txt", "w") #si se quiere guardar la respuesta en un archivo
# Envia un POST request al portal del ajax y regresa una respuesta en JSON
r = requests.post(url = URL, data=json.dumps(PARAMS), headers=headers) 

json1 = r.json()
fechas = [ "27 abril"] #Fecha a buscar
fecha = [] #lista de respuestas de fechas
respuesta = "" #variable para envio de informacion por mail
cine = ""
pelicula = ""
formato = "SUB" #formato a buscar SUB, 3D SUB, etc
horas = []
NoHoras = ["65057","65058","65060","65061","65079","65080","65081"] #excluir horas

#Busca el Cine seleccionado
for x in range(len(json1["d"]["Cinemas"])):
	if json1["d"]["Cinemas"][x]["Key"] == "cinepolis-vip-galerias-mall-hermosillo": 
 		cine = x

if cine == "" :
	 quit()

#Busca las fechas a Buscar
for y in range(len(json1["d"]["Cinemas"][cine]["Dates"])):
	if json1["d"]["Cinemas"][cine]["Dates"][y]["ShowtimeDate"] in fechas:  
		fecha.append(y)

if fecha == []:
	quit()

#Busca las peliculas
for a in range(len(fechas)): 
	respuesta = respuesta + json.dumps(json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["ShowtimeDate"]) + "\n"
	for z in range(len(json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"])):
		if json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][z]["Id"] == 31133:
			pelicula = z 
			if pelicula == "": 
				quit()
			respuesta = respuesta + json.dumps(json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][pelicula]["OriginalTitle"]) + "\n"
			for c in range(len(json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][pelicula]["Formats"])):
				if json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][pelicula]["Formats"][c]["Name"] == formato:
					formato = c
					for b in range(len(json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][pelicula]["Formats"][formato]["Showtimes"])):
						if json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][pelicula]["Formats"][formato]["Showtimes"][b]["ShowtimeId"] not in NoHoras: 
						 	horas.append(b) 
						 	respuesta = respuesta + "	Hora: " + json.dumps(json1["d"]["Cinemas"][cine]["Dates"][fecha[a]]["Movies"][pelicula]["Formats"][formato]["Showtimes"][b]["ShowtimeAMPM"]) + "\n" 


if horas == []: 
	quit()


f.close
#pruebas en JSON

some_text = respuesta

f.write(some_text) #guarda en archivo

#SMS.send(some_text)
