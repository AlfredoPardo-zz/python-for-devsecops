# -*- coding: utf-8 -*-

# mm_pybot specific
import re
from mmpy_bot.bot import respond_to

""" DB SPECIFIC """

from sqlalchemy import create_engine, Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from datetime import datetime

postgres_username=os.environ['POSTGRES_USERNAME']
postgres_password=os.environ['POSTGRES_PASSWORD']
postgres_host=os.environ['POSTGRES_HOST']
postgres_database=os.environ['POSTGRES_DATABASE']

db_string = 'postgresql+psycopg2://{}:{}@{}/{}'.\
        format(postgres_username, \
        postgres_password, \
        postgres_host,
        postgres_database)

db = create_engine(db_string)  
Base = declarative_base()

class Docker_Bench(Base):
    __tablename__ = 'docker_bench'
    uid = Column(String(50), primary_key=True)
    test_id = Column(String(10), nullable=False)
    test_description = Column(String(100), nullable=False)
    result_id = Column(String(10), nullable=False)
    result_description = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)

""" END OF DB SPECIFIC """


@respond_to('^docker bench$', re.IGNORECASE)
def ping_reply(message):

    Session = sessionmaker(db)  
    session = Session()

    docker_bench_items = session.query(Docker_Bench).all()

    status = {}
    
    md_controls_titles = {}
    md_controls_items = {}

    for docker_bench_item in docker_bench_items:

        if docker_bench_item.status not in status:
            status[docker_bench_item.status] = 1
        else:
            status[docker_bench_item.status] += 1

        if docker_bench_item.test_id not in md_controls_items:
            md_controls_titles[docker_bench_item.test_id] = docker_bench_item.test_description
            md_controls_items[docker_bench_item.test_id] = "|*ID*|*Description*|*Status*|\n|-|-|-|\n"
        
        control_item_status = ""
        if docker_bench_item.status == "INFO":
            control_item_status = ":information_source:"
        elif docker_bench_item.status == "WARN":
            control_item_status = ":warning:"
        elif docker_bench_item.status == "PASS":
            control_item_status = ":white_check_mark:"
        else:
            control_item_status = ":spiral_notepad:"

        md_controls_items[docker_bench_item.test_id] = md_controls_items[docker_bench_item.test_id] + "|{}|{}|{}|\n".\
            format(docker_bench_item.result_id, docker_bench_item.result_description, control_item_status)

    md_response = "# Docker Bench Results\n\n"
    md_response += "## Summary\n\n"
    md_response += "|Status|Amount|\n"
    md_response += "|-|-|\n"
    md_response += "|:warning: **Warning**|{}|\n".format(status["WARN"])
    md_response += "|:white_check_mark: **Pass**|{}|\n".format(status["PASS"])
    md_response += "|:information_source: **Informational**|{}|\n".format(status["INFO"])
    md_response += "|:spiral_notepad: **Note**|{}|\n".format(status["NOTE"])
    md_response += "\n\n"
    md_response += "## Items\n\n"

    for ct_id, ct_description in md_controls_titles.items():
        md_response += "### {} - {}\n\n".format(ct_id, ct_description)

        md_response += "{}\n".format(md_controls_items[ct_id])            

    message.reply(md_response)    
    
ping_reply.__doc__ = "Send Current Controls Status"
