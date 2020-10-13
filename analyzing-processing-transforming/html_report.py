import os
import json
import pyjade
import jinja2

def main():

    output_folder = "./outputs"
    file_name = "trivy_jenkins_2.60.3_results.json"

    trivy_data = json.loads(open(os.path.join(output_folder, file_name)).read())[0]

    trivy_template = open("./templates/trivy_report.jade").read()

    trivy_report_template = jinja2.Template(trivy_template)
    rendered_template = trivy_report_template.render(target=trivy_data["Target"], 
                                                     vulnerabilities=trivy_data["Vulnerabilities"])
    html_converted = pyjade.utils.process(rendered_template)

    open("./outputs/trivy_report.html", "w").write(html_converted)

if __name__ == "__main__":
    main()