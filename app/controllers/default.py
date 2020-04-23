from flask import render_template, jsonify, request, json
import requests
from operator import itemgetter
from app import app
import urllib

def allInfo():

  PEOPLE_URL = 'https://swapi.dev/api/people'
 
  def getUrlNextPage(page):
    return page['next']

  def getPeoplePerPage(page):
    return [people for people in page['results']]
  
  def getPage(pageUrl=None):
    if pageUrl is None:
        pageUrl = PEOPLE_URL

    response = requests.get(pageUrl)
    return response.json() if response.status_code == 200 else None

  peoples = []
  startPage = getPage()
  pagePeople = getPeoplePerPage(startPage)
  peoples.extend(pagePeople)
  nextPage = getUrlNextPage(startPage)

  while True:
        page = getPage(nextPage)
        if page is None:
          print('Error: ', nextPage)
        elif page['next']:
          nextPage = getUrlNextPage(page)
          pagePeople = getPeoplePerPage(page)
          peoples.extend(pagePeople)
        else:
          pagePeople = getPeoplePerPage(page)
          peoples.extend(pagePeople)
          break

  return peoples

def allStarships():

  STARSHIPS_URL = 'https://swapi.dev/api/starships'

  def getUrlNextPage(page):
    return page['next']

  def getStarshipsPerPage(page):
    return [starships for starships in page['results']]
  
  def getPage(page_url=None):
    if page_url is None:
        page_url = STARSHIPS_URL

    response = requests.get(page_url)
    return response.json() if response.status_code == 200 else None

  starships = []
  startPage = getPage()
  pageStarships = getStarshipsPerPage(startPage)
  starships.extend(pageStarships)
  nextPage = getUrlNextPage(startPage)

  while True:
        page = getPage(nextPage)
        if page is None:
            print('Error: ', nextPage)
        elif page['next']:
            nextPage = getUrlNextPage(page)
            pageStarships = getStarshipsPerPage(page)
            starships.extend(pageStarships)
        else:
            pageStarships = getStarshipsPerPage(page)
            starships.extend(pageStarships)
            break

  return starships

@app.route('/', methods=['GET'])
def index():

  peoples = allInfo()
  return render_template('index.html', peoples=peoples)

@app.route('/findfilm/<string:name>', methods=['GET'])
def filmsByName(name):

  peoples = allInfo()

  cont = 0
  result = []

  while cont < len(peoples):
    if peoples[cont]['name'] == name:
      result = peoples[cont]
      cont = len(peoples)
    else:
      cont = cont + 1

  filmsDict = result.get("films")
  contFilm = 0
  resultListFilms = []
  filmsTitles = []

  while contFilm < len(filmsDict):
    responseFilm = requests.get(filmsDict[contFilm])
    filmsJson = responseFilm.json()
    resultListFilms.append(filmsJson)
    filmsTitles.append(resultListFilms[contFilm]['title'])
    contFilm = contFilm + 1

  return render_template('films.html', name=name, films=filmsTitles)

@app.route('/findstarships/<string:name>', methods=['GET'])
def starshipsByName(name):

  peoples = allInfo()

  # pegar dados do ator
  cont = 0
  result = []

  while cont < len(peoples):
    if peoples[cont]['name'] == name:
      result = peoples[cont]
      cont = len(peoples)
    else:
      cont = cont + 1

  # lógica para pegar filmes do ator com base no objeto já salvo
  starshipsDict = result.get("starships")
  contStarships = 0
  resultListStarships = []
  starshipsTitles = []

  while contStarships < len(starshipsDict):
    responseStarships = requests.get(starshipsDict[contStarships])
    starshipsJson = responseStarships.json()
    resultListStarships.append(starshipsJson)
    starshipsTitles.append(resultListStarships[contStarships]['name'])
    contStarships = contStarships + 1

  print(starshipsTitles)

  return render_template('starships.html', name=name, starships=starshipsTitles)

