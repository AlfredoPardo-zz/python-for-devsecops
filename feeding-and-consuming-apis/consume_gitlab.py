import requests
import urllib3
from pprintjson import pprintjson as ppjson

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_url = "https://gitlab.com/api/v4"
private_token = "your-personal-access-token-goes-here"
separator = "*" * 80

project_id = "999999999"
group_id = "999999999"
commit_id = "999999999"
pipeline_id = "999999999"

# Groups
response = requests.get("{}/groups?private_token={}".format(api_url, 
    private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Groups",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Group Members
response = requests.get("{}/groups/{}/members?private_token={}".format(api_url,
    group_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Group Members",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Projects
response = requests.get("{}/projects/{}?private_token={}".format(api_url, 
    project_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Projects",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Project Members
response = requests.get("{}/projects/{}/members?private_token={}".format(api_url,
    project_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Project Members",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Commits
response = requests.get("{}/projects/{}/repository/commits?private_token={}".\
    format(api_url, project_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Repository Commits",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Commit Details
response = requests.get("{}/projects/{}/repository/commits/{}/diff?private_token={}".\
                        format(api_url, project_id, commit_id, private_token),
                               verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Repository Commit Details",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Merge Requests
response = requests.get("{}/projects/{}/merge_requests?private_token={}".\
    format(api_url, project_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Project Merge Requests",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Pipelines
response = requests.get("{}/projects/{}/pipelines?private_token={}".\
    format(api_url, project_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Project Pipelines",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())

# Jobs
response = requests.get("{}/projects/{}/pipelines/{}/jobs?private_token={}".\
    format(api_url, project_id, pipeline_id, private_token), verify=False)

print("{}\n{}\n{}".format(separator,"Gitlab Project Pipeline Jobs",separator))
print("{}\n{}".format("\tHeaders",separator))
for header_key, header_value in response.headers.items():
    print("\t{}: {}".format(header_key, header_value))
print("{}\n\t{}\n{}".format(separator,"Response",separator))
ppjson(response.json())
