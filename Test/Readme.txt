Le programme si divise en:

- main.py: la classe qui fait l´interaction avec l'utilisateur 

- ClassLibrary: répertoire contenant des classes d'affaire

- ClassLibrary\Department.py: classe qui représente un departement. Les logiques de moyenne, min, max se trouve ici.
C'est dans cette classe aussi que l'on contrôle que l'on ne peut pas ajouter un employé à un département inexistant

- ClassLibrary\Employee.py: classe qui représente un employé. 
La logique des noms vides et salaire positive se trouvent dans cette classe


==========
Pour exécuter:

$ tar -xzvf sources.tar.gz
$ python main.py

=====
Les tests se trouvent dans le fichier outputTests.tar.gz
Pour l'ouvrir:
$ tar -xzvf outputTests.tar.gz

NOTE: Dans Windows, winzip se dit capable d'ouvrir des fichiers tar (http://www.winzip.com/win/en/tar-file.html)