{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c47ceb14-2cf7-40c9-ab3c-2cb361bdc015",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "import creds\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "def get_nba_teams(api, filename):\n",
    "    url=\"https://api-nba-v1.p.rapidapi.com/teams\"\n",
    "    headers = {\n",
    "\t\t\"X-RapidAPI-Key\": api,\n",
    "\t\t\"X-RapidAPI-Host\": \"api-nba-v1.p.rapidapi.com\"\n",
    "    }\n",
    "    response = requests.get(url, headers=headers)\n",
    "    print(response.json())\n",
    "    api_data=response.json()\n",
    "    nbaFranchise_True = [team for team in api_data[\"response\"]if team[\"nbaFranchise\"]]# Search for nbaFranchise == True\n",
    "    filtered_data= {\n",
    "        \"results\": len(nbaFranchise_True),\n",
    "\t\t\"response\": nbaFranchise_True\n",
    "    }\n",
    "    with open(filename, \"w\") as file:\n",
    "        json.dump(filtered_data, file, indent=4)\n",
    "        \n",
    "def get_json2csv(filename):\n",
    "    with open(filename, 'r') as json_data:\n",
    "        data = json.load(json_data)\n",
    "        df = pd.json_normalize(data['response'])\n",
    "        output_filename=os.path.splitext(filename)[0]#[0] -> Return base filename without its  extension\n",
    "        df.to_csv(output_filename + '_normalized.csv')\n",
    "api=creds.api_key\n",
    "filename='nbateams.json'\n",
    "get_nba_teams(api, filename)\n",
    "get_json2csv(filename)"
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
