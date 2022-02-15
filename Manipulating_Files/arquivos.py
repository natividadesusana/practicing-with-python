import json

"""""
with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + ' | ' + str(dados))
"""""

dicionario = {
  "CHAVINHO": ["CHAVES", "15/02/2022", "RECEP_01"],
  "QUICO": ["QUICO FLORES", "14/02/2022", "RAIOX_01"],
  "FLORINDA": ["DONA FLORINDA", "02/01/2022", "RECEP_03"],
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)