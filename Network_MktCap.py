from lxml import html  
import requests
from time import sleep
import json
import argparse
from collections import OrderedDict
import pandas as pd
import os
import datetime


def parse(ticker):
	url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
	response = requests.get(url, verify=False)
	print ("Parsing %s"%(url))
	sleep(4)
	parser = html.fromstring(response.text)
	summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
	summary_data = OrderedDict()
	other_details_json_link = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker
	summary_json_response = requests.get(other_details_json_link)
	#try:
	data = html.fromstring(summary_json_response.text)
	#json_loaded_summary =  json.loads(summary_json_response.text)

	#y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
	#earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
	mk = data.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/span/text()')	
	#eps = json_loaded_summary["quoteSummary"]["result"][0]["earningsHistory"]["history"]["epsActual"]['raw']
	if mk:
		new = mk[0]
		return new[:-1]
	else: 
		return -1
	#return mk
	#try:
	#	eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["epsActual"]['raw']
	#except:
	#	print("OOPS1")
	#try:
	#	curas = json_loaded_summary["quoteSummary"]["result"][0]["balanceSheetHistory"]["balanceSheetStatements"][0]["totalCurrentAssets"]['raw']/10000000000
	#except:
	#	print("OOPS1")
	#try:
	#	curliab = json_loaded_summary["quoteSummary"]["result"][0]["balanceSheetHistory"]["balanceSheetStatements"][0]["totalCurrentLiabilities"]['raw']/10000000000
	#except:
	#	print("OOPS2")

	#curas = json_loaded_summary["quoteSummary"]["result"][0]["balanceSheetHistory"]["balanceSheetStatements"]["totalCurrentAssets"]['raw']/10000000000
	#cliab = json_loaded_summary["quoteSummary"]["result"][0]["balanceSheetHistory"]["balanceSheetStatements"]["totalCurrentLiabilities"]['raw']/10000000000

	#rev = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["Revenue"]['raw']
		#marketcap = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["marketCap"]['raw']
	#datelist = []
	#for i in earnings_list['earningsDate']:
	#	datelist.append(i['fmt'])
	#earnings_date = ' to '.join(datelist)
	#for table_data in summary_table:
	#	raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
	#	raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
	#	table_key = ''.join(raw_table_key).strip()
	#	table_value = ''.join(raw_table_value).strip()
	#	summary_data.update({table_key:table_value})
	#summary_data.update({'1y Target Est':y_Target_Est,'EPS (TTM)':eps,'Earnings Date':earnings_date,'ticker':ticker,'url':url})
	#summary_data.update({'Market Cap':(shareprice*sharesout/1000000000000)})		
	#return eps,curas,curliab
	#except:
	#print ("Failed to parse json response")
	#	return {"error":"Failed to parse json response"}

symbols = pd.read_csv("../Dataset/ind_nifty500list.csv")
		
if __name__=="__main__":
	#argparser = argparse.ArgumentParser()
	#argparser.add_argument('ticker',help = '')
	#args = argparser.parse_args()
	#ticker = args.ticker
	#print ("Fetching data for %s"%(ticker))

	mkt = []
	for i in range(0,501):

		symbol = symbols.iloc[i,2]


		print(symbol)

		symbol1 = symbol + ".NS"

		#if(sp500.iloc[1,1] == '02-01-2009'):
		scraped_data = parse(symbol1)

		mkt.append(scraped_data)
						

	actions = pd.DataFrame()

	actions["MktCap"] = pd.Series(mkt)


	
	actions.to_csv("NSEMkt.csv")	
	#print(sp500.head())

			#sp500.to_csv("ftof\\"+symbol+".csv")

		#except:
		 # continue
		#print ("Writing data to output file")
	#with open('%s-summary.json'%(ticker),'w') as fp:
	#	json.dump(scraped_data,fp,indent = 4)