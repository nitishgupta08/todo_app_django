# todo_app_django
Todo app made with Django and DRF. Users can perform CRUD on todo via templates or apis

### This repo is for me to implement anything new I learn in Django :)

## Setup
<ul>
<li>Clone the repository</li>
<li>Create a virtual environment by using <code>virtualenv</code></li>
<li>Install required packages by running <code>pip install -r requirements.txt</code></li>
<li>Generate Django secret key and store it in <code>.env</code> file</li>
<li>Start a MySQL server copy db name, username, password in <code>.env</code> file</li>
<li>Delete <code>migrations</code> folder from <code>todo</code> app</li>
<li>execute <code>python manage.py makemigrations</code></li>
<li>execute <code>python manage.py migrate</code></li>
<li>execute <code>python manage.py runserver</code></li>
<li>Your development server is now running on <code>http://127.0.0.1:8000</code></li>
</ul>

