# job-details-scraper

### UrlParsing.Py
#### UrlParseBs

```python
from UrlParsing import UrlparseBs
obj = UrlParseBs(url)
```
This class checks the url is existing or not. If it is exits, it can parse the site using `BeautifulSoup4`. Otherwise `"Error while occuring with code "+status` . 

###### Example:

```python
from UrlParsing import UrlParseBs
obj = UrlParse(url)
Data = obj.parse()
```
#### UrlParseSe

```python
from UrlParsing import UrlParseSe
obj = UrlParseSe(url)
```
In Selenium, The driver should be installed for installing drivers [check](https://selenium-python.readthedocs.io/installation.html#drivers). Incase The driver is  not properly installed in system , then it switch back to the available driver provided in the `Drivers Folder` .
`Note: It can only works on **Firefox** `

##### Example:

```python
from UrlParsing import UrlParseSe
obj = UrlParse(url)
Data = obj.parse()
```
 **The Whole application uses `UrlParseBs` to parse the site**

### GenLink.py 
- It **navigates** through all the pages,
- It extracts all the **Url contents** from the page,
- It dumps the **Extracted Url** into a pickle file as `job_urls.txt`.

### PageExtracter.py
Regarding to this program , It extracts the content from the **parsed data** .
It returns the field entities like **jobtitle** , **institution name** , **location** , **jobtype** , **salary** , **summary** , **posted on** , **key term data** .

### main.py
The main.py reads the **joburl.txt** .
 Which contains all the url , Then using the **Extractor.py** the **main.py** extracts all the contents from the url and save it in **.xlsx file** .
 

### MergeData.py
The program just merges all `.xlsx` files in **datasets folder** and remove duplication of records and export it as `mergedata.xlsx`.

### WordFrequency.py
The program is basically designed to find the **word count** of the **summary field** in the extracted data and export it as `wordfrequency.xlsx` file with fields **words**, **count**, **per-word**, **post-word**.

### Contributors
1. [Amira Begam](https://github.com/AmiraBegam)
2. [Ghanesh Mouthouvel](https://github.com/ghaneshmouthouvel)
3. [Ghoseya](https://github.com/ghoseya)
4. [Jagadeesh Mouthouvel](https://github.com/jagadeesh-tolnut)
5. [Naseema](https://github.com/myselfusereasy/)

### License
This project is license under **AGPL v3**. Read `LICENSE` file for more infomration.
