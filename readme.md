
# Companies House to Google Big Query

## Install

On a Google Compute Engine Instance

- Set up pip3

```
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3 get-pip.py
```

- Install pandas.

```
sudo pip3 install pandas
```

## Tranform the data

Download Companies House data

```
curl http://download.companieshouse.gov.uk/BasicCompanyData-2018-02-01-part1_5.zip -O
```

Clone this repo.

```
git clone https://github.com/ScatteredInk/companies-house-google-big-query.git
cd companies-house-google-big-query

```

Run script

```
python3 basic_coh_to_gbq.py BasicCompanyData-2018-02-01-part1_5.zip
```

## Transfer to Google Big Query

```
bq load --noreplace --source_format=CSV uk_companies_house.company_data gbq_BasicCompanyData-2018-02-01-part1_5.csv company_data_schema.json
```

gsutil cp 2018-02-11.csv gs://uk-psc-data/2018-02-11.csv

# UK PSC data to BODS

Install jq and unzip

```
sudo apt-get install jq unzip
```

# Some spare material to delete, probably


Load Pyton with `python3` and: 

- remove headers from CSV file
- perform any other data cleaning (dates!)


```

```





Load the database

```
bq load --noreplace --source_format=CSV uk_companies_house.company_data gs://uk-psc-data/1_5
.csv company_data_schema.json
```

TODO: 

- specify nulls as NaN
- add dates to CSVs