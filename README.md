# job-details-scraper

### UrlParsing.Py
#### UrlParseBs

```python
from UrlParsing import UrlparseBs
obj = UrlParseBs(url)
```
This function first checks the url is existing or not . If it is exits , it can parse using UrlParse . Otherwise "Error while occuring with code "+status . 

###### Example

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
In This function first install the Driver . Incase of , The driver is  unable to install in system , then it sets the prebuild Driver in the system
. 
Note - It can only works on **Firefox**

#### Example

```python
from UrlParsing import UrlParseSe
obj = UrlParse(url)
Data = obj.parse()
```
 **The Whole application uses UrlParseBs**

### GenLink.py 
- It **navigates** through all the pages ,
- It extracts all the **Url contents** from the page ,
- It dumps the **Url** using **Pickle** .

### PageExtracter.py
Regarding to this program , It extracts the content from the **parsed data** .
It returns the field entities like **jobtitle** , **institution name** , **location** , **jobtype** , **salary** , **summary** , **posted on** , **key term data** .
 
### MergeData.py
The program just merges all `.xlsx` files in **datasets folder** and remove duplication of records and export it as `mergedata.xlsx`.

### WordFrequency.py
The program is basically designed to find the **word count** of the **summary field** in the extracted data and export it as `wordfrequency.xlsx` file with fields **words**, **count**, **per-word**, **post-word**.
