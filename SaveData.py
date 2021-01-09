import json

data={}
data['libros'] = []
data2={}
data2['enlaces'] =[]
data3={}
data3['texto'] =[]

def IsNumber(pagSearch):
    return pagSearch <100000

def saveBook(text):

    link = text[1].split("//", 1)
    splitSlashLink = link[1].split("/")
    pagSearch=splitSlashLink[2].split("-")
    for i in pagSearch:
        if i.isnumeric():
            res = i
        else : res = 0
    with open('Libros.json','r') as infile:
        data = json.load(infile)

    data['libros'].append({
     'name' : splitSlashLink[1],
     'page': str(res),
     'url': text[1]
    })

    with open('Libros.json','w') as outfile:
        json.dump(data,outfile)

def saveLink(text):

    link = text[1].split("//", 1)
    webpageName=link[1].split("/")
    data2['enlaces'].append({
        'web':webpageName[0],
        'url':text[1]
    })
    with open('Enlaces.json','w') as outfile:
        json.dump(data2,outfile)

def saveText(text):
    data3['texto'].append({
        'texto':text[1]
    })
    with open('Texto.json','w') as outfile:
        json.dump(data3,outfile)