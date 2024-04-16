from jinja2 import Environment, FileSystemLoader
import csv

with open('./rosters/2024-04-16-roster.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    players = [row for row in csv_reader]


environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("varsity_card_template.txt")

for player in players:
  if player['team'] == 'Varsity':
    content = template.render(player)
    with open('./varsity-roster-cards.html', mode="a", encoding="utf-8") as message:
        message.write(content)

for player in players:
  if player['team'] == 'Junior Varsity':
    content = template.render(player)
    with open('./junior-varsity-roster-cards.html', mode="a", encoding="utf-8") as message:
        message.write(content)