from sqlalchemy.orm import sessionmaker
from models import

Session = sessionmaker(bind=engine)
session = Session()

# Seed data for series and comics
series_data = [
  {"name": "Series A", "comics": [{"title": "Comic A1", "issue": 1}, {"title": "Comic A2", "issue": 2}]},
  {"name": "Series B", "comics": [{"title": "Comic B1", "issue": 1}, {"title": "Comic B2", "issue": 2}]}
]

for series_info in series_data:
  series = Series(name=series_info["name"])
  session.add(series)
  session.commit()  # Commit to get the series ID if needed for relationships

  for comic_info in series_info["comics"]:
    comic = Comic(title=comic_info["title"], issue=comic_info["issue"], series_id=series.id)
    session.add(comic)

  session.commit()

print("Data seeded successfully.")
