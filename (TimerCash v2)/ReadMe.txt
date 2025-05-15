Per poter creare un file eseguibile dai file python 
usufruendo di Kivy e Kivymd bisogna seguire queste procedure

step 0: 

Se sei su Windows, scaricare un MAcchina virtuale (WSL) Inux o Ubuntu
per poter utilizzare al meglio tutte le librerie.

Step 1:

aprire il terminale di Linux o Ubuntu e inserire queste linee di comando:

    - sudo apt-get install git
    - git clone https://github.com/kivy/buildozer.git

    - sudo apt-get update
    - sudo apt update
    - sudo apt install cmake
    - sudo apt-get install openjdk-17-jdk
        dopo aver inserito questo codice digitare 0 e premere invoking
    - sudo update-alternatives --config java
    - sudo apt-get install unzip
    - sudo apt install python3 python3-pip ipython3
    - sudo apt install cython=0.29.19
    - sudo apt-get install autoconf
    - sudo apt install build-essential libltdl-dev libffi-dev libssl-dev python3-dev
    - sudo pip3 install --upgrade cython
    - sudo apt-get install zip
    - sudo apt install python3-dev


    - cd buildozer
    - sudo python3 setup.py install

Step 2:

una volta dentro la directory della app ( o presa da git clone o in locale)
eseguire il comando:

    - sudo buildozer init

creare il file buildozer.spec

Step 3:

Aprire il file buildozer.spec e modificare i parametri essenziali:

    - requirements = python3,kivy,pillow,kivymd
        per le librerie richieste
    - osx.kivy_version = 2.3.0
        versione kivy
    - android.logcat_filters = *:S python:D
    - p4a.branch = develop

    piu nome della app e nome del package

Step 4:

Una volta terminate le modifiche eseguire sempre da linea di comando:

    - sudo buildozer android debug

Farà partire un lungo processo nper creare il file apk

