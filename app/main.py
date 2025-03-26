from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["biblio"]
livres_collection = db["livres"]

@app.get("/")
def read_root():
    return {"message": "Backend FastAPI prêt !"}

# Endpoint pour récupérer les livres en prêt
@app.get("/prets")
def get_prets():
    livres = list(livres_collection.find({}, {"_id": 0}))
    return {"livres": livres}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
