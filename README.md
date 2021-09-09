
![Logo](https://eliimagebucket.s3.amazonaws.com/easy+Street.png)

    
# Easy Street

Easy Street allows people to programmatically find apartments in Brooklyn via scraping and compiling apartments listings from Craigslist that match their search criteria. No digging through listings manually. Find what you need. Use EasyStreet. 
## Run Locally

Clone the project

```bash
  git clone https://github.com/ElijahLogan/EasyStreet.git
```

Go to the project directory

```bash
  cd EasyStreet
```

Install dependencies

```bash
  pip3 install bs4, urllib
```

Run Jupyter Notebook

```bash
 jupyter notebook 
```


Run EasyStreet and download a csv of apartments within the area you want to move and in your price range

```bash
from EasyStreet import EasyStreet
apartmentFinder = EasyStreet(1, 11237, 900, 1400)
apartmentListings = bot.apartmentFinder()
```



  
### Sort and save data


```bash
apartmentListings.sort_values('price')
```

![Logo](https://eliimagebucket.s3.amazonaws.com/sorted.png)


```bash
apartmentListings.to_csv('BushwickApartments.csv')
```
## Tech Stack

**Client:** bs4, pandas, urllib.request



  
## Roadmap

- FrontEnd for people that aren't engineers/analysts 

- Airflow Dag to automatically check criagslist from lamda functions 3x a day 

- Outpu functions to kinesis firehose

- Event alert and send message of new apartment that meets search criteria


  
## Authors

- [@ElijahLogan](https://www.github.com/ElijahLogan)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
# Hi, I'm Elijah ! 👋

  I'm a Full Stack Develoloper and Data Engineer from NY who got tired of checking Craigslist for apartments in my area and other areas of nyc so I created a Scraper to check for me! 
  

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherinempeterson.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/elijah-logan//)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/eli_izell/)

  