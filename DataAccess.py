import bs4
import pprint
import urllib.request

class DataAccess(object):
    def __init__(self,neighborhood, zipcode, low, high ):
        self.neighborhood = neighborhood
        self.zipcode = zipcode
        self.low = low
        self.high = high    
        self.url = "https://newyork.craigslist.org/search/brk/hhh?query={}&search_distance=1&postal={}&min_price={}&max_price={}&availabilityMode=0&sale_date=all+dates".format(self.neighborhood, self.zipcode, self.low, self.high)

    def apartmentSearch(self):
        
        #grabs a list of apartments in area and price range declared once module is initialized```
        url = self.url

        #Headers
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

        headers={'User-Agent':user_agent,} 

        request=urllib.request.Request(url,None,headers) #The assembled request
        source = urllib.request.urlopen(request)
        soup = bs4.BeautifulSoup(source, 'lxml')

        searchResults = soup.find(id='search-results')

        resultRows = searchResults.find_all('li', class_="result-row")

        apartmentList = self.listUnits(resultRows) 

        footageCleanedList = [self.footageCleaner(i) for i in apartmentList]

        return footageCleanedList


    def detailExtraction(self, html):
        # grabs price, footage, timePosted, apartmentLink
      
          apartment_price = html.find('span', class_="result-price").string
      
          footage = html.find('span', class_="housing")
          #strip uneccessary /n
          # footage = footage.strip()
      
          time_posted = html.find('time').attrs['datetime']
      
          apartment_link = html.find('a').attrs['href']
          apartment_address = self.apartmentAddress(apartment_link)
      
          return [apartment_price, footage, apartment_address, time_posted, apartment_link ]




    def apartmentAddress(self, url):

          
          # Ulr for apartment listing`
      url = url
    
        #Headers
      user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
      headers={'User-Agent':user_agent,}
    
      request=urllib.request.Request(url,None,headers) #The assembled request
      source = urllib.request.urlopen(request)
      soup = bs4.BeautifulSoup(source, 'lxml')
    
      address = soup.find('div', class_='mapaddress')
    
      return address
      
    def listUnits(self,unitListings):

      # functions takea a list and loops over iter
      units = []
      length = len(unitListings) -1
      for i in range(length):
      
        item = unitListings[i]
        data  = self.detailExtraction(item)
        units.append(data)
      return units


    def footageCleaner(self,listing):
        if listing[1]:
              footage_content = listing[1].contents
              footageStr = ' '.join([str(elem) for elem in footage_content])
              footageStr = footageStr.strip()
              listing[1] = footageStr
              return listing
        else:
            return listing
                  
      
