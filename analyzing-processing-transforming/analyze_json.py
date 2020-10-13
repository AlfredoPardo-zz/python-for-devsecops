import os; import json; from pprintjson import pprintjson as ppjson

def main():

    output_folder = "./outputs"
    file_name = "trivy_jenkins_2.60.3_results.json"

    content = json.loads(open(os.path.join(output_folder, file_name)).read())

    ppjson(content)

if __name__ == "__main__":
    main()