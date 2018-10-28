# Code largely based on https://github.com/CoreyMSchafer/code_snippets

from flask import Flask, render_template, url_for

app = Flask(__name__)

# All the information
posts = [
    {
        'index': 'Data Processing',
        'subindex': '',
        'title': 'Objective',
        'content': '1. Find the number of graduates yearly by state and field \
                       of study. \n \
                    2. Find the number of jobs created yearly by state and \
                       industries. \n \
                    3. To find the correlations between the number of \
                       graduates by field of study and the number of jobs \
                       created by industries. \n\n \
                    Please note: This study concerns only the data in Malaysia.',
        'show_image': 'False',
        'image': '',
        'image_style': ''
    },
    {
        'index': 'Objective 1',
        'subindex': 'Findings 1.1',
        'title': 'Total Graduates Output by State in year 2015',
        'content': 'A first look at the total graduates output overall to show \
                    a rough idea of the output density in Malaysia. \n \
                    Please note: A dataset from year 2015 is chosen as it is \
                    the most recent dataset that contains the required data \
                    and is public available.',
        'show_image': 'True',
        'image': '/static/images/total_graduates_output-by-state-2015.jpg',
        'image_style': 'width:1050px;height:376px;'
    },
    {
        'index': 'Objective 1',
        'subindex': 'Findings 1.2',
        'title': 'Total Graduates Output by Field of Study in year 2015',
        'content': 'The bar chart below shows the number of graduates \
                    by their field of study in Malaysia.',
        'show_image': 'True',
        'image': '/static/images/total-graduate-by-field-2015.jpg',
        'image_style': 'width:1050px;height:644px;'
    },
    {
        'index': 'Objective 1',
        'subindex': 'Findings 1.3.1',
        'title': 'Number of Graduates by Field of Study and State',
        'content': 'A more detail stacked bar chart that visualizes the \
                    graduates output in each state with each stack in a bar \
                    representing a field of study.',
        'show_image': 'True',
        'image': '/static/images/graduates-output-by-state-2015.jpg',
        'image_style': 'width:1050px;height:290px;'
    },
    {
        'index': 'Objective 1',
        'subindex': 'Findings 1.3.2',
        'title': 'Findings 1.3.1 w/o Selangor',
        'content': 'As the number of graduates in Selangor dramatically \
                    exceeds any other state, it is removed in the following \
                    chart to have a better focus on the rest of the states.',
        'show_image': 'True',
        'image': '/static/images/graduates-output-by-state-2015-wo-selangor.jpg',
        'image_style': 'width:1050px;height:742px;'
    },
    {
        'index': 'Objective 1',
        'subindex': 'Findings 1.4',
        'title': 'Trend of Graduates Output by Field of Study',
        'content': 'The line chart covers multiple datasets ranging from year \
                    2012 - 2015, revealing the trends of the number of \
                    graduates in each field of study for the past years.',
        'show_image': 'True',
        'image': '/static/images/graduates-in-malaysia-yearly-by-field.jpg',
        'image_style': 'width:1050px;height:518px;'
    },
    {
        'index': 'Objective 2',
        'subindex': 'Findings 2.1',
        'title': 'Number of Vacancies in Malaysia by Industries',
        'content': 'The following treemap covers the number of jobs created \
                    in year 2016.',
        'show_image': 'True',
        'image': '/static/images/total-vacancies-by-industries-2016.jpg',
        'image_style': 'width:1050px;height:475px;'
    },
    {
        'index': 'Objective 3',
        'subindex': 'Findings 3.1',
        'title': 'Correlations between Graduates Output and Number \
                  of Jobs Created',
        'content': 'Correlations are calculated by Pearson Correlation method, \
                    using the dataset integrated from the pre-processed \
                    datasets containing the data on Graduates Output in \
                    2015 and number of Vacancies in \
                    2016. It is assumed in this case that most, if not all, \
                    graduates graduated at the end of year, and that they only \
                    start to work in the year after their graduation. \n\n \
                    The following heatmap is generated from the correlations \
                    calculated previously, with each square representing the \
                    corresponding correlation between a vacancy industry and \
                    a field of study of graduates.',
        'show_image': 'True',
        'image': '/static/images/correlations.jpg',
        'image_style': 'width:1069px;height:1048px;'
    },
    {
        'index': 'Disclaimer',
        'subindex': '',
        'title': '',
        'content': 'This project is just a showcase of ability to present and \
                    process data, as well as the ability to create and deploy \
                    a web app, hence the creation of this website. \
                    Therefore, given the limitation on time, in-depth \
                    explanation in the data processing and analysis of the \
                    results are not the focus of this study.',
        'show_image': 'False',
        'image': '',
        'image_style': ''
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



if __name__ == '__main__':
    app.run(debug=True)