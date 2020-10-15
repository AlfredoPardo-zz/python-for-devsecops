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

class Kube_Bench(Base):
    __tablename__ = 'kube_bench'
    uid = Column(String(50), primary_key=True)
    time = Column(String(50), nullable=False)
    node_type = Column(String(50), nullable=False)
    section_id = Column(String(50), nullable=False)
    section_description = Column(String(255), nullable=False)
    test_id = Column(String(50), nullable=False)
    test_description = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)

""" END OF DB SPECIFIC """

@respond_to('^kube bench$', re.IGNORECASE)
def ping_reply(message):

    Session = sessionmaker(db)  
    session = Session()

    kube_bench_items = session.query(Kube_Bench).all()

    node = {
        "Master": {
            "status": {},
            "md_controls_titles": {},
            "md_controls_items": {}
        },
        "Node": {
            "status": {},
            "md_controls_titles": {},
            "md_controls_items": {}
        }
    }

    for kube_bench_item in kube_bench_items:

        if kube_bench_item.status not in node[kube_bench_item.node_type]["status"]:
            node[kube_bench_item.node_type]["status"][kube_bench_item.status] = 1
        else:
            node[kube_bench_item.node_type]["status"][kube_bench_item.status] += 1

        if kube_bench_item.section_id not in node[kube_bench_item.node_type]["md_controls_items"]:
            node[kube_bench_item.node_type]["md_controls_titles"][kube_bench_item.section_id] = kube_bench_item.section_description
            node[kube_bench_item.node_type]["md_controls_items"][kube_bench_item.section_id] = "|*ID*|*Description*|*Status*|\n|-|-|-|\n"
            
        control_item_status = ""
        if kube_bench_item.status == "FAIL":
            control_item_status = ":x:"
        elif kube_bench_item.status == "PASS":
            control_item_status = ":white_check_mark:"
        else:
            control_item_status = ":warning:"

        node[kube_bench_item.node_type]["md_controls_items"][kube_bench_item.section_id] += "|{}|{}|{}|\n".\
            format(kube_bench_item.test_id, kube_bench_item.test_description, control_item_status)
    
    md_response = "# Kube Bench Results\n\n"
    md_response += "## Summary\n\n"
    md_response += "### Master Node\n\n"
    md_response += "|Status|Amount|\n"
    md_response += "|-|-|\n"
    md_response += "|:x: **Fail**|{}|\n".format(node["Master"]["status"]["FAIL"])
    md_response += "|:warning: **Warning**|{}|\n".format(node["Master"]["status"]["WARN"])
    md_response += "|:white_check_mark: **Pass**|{}|\n".format(node["Master"]["status"]["PASS"])
    md_response += "\n\n"
    md_response += "### Worker Node\n\n"
    md_response += "|Status|Amount|\n"
    md_response += "|-|-|\n"
    md_response += "|:x: **Fail**|{}|\n".format(node["Node"]["status"]["FAIL"])
    md_response += "|:warning: **Warning**|{}|\n".format(node["Node"]["status"]["WARN"])
    md_response += "|:white_check_mark: **Pass**|{}|\n".format(node["Node"]["status"]["PASS"])
    md_response += "\n\n"
    md_response += "## Items\n\n"
    
    md_response += "### Master Node\n\n"
    for ct_id, ct_description in node["Master"]["md_controls_titles"].items():
        md_response += "#### {} - {}\n\n".format(ct_id, ct_description)
        md_response += "{}\n".format(node["Master"]["md_controls_items"][ct_id])
    
    md_response += "### Worker Node\n\n"
    for ct_id, ct_description in node["Node"]["md_controls_titles"].items():
        md_response += "#### {} - {}\n\n".format(ct_id, ct_description)
        md_response += "{}\n".format(node["Node"]["md_controls_items"][ct_id])

    message.reply(md_response)    
    
ping_reply.__doc__ = "Send Current Controls Status"