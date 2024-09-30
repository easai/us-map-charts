# us-map-charts

The Electoral College is a set of electors who are selected to elect the president and vice president. The process is described in Article II of the U.S. Constitution. The number of electoral votes a state has equals its number of Senators plus its number of Representatives in the House of Representatives, the latter being dependent on the Census's reported population.

Here is an excellent explanation how it works:
[How the Electoral College Works](https://www.youtube.com/watch?v=OUS9mM8Xbbw)

![Electoral-Votes](https://github.com/easai/us-map-charts/blob/main/images/Electoral-Votes.png)
![Electoral-Votes-Northeastern](https://github.com/easai/us-map-charts/blob/main/images/Electoral-Votes-Northeastern.png)
### Installation
Run the following command to install all the dependencies.
```bash
poetry install
```
### Usage
This map shows all U.S. states and the number of electors.
```bash
poetry run py .\us_map_charts\electors.py
```

This map shows the northeastern U.S. states and the number of electors.
```bash
poetry run py .\us_map_charts\northeastern.py
```
