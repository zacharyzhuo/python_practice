import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)  # 200為請求成功

# Store API response in a variable.
response_dict = r.json()
# 印出Github共有多少個python倉庫
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []  # 儲存專案名字與星星數量
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Get the project description, if one is available.
    description = repo_dict['description']
    if not description:
        description = 'No description provided.'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }

    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)  # 將基礎色調改成深藍色

# 設定圖表標題、次標籤、主標籤
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)  # Bar為長條圖，以及將X軸調成45度
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)  # 新增資料時預設為空字串
chart.render_to_file('python_repos.svg')
