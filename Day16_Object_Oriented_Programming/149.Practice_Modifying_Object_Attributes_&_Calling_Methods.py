from prettytable import PrettyTable

table=PrettyTable() # Create a table object
print(table) 
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])# Add a column to the table
table.add_column("Type",["Electric", "Water", "Fire"])
table.add_column("HP", [100, 100, 100])
table.align="l" # Align the table to the left using an attribute
print(table)