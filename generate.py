import pandas as pd
import jinja2
import json


data = pd.read_excel("app_coor.xlsx")[["x", "y", "value", "page"]]
with open("template.html") as f:
    template = jinja2.Template(f.read())
for page in set(data['page'].dropna()):
    page = int(page)
    subdata = data.query("page == @page")[["x", "y", "value"]]
    html = template.render(data=json.dumps(subdata.values.tolist()), id=page, max_value=subdata['value'].max())
    with open(f"{page}.html", "w") as f:
        f.write(html)
