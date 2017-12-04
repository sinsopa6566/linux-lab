import click
import requests

from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO

@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def main(src, dst):
    	"""Get Photo Phone From Siamphone"""
	src_search=""	
	for fn in src:
       		src_search+='%s' % (fn)+" "
	src_search+='%s'%(dst)
	url='https://www.google.co.in/search?q='+src_search+' siamphone'
	html=requests.get(url.replace(' ','+'))
	b=BeautifulSoup(html.content,'html.parser')
	getUrl=b.find_all('h3',{'class':'r'})[0].a['href'].replace('/url?q=','')
	for x in range(len(str(getUrl))):
		if getUrl[x]=='&':
			getUrl=getUrl[:x]
			break
	html=requests.get(getUrl)
	b=BeautifulSoup(html.content,'html.parser')
	photo=b.find_all('div',{'id':'section_left'})[0].img['src']
	req=requests.get('http://www.siamphone.com'+photo)
	img=Image.open(StringIO(req.content))
	img.show()
