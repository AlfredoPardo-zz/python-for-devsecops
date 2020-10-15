# Feeding and Consuming APIs

## Consuming GitLab API

### How to evaluate permissions

|Access Level|Access Type|
|-|-|
|10|Guest Access|
|20|Reporter Access|
|30|Developer Access|
|40|Maintainer Access|
|50|Owner Access|

### Notes

* Please...
    * ... replace `private_token` with your *Personal Access Token* from GitLab
    * ... replace `project_id`, `group_id`, `commit_id`, and `pipeline_id` with the ID you want to analyze

## Feeding DefectDojo API

### Notes

* Please...
    * ... replace `your-api-key-goes-here` with your *API v1 Key* from DefectDojo
    * ... replace the `engagement_id` variable with the appropriate ID for the engagement you are intending to run
    * ... replace `api_protocol`, `api_url` and `api_port` as needed.