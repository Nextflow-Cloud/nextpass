# Nextpass
### About

A secure, reliable, and fast way to store your passwords in a encrypted manner. Provides top notch security for your credentials.
* AES-256 CBC security for database encryption
* Scrypt for key derivation
* Bcrypt for secure hashing
* Syncs encrypted backups with a server to keep backups synced securely which can be found [here](https://github.com/Nextflow-Cloud/sso-system) 

### Build the program
```shell
pyinstaller main.py --onefile --file=favicon.ico
```

* Enjoy the password manager :)

### Contribute
Nextflow Cloud Technologies is committed to open-source software and free use. This means that you are free to view, modify, contribute, and support the project. Making a pull request with something useful is highly encouraged as this project is made possible by contributors like you who support the project.

* prod: Most stable branch -- used in production. 
* main: Beta/release preview -- mostly stable and likely will be pushed to production with a couple fixes.
* dev: Active development -- expect a variety of unstable and/or unfinished features and fixes.
