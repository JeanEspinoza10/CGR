import requests
import json

class Categories:
    
    def __init__(self):
        
          
        self.url_base = 'https://celsoalexdiaz.proactivanet.com/panet/api/Categories'

        # Colocar la key como variable de entorno
        self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqZWFuLmVzcGlub3phQHNvbHV0aW9udGVjaC5jb20ucGUiLCJvdnIiOiJmYWxzZSIsImF1dCI6IjAiLCJuYmYiOjE3MTcwNDU2ODMsImV4cCI6MTc0ODU4MTY4MywiaWF0IjoxNzE3MDQ1NjgzLCJpc3MiOiJwcm9hY3RpdmFuZXQiLCJhdWQiOiJhcGkifQ.QAUcqs1DJjBcQW59diOINBWvndnZob3-KS-2t2F9ahA',
                'Accept-Language': 'es'
            }


        
    def checked(self, valor, id_fhater):
        try:
            params = {
                "Name":valor,
                "PadCategories_id":id_fhater,
                '$fields': 'Name,Path,Sort'
            }

            response = requests.get(url=self.url_base,headers=self.headers,params=params)
            
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            raise ValueError(e)

    def addCategorie(self, nameCategorie, id_categorie_father):
        try:
            data = {
                "Name": f"{nameCategorie}",
                "Description": "api",
                "Sort": None,
                "PadCategories_id": f"{id_categorie_father}",
                "AppliesToIncidents": True,
                "AppliesToProblems": True,
                "AppliesToRFCs": True,
                "AppliesToKB": True,
                "Inactive": False
            }

            
            result = self.checked(valor = nameCategorie, id_fhater = id_categorie_father)
            
            if(result):
                return {
                    "status_code": 200,
                    "message": "categorie exists"
                }
            else:
                response = requests.post(url=self.url_base, headers=self.headers, data=json.dumps(data))
                if response.status_code == 200 or response.status_code == 201:
                    return {
                        "status_code": 200,
                        "message": "categorie add"
                        }
                else:
                    return {
                        "status_code": response.status_code,
                        "message": response.content
                    
                    }


        except Exception as e:
            raise ValueError(e)
        