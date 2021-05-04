FROM python:3.9

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["python3","-m", "uk.ac.ebi.ensembl.search.gene.app.search_gene"]
