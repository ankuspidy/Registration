# Registration
Registration and login page<br />
Follow the below steps to get started with the project<br />

On the terminal<br />

1). write "git clone https://github.com/ankuspidy/Registration.git".<br />
2). Activate the virtual environment.<br />
3). python3 -m pip -r requirements.txt<br />
4). python3 manage.py migrate<br />
5). python3 manage.py runserver<br />

After the server run successfully, paste "http://127.0.0.1:8000/signup/" in the url bar and get yourself registered.<br /><br />


You can also configure your mail settings by changing the host_user and host_password by following steps.<br />
1). Create a new dummy account on the gmail.<br />
2). Go to https://myaccount.google.com/lesssecureapps and toggle on 'Allow less secure apps' option.(Note that this is just for testing purpose)<br />
3). Go to project 'settings.py'<br />
4). Change the EMAIL_HOST_USER <b> and </b> EMAIL_HOST_PASSWORD to your respective dummy account's user and password.<br />

<h2>All set your are ready to go.</h2>




