import random

# Define lists of Marvel and DC comic series
marvel_series = ["Spider-Man", "X-Men", "Avengers", "Fantastic Four", "Iron Man", "Captain America", "Hulk", "Thor", "Guardians of the Galaxy", "Daredevil", "Black Panther", "Doctor Strange", "The Punisher", "Deadpool", "Wolverine", "Runaways", "Exiles", "Alpha Flight", "New Mutants", "Inhumans", "Young Avengers", "Thunderbolts", "Marvel Knights", "Alpha Flight", "Power Pack", "Squadron Supreme", "Excalibur", "X-Factor", "Marvel Two-in-One", "Cloak and Dagger", "Marvel 2099", "Marvel Zombies", "Marvel MAX", "Marvel UK", "Starjammers", "Agents of Atlas", "Marvel Apes", "Marvel Noir", "Marvel Mangaverse", "New Warriors", "Marvel 1602", "Nextwave", "Marvel Team-Up", "Marvel Adventures", "Ultimate Marvel", "Marvel NOW!", "Marvel Legacy", "Marvel Age", "Marvel Illustrated"]

dc_series = ["Batman", "Superman", "Wonder Woman", "Justice League", "The Flash", "Green Lantern", "Aquaman", "Teen Titans", "Green Arrow", "Shazam", "Suicide Squad", "Batgirl", "Nightwing", "Robin", "Harley Quinn", "Birds of Prey", "Justice Society of America", "Legion of Super-Heroes", "Justice League Dark", "The Doom Patrol", "The Outsiders", "The Spectre", "The Question", "Hawkman", "Hawkgirl", "Booster Gold", "Blue Beetle", "Firestorm", "Plastic Man", "Zatanna", "Black Canary", "Vixen", "The Atom", "Doctor Fate", "Metamorpho", "The Metal Men", "The Creeper", "The Demon", "Sandman", "Starman", "Manhunter", "Fire", "Ice", "The Ray", "Steel", "Power Girl", "The Huntress", "The Phantom Stranger", "Ambush Bug", "Katana", "The Red Hood", "The Creeper", "Mister Miracle", "Big Barda", "The New Gods", "Orion", "Mister Miracle", "Infinity Inc.", "The Watchmen", "The Sandman", "Animal Man", "Swamp Thing", "Doom Patrol", "Global Guardians", "Secret Six", "The Warlord", "Jonah Hex", "Blackhawk", "Suicide Squad", "Stormwatch", "Challengers of the Unknown", "Young Justice", "The Power Company", "Vigilante", "The Freedom Fighters", "The Secret Society of Super-Villains", "The All-Star Squadron", "The Seven Soldiers of Victory", "Infinity Inc.", "The Metal Men", "The Doom Patrol", "The Outsiders"]

# Randomly select 5 series from each publisher
random_marvel_series = random.sample(marvel_series, 5)
random_dc_series = random.sample(dc_series, 5)

# Print the randomly selected series
print("Randomly Selected Marvel Series:")
for series in random_marvel_series:
    print(series)

print("\nRandomly Selected DC Series:")
for series in random_dc_series:
    print(series)
