# Ensembl Technical Test - Python

Before you run the application, please make sure you have installed following tools, you should have rights to install packages & run docker containers
#### Prerequisites
```
1. Git [version 2.30.0 OR Higher]
2. Python 3.9 OR Higher
3. Docker (In case running as docker. Tested on Docker version 20.10.5, build 55c4c88)
```

#### Notes
* Search is case-insensitive. Any combination of cases(lower/upper) can be used for search.
* In test document, expected endpoint has been mentioned as ***/gene_suggest***, but as per REST standards
same has been changed to ***/gene-suggestions***.
* Some test cases have been written to demonstrate how unit/integration testing can be done. I tried to use in-memory database. 
  End-to-end automated testing is described in the testing document.
* Added Docker support for the application; Dockerfile is included.  
* Error handling has been done in the application. Errors like BAD_REQUEST, NOT_FOUND & INTERNAL_SERVER_ERROR are handled.
  You can produce these errors by removing query parameters or keeping empty values.

#### Clone the project from GitHub
   ```
   git clone https://github.com/shimpiashutosh/ensembl-technical-test-python.git
   ```
#### Navigate to project's root folder before following the steps e.g.
   ```
   cd ensembl-technical-test-python
   ```
#### How to run test cases?
   Before running test cases, please install required packages using setup.py OR requirements.txt as mentioned in the steps, 
   running application without docker container
   ```
   python3 -m unittest discover uk.ac.ebi.ensembl.search.gene.tests
   ```

#### Following are the steps in order to run the application as Docker container
1. Build the Docker image.
   ```
   docker build -t ensembl-technical-test-python:1.0.0 .
   ```
2. Run the Docker image.
   ```
   docker run --rm -d --name ensembl-technical-test-python -p 5002:5002 ensembl-technical-test-python:1.0.0
   ```
3. Test the application using following link with the help of browser or postman or any suitable tool.
   
   SUCCESS
   ```
   http://127.0.0.1:5002/gene-suggestions?query=BRC&species=homo_sapiens&limit=4
   ```
   BAD_REQUEST
   ```
   http://127.0.0.1:5002/gene-suggestions?query=BRC&species=homo_sapiens&limit=four
   ```
   NOT_FOUND
   ```
   http://127.0.0.1:5002/gene-suggestions?query=1234&species=homo_sapiens&limit=2
   ```
   *Change url query parameters as needed.
4. Stop the container
   
   List running containers
   ```
   docker ps
   ```
   Select CONTAINER ID & pass to following command to stop the container
   ```
   docker stop {CONTAINER ID}
   
---------------- OR ----------------

#### Following are the steps in order to run the application without docker container 
1. Install python dependencies [If **python3** won't work then try to use **python**]
   ```
   python3 setup.py install
   
   OR
   
   python3 -m pip install -r requirements.txt
   ```
2. Run the application
   ```
   python3 -m uk.ac.ebi.ensembl.search.gene.app.search_gene
   ```
3. Test the application using following link with the help of browser or postman or any suitable tool.

   SUCCESS
   ```
   http://127.0.0.1:5002/gene-suggestions?query=BRC&species=homo_sapiens&limit=4
   ```
   BAD_REQUEST
   ```
   http://127.0.0.1:5002/gene-suggestions?query=BRC&species=homo_sapiens&limit=four
   ```
   NOT_FOUND
   ```
   http://127.0.0.1:5002/gene-suggestions?query=1234&species=homo_sapiens&limit=2
   ```
   *Change url query parameters as needed.
4. Stop the Application
   ```
   CTRL+C
   ```
