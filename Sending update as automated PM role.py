import pandas as pd
import datetime
import smtplib

# read in the google sheets file
df = pd.read_excel('https://docs.google.com/spreadsheets/d/1mghDFocpj-RXn-TnSb3vzXwLfKvOPP1o8414titXEQI/edit?usp=sharing')

# group the responses by the question column and count the number of each response
grouped_responses = df.groupby('Question')['Response'].value_counts()

# create a bar chart of the grouped responses
grouped_responses.plot(kind='bar')

# display the chart
plt.show()

# check if there is a chart to display
if not grouped_responses.empty:

# send email alert to ajayc003@gmail.com that there is a chart to display
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('email@gmail.com', 'password')
server.sendmail('email@gmail.com', 'ajayc003@gmail.com', 'There is a chart to display for the responses file.')
server.quit()

# check if the current time is Friday at 2:00PM IST
now = datetime.datetime.now()
if now.weekday() == 4 and now.hour == 14:

# send email alert to user to upload the file
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('email@gmail.com', 'password')
server.sendmail('email@gmail.com', 'email@gmail.com', 'Please upload the responses file at https://docs.google.com/spreadsheets/d/1mghDFocpj-RXn-TnSb3vzXwLfKvOPP1o8414titXEQI/edit?usp=sharing')
server.quit()

# wait for 600 seconds for the email to be clicked
time.sleep(600)

# check if the email was clicked
if not server.clicked:
# send email alert to laksh365@gmail.com that the email to upload the file was not clicked
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('email@gmail.com', 'password')
server.sendmail('email@gmail.com', 'laksh365@gmail.com', 'The email to upload the responses file was not clicked.')
server.quit()