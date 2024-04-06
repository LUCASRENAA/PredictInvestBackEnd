# PredictInvest-BackEnd





# Comandos utilizados para a criação do projeto

```
django-admin startproject PredictInvestBackEnd .
django-admin startapp BackEnd   
```

# Primeiro acesso
```
git clone https://github.com/LUCASRENAA/PredictInvestBackEnd.git
cd PredictInvestBackEnd
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
pip3 install -r requeriments.txt
python3 manage.py migrate
python3 manage.py createsuperuser 
python3 manage.py runserver
```



# Configurações

Não esqueça de adicionar a secret na opção de "settings" do projeto