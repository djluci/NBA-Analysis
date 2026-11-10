{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6ccdd57-f1a0-4a21-af18-5ad43d8e43cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "import creds\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "def get_nba_standings(api, filename):\n",
    "    url = \"https://api-nba-v1.p.rapidapi.com/standings\"\n",
    "    querystring = {\"league\":\"standard\", \"season\":\"2021\"}\n",
    "    headers = {\n",
    "        \"X-RapidAPI-Key\": api,\n",
    "\t\t\"X-RapidAPI-Host\": \"api-nba-v1.p.rapidapi.com\"\n",
    "    }\n",
    "    response = requests.get(url, headers=headers, params=querystring)\n",
    "    print(response.json())\n",
    "    with open(filename, \"w\") as file:\n",
    "        json.dump(api_data, file, indent = 4)\n",
    "def get_json2csv(filename):\n",
    "    with open(filename, 'r') as json_data:\n",
    "        data=json.load(json_data)\n",
    "        df = pd.json_normalize(data['response']) # Have to change response to the last Array of desired data, for reference check each \".JSON\"\n",
    "        output_filename = os.path.splitext(filename)[0] #[0]->Returns filename without extension\n",
    "        df.to_csv(output_filename + '_normalized.csv')\n",
    "api = creds.api_key\n",
    "filename= 'Data/nbastandings.json' \n",
    "get_nba_standings(api, filename)\n",
    "get_json2csv(filename)        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
