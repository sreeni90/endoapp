## Endo Procedure Data App


### API Endpoints

#### Procedure

* **/api/procedure/** (Procedure list endpoint)
* **/api/procedure/{procedure-id}/** (Procedure retrieve endpoint)

### Install 

    pip3 install -r requirements.txt

### Usage

   ./manage.py makemigrations
   ./manage.py migrate 
   ./manage.py runserver

### Testing

    Create user token and test using any REST client or using curl

    curl -X GET http://127.0.0.1:8000/api/procedure/{procedure_id} -H 'Authorization: Token {token generated in admin site}'

    

