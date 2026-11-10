# NBA Team Stats: Data Pipeline & EDA (2021–22 Season)

Pulls 2021–22 NBA regular-season data from the API-NBA (RapidAPI) service, cleans and merges it into one team-level dataset, and explores which team stats correlate with winning at home and away.

## Pipeline

```
API-NBA (RapidAPI)
   │
   ├── import_teams.py      → nbateams.json      → nbateams_normalized.csv
   ├── import_standings.py  → nbastandings.json  → nbastandings_normalized.csv
   └── import_teamstats.py  → nbateamstats.json  → nbateamstats_normalized.csv
                                   │
                          data_prep.ipynb  (clean + merge)
                                   │
                          nbateamstats_final.csv
                                   │
                          exploratoryDataAnalysis.ipynb
```

## Files

| File | Purpose |
|---|---|
| `import_teams.py` | Fetches all teams from `/teams`, keeps only NBA franchises, saves JSON + flattened CSV |
| `import_standings.py` | Fetches league standings from `/standings` (season `2021`), saves JSON + flattened CSV |
| `import_teamstats.py` | Loops over 30 team IDs, fetches regular-season stats from `/teams/statistics` (`stage=2`), 6 s delay between calls to respect rate limits |
| `data_prep.ipynb` | Drops unused standings columns, renames columns to camelCase, merges team stats with standings (conference, home/away records) on `teamID`, writes `nbateamstats_final.csv` |
| `exploratoryDataAnalysis.ipynb` | Missing-value check, summary stats, correlation heatmaps, East-conference regression plot |

Note: in the API, `season=2021` means the 2021–22 season.

## Setup

**Requirements:** Python 3.11+

```bash
pip install requests pandas numpy seaborn matplotlib colorcet ipywidgets jupyter
```

**API key:** create a free account on [RapidAPI](https://rapidapi.com/) and subscribe to [API-NBA](https://rapidapi.com/api-sports/api/api-nba). Then add a `creds.py` next to the scripts:

```python
api_key = "YOUR_RAPIDAPI_KEY"
```

Add `creds.py` to `.gitignore` so the key is never committed.

## Usage

1. Fetch the raw data (each script writes a JSON and a `_normalized.csv`):
   ```bash
   python import_teams.py
   python import_standings.py
   python import_teamstats.py   # ~3 min: 30 teams × 6 s delay
   ```
2. Put the generated CSVs in a `data/` folder.
3. Run `data_prep.ipynb` to produce `nbateamstats_final.csv`.
4. Run `exploratoryDataAnalysis.ipynb`.

## Analysis & Findings

Correlations with **home wins** (`winHome`):

| Feature | Correlation |
|---|---|
| Field goals made (`fgm`) | 0.46 |
| Defensive rebounds (`defReb`) | 0.41 |
| Points off turnovers | 0.30 |
| Three-pointers made (`tpm`) | 0.29 |
| Assists | 0.29 |
| Steals | 0.29 |

- `fgm` is the strongest single feature tied to winning at home.
- Among defensive stats, `defReb` correlates more strongly than `steals`.
- The EDA also plots defensive rebounds vs. home wins for Eastern Conference teams with a regression line, and repeats the correlation analysis for away wins.

Caveat: this is one season and 30 teams, so correlations are exploratory, not predictive.

## Tech Stack

Python, pandas, NumPy, seaborn, matplotlib, colorcet, Jupyter, REST API (requests)

## Possible Next Steps

- Extend to multiple seasons for a larger sample
- Fit a regression / tree model on win percentage with cross-validation
- Add playoff stats (`stage=3`)
