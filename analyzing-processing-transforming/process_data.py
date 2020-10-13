import pandas as pd; import matplotlib.pyplot as plt
import numpy as np; import os; import json

def main():

    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(aspect="equal"))

    output_folder = "./outputs"
    file_name = "trivy_jenkins_2.60.3_results.json"

    with open(os.path.join(output_folder, file_name)) as f: 
        trivy_data = json.load(f)
        
    trivy_vulns = pd.json_normalize(trivy_data[0]['Vulnerabilities'])
    df = trivy_vulns.groupby(['Severity']).size().reset_index(name='Counts')

    data = df["Counts"]; values = df["Severity"]

    colors = ['#CB4335','#AF601A','#1A5276','#E67E22']

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"), colors=colors)

    ax.legend(wedges, values,
            title="Severities",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold"); plt.savefig("./images/trivy_pie_chart.png", transparent=True)


if __name__ == "__main__":
    main()