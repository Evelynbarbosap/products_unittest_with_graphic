O intuito do repositório é por em prática clean code, validações com pydantic, teste unitário e gráficos gerados na lib Plotly do python com FastApi. 

Para rodar o reposítório é preciso rodar:
1) python3 -m venv env
2) source ./env/Scripts/activate
3) pip3 install -r requirements.txt
4) uvicorn main:app --reload

Para rodar o gráfico é preciso rodar:
1) python graphic.py

Para rodar o teste unitário é preciso rodar:
1) python unittest.py
