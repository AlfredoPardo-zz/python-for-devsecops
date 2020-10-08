from sqlalchemy import create_engine, Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
import json; import os

postgres_username=os.environ['POSTGRES_USERNAME']
postgres_password=os.environ['POSTGRES_PASSWORD']
postgres_host=os.environ['POSTGRES_HOST']
postgres_database=os.environ['POSTGRES_DATABASE']

db_string = 'postgresql+psycopg2://{}:{}@{}/{}'.\
        format(postgres_username, 
        postgres_password, 
        postgres_host,
        postgres_database)

db = create_engine(db_string)  
base = declarative_base()

class Docker_Image_Static_Analysis(base):
    __tablename__ = 'docker_image_static_analysis'
    uid = Column(String(50), primary_key=True)
    image_name = Column(String(100), nullable=False)
    cve = Column(String(50), nullable=False)
    severity = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)

def main():

    Session = sessionmaker(db)  
    session = Session()

    base.metadata.create_all(db)

    output_folder = "outputs"
    file_name = "trivy_jenkins_2.60.3_results.json"

    with open(os.path.join(output_folder, file_name)) as f: 
        trivy_data = json.load(f)
        
    image_name = trivy_data[0]["Target"]

    for vulnerability in trivy_data[0]["Vulnerabilities"]:
        
        uid = uuid4()
        cve = vulnerability["VulnerabilityID"]
        severity = vulnerability["Severity"]
        
        if "References" in vulnerability:
            url = vulnerability["References"][0]

        docker_vuln = Docker_Image_Static_Analysis(uid=uid,
                                                image_name=image_name,
                                                cve=cve,
                                                severity=severity,
                                                url=url)
        session.add(docker_vuln)  
        session.commit()
        
    session.close()

if __name__ == "__main__":
    main()