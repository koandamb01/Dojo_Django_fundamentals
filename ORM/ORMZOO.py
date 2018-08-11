
################################# YELLOW BELT ################################
# Find all baseball leagues. 
League.objects.filter(sport="Baseball")

# Find all womens' leagues.
League.objects.filter(name__contains="womens")

# Find all leagues where sport is any type of hockey.
League.objects.filter(sport__contains="Hockey")
 
# Find all leagues where sport is something OTHER THAN football.
League.objects.exclude(sport="Football")

# Find all leagues that call themselves "conferences".
League.objects.filter(name__contains="Conference")

# Find all leagues in the Atlantic region.
League.objects.filter(name__contains="Atlantic")

# Find all teams based in Dallas.
Team.objects.filter(location="Dallas")

# Find all teams named the Raptors.
Team.objects.filter(team_name="Raptors")

# Find all teams whose location includes "City".
Team.objects.filter(location__contains="City")

# Find all teams whose names begin with "T".
Team.objects.filter(team_name__startswith="T")

# Return all teams, ordered alphabetically by location.
Team.objects.all().order_by("location")

# Return all teams, ordered by team name in reverse alphabetical order.
Team.objects.all().order_by("-team_name")

# Find every player with last name "Cooper".
Player.objects.filter(last_name="Cooper")

# Find every player with first name "Joshua".
Player.objects.filter(first_name="Joshua")

# Find every player with last name "Cooper" EXCEPT FOR Joshua.
Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")

# Find all players with first name "Alexander" OR first name "Wyatt"
Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
