from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(chart1ID = 'chart1_ID', chart1_type = 'bar', chart1_height = 300,
chart2ID = 'chart2_ID', chart2_type = 'bar', chart2_height = 300,
chart3ID = 'chart3_ID', chart3_type = 'column', chart3_height = 300,
chart4ID = 'chart4_ID', chart4_type = 'scatter', chart4_height = 300,
chart5ID = 'chart5_ID', chart5_type = 'scatter', chart5_height = 300,
chart6ID = 'chart6_ID', chart6_type = 'column', chart6_height = 300):

#Description of chart1

  chart1 = {"renderTo": chart1ID, "type": chart1_type, "height": chart1_height}
  data = pd.read_csv("/home/niharika/Desktop/jqueryviz/data/data.csv")
  male_count = data[data['Gender'] == 'M']["Gender"].count()
  female_count = data[data['Gender'] == 'F']["Gender"].count()
  series1 = [{"name": 'Male', "data": [male_count],"color":"red"}, {"name": 'Female', "data": [female_count],"color":"purple"}]
  title1 = {"text": 'Gender Ratio of Male and Female in the program'}
  xAxis1 = {"categories": ['Gender']}
  yAxis1 = {"title": {"text": 'Count'}}

#Description of chart2

  chart2 = {"renderTo": chart2ID, "type": chart2_type, "height": chart2_height,}
  technologies = []
  values = []
  for i in data.Technology.unique():
    technologies.append(i)
    values.append(data[data['Technology'] == i]["Technology"].count())

  series2 = [{"name": 'Technologies', "data": values,"color":"yellow"}]
  title2 = {"text": 'Information of total number of Engineers working in each Technologies'}
  xAxis2 = {"categories": technologies}
  yAxis2 = {"title": {"text": 'Count'}}

#Description of chart3

  chart3 = {"renderTo": chart3ID, "type": chart3_type, "height": chart3_height}
  total = male_count + female_count
  male_per = (male_count/total) * 100
  female_per = (female_count/total) * 100
  series3 = [{"name": 'Male', "data": [male_per],"color":"green"},{"name": 'Female', "data": [female_per],"color":"pink"}]
  title3 = {"text": 'Gender Ratio of Engineers present in the program'}
  yAxis3 = {"categories": ['Gender']}
  xAxis3 = {"title": {"text": 'Count'}}

#Description of chart4

  chart4 = {"renderTo": chart4ID, "type": chart4_type, "height": chart4_height}
  lab_X = data[data['Lab'] == 'Banglore']['Lab'].count()
  lab_Y = data[data['Lab'] == 'Mumbai']['Lab'].count()
  series4 = [{"name": 'Banglore', "data": [lab_X],"color":"orange"}, {"name": 'Mumbai', "data": [lab_Y],"color":"black"}]
  title4 = {"text": 'Distribution of students in Lab_X and Lab_Y'}
  xAxis4 = {"categories": ['Lab']}
  yAxis4 = {"title": {"text": 'Count'}}

#Description of chart5

  chart5 = {"renderTo": chart5ID, "type": chart5_type, "height": chart5_height,}
  technologies = []
  values = []
  for i in data.Technology.unique():
    technologies.append(i)
    values.append(data[data['Technology'] == i]["Technology"].count())

  series5 = [{"name": 'Technologies', "data": values,"color":"red"}]
  title5 = {"text": 'Distribution of  All Technologies'}
  xAxis5 = {"categories": technologies}
  yAxis5 = {"title": {"text": 'Count'}}

#Description of chart6

  chart6 = {"renderTo": chart6ID, "type": chart6_type, "height": chart6_height, }
  company = []
  values1 = []
  for j in data.Company.unique():
    company.append(j)
    values1.append(data[data['Company'] == j]["Company"].count())

  series6 = [{"name": 'Technologies', "data": values,"color":"green"}]
  title6 = {"text": 'Company vs Technologies Bar Graph'}
  xAxis6 = {"categories": company}
  yAxis6 = {"title": {"text": 'Count'}}

#return the template files

  return render_template('index.html', chart1ID=chart1ID, chart1=chart1, series1=series1, title1=title1, xAxis1=xAxis1, yAxis1=yAxis1,
                         chart2ID=chart2ID, chart2=chart2, series2=series2, title2=title2, xAxis2=xAxis2, yAxis2=yAxis2,
                         chart3ID=chart3ID, chart3=chart3, series3=series3, title3=title3, yAxis3=yAxis3, xAxis3=xAxis3,
                         chart4ID=chart4ID, chart4=chart4, series4=series4, title4=title4, yAxis4=yAxis4, xAxis4=xAxis4,
                         chart5ID=chart5ID, chart5=chart5, series5=series5, title5=title5, yAxis5=yAxis5, xAxis5=xAxis5,
                         chart6ID=chart6ID, chart6=chart6, series6=series6, title6=title6, yAxis6=yAxis6, xAxis6=xAxis6)




if __name__ == "__main__":
 app.run(debug = True, host='127.0.0.1', port=5000, passthrough_errors=True)
