import requests
import csv

url = "https://jsearch.p.rapidapi.com/search"

query='product designer internship '

querystring = {"query":query,"page":"1","num_pages":"5"}

headers = {
	"X-RapidAPI-Key": "73bdff1dbcmsh0f0a1522e024a65p11bfd9jsnd5e2cacd763d",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}
try:
    response = requests.get(url, headers=headers, params=querystring)

except  ConnectionAbortedError as E:
    print(E)
    
csv_file=open('internship24.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['employer name','job title','job link','employment type'])

data1=response.json()
data2=data1['data']
for info in data2:
    employername=info['employer_name'] 
    jobtitle=info['job_title']
    joblink=info['job_apply_link']
    jobtype=info['job_employment_type']
    
    csv_writer.writerow([employername,jobtitle,joblink,jobtype])

csv_file.close()