@app.route('/findvehicles/<string:name>', methods=['GET'])
def vehiclesByName(name):

  peoples = allInfo()

  cont = 0
  result = []

  while cont < len(peoples):
    if peoples[cont]['name'] == name:
      result = peoples[cont]
      cont = len(peoples)
    else:
      cont = cont + 1

  # lógica para pegar filmes do ator com base no objeto já salvo
  vehiclesDict = result.get("vehicles")
  contVehicles = 0
  resultListVehicles = []
  vehiclesTitles = []

  while contVehicles < len(vehiclesDict):
    responseVehicles = requests.get(vehiclesDict[contVehicles])
    vehiclesJson = responseVehicles.json()
    resultListVehicles.append(vehiclesJson)
    vehiclesTitles.append(resultListVehicles[contVehicles]['name'])
    contVehicles = contVehicles + 1

  return render_template('vehicles.html', name=name, vehicles=vehiclesTitles)

@app.route('/findhomeworld/<string:name>', methods=['GET'])
def homeworldByName(name):

  peoples = allInfo()

  cont = 0
  result = []

  while cont < len(peoples):
    if peoples[cont]['name'] == name:
      result = peoples[cont]
      cont = len(peoples)
    else:
      cont = cont + 1

  # lógica para pegar planetas do ator com base no objeto já salvo
  homeworldDict = result.get("homeworld")
  responseHomeworld = requests.get(homeworldDict)
  homeworldJson = responseHomeworld.json()

  return render_template('homeworld.html', name=name, homeworld=homeworldJson)

@app.route("/rankingstarships", methods=['GET'])
def rankingStarships():

  response = requests.get('https://swapi.dev/api/starships/')
  dictResponse = response.json()
  dictList = dictResponse.get("results")

  listStarships = allStarships()
  listStarshipsScore = {}

  cont = 0
  score = 0

  while cont < len(listStarships):

    # name   
    name = listStarships[cont]['name']

    # hyperdrive_rating
    hyperdrive_rating = listStarships[cont]['hyperdrive_rating']

    if hyperdrive_rating == "unknown":
      hyperdriveRating = "unknown"
    else:
      hyperdriveRating = float(hyperdrive_rating)
    

    # cost_in_credits
    cost_in_credits = listStarships[cont]['cost_in_credits']
    
    if cost_in_credits == "unknown":
      costInCredits = "unknown"
    else:  
      costInCredits = float(cost_in_credits)
    

    # criando estrutura pra nomes e score
    if type(hyperdriveRating) and type(costInCredits) == float:
      score = hyperdriveRating / costInCredits
    else:
      score = "unknown"

    listStarshipsScore[cont] = {
      "name": name,
      "score": score
    }

    cont = cont + 1

  # convertendo dict em list
  contScore = 0
  resultListScore = []

  while contScore < len(listStarshipsScore):
    responseScore = listStarshipsScore[contScore]
    resultListScore.append(responseScore)
    contScore = contScore + 1

  # substituindo onde for a string unknow por 0 pra fazer ordenamento
  contUnsorted = 0
  unsortedListScore = resultListScore

  while contUnsorted < len(unsortedListScore):
    if type(unsortedListScore[contUnsorted]['score']) == str:
       unsortedListScore[contUnsorted]['score'] = 0
    contUnsorted = contUnsorted + 1

  # ordenando do maior pro menor
  starships_ordered = sorted(unsortedListScore, key=lambda k: k['score'], reverse=True) 
  
  # invertendo o 0 para a string unknow na lista ordenada
  contSorted = 0
  sortedListStarScore = starships_ordered

  while contSorted < len(sortedListStarScore):
    if sortedListStarScore[contSorted]['score'] == 0:
       sortedListStarScore[contSorted]['score'] = "unknown"
    contSorted = contSorted + 1
  
  return render_template('rankingstarships.html', data=sortedListStarScore)