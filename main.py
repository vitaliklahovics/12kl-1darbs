
# Izveido failus 'admin.txt' un 'guest.txt' un ieraksta tajos lietotāja datus

# Izveidot 'admin.txt' failu ar administratora datiem
with open('admin.txt', 'w') as admin_file:
    admin_file.write("---------------------------\n")
    admin_file.write("|         Admins          |\n")
    admin_file.write("---------------------------\n\n")
    
    admin_file.write("Vārds: Admin0\n")
    admin_file.write("Uzvārds: Adminovs0\n")
    admin_file.write("Loma: Admin\n")
    admin_file.write("Vecums: 22\n\n")

    admin_file.write("Vārds: Admin1\n")
    admin_file.write("Uzvārds: Adminovs1\n")
    admin_file.write("Loma: Admin\n")
    admin_file.write("Vecums: 20\n\n")

    admin_file.write("Vārds: Admin2\n")
    admin_file.write("Uzvārds: Adminovs2\n")
    admin_file.write("Loma: Admin\n")
    admin_file.write("Vecums: 18\n\n")

    admin_file.write("Vārds: Admin3\n")
    admin_file.write("Uzvārds: Adminovs3\n")
    admin_file.write("Loma: Admin\n")
    admin_file.write("Vecums: 28\n\n")

    admin_file.write("Vārds: Admin4\n")
    admin_file.write("Uzvārds: Adminovs4\n")
    admin_file.write("Loma: Admin\n")
    admin_file.write("Vecums: 34\n\n")
    

# Izveidojiet 'guest.txt' failu ar viesu datiem
with open('guest.txt', 'w') as guest_file:
    guest_file.write("---------------------------\n")
    guest_file.write("|          Viesi          |\n")
    guest_file.write("---------------------------\n\n")
    
    guest_file.write("Vārds: Viesis0\n")
    guest_file.write("Uzvārds: Viesitis0\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 25\n\n")

    guest_file.write("Vārds: Viesis1\n")
    guest_file.write("Uzvārds: Viesitis1\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 35\n\n")

    guest_file.write("Vārds: Viesis2\n")
    guest_file.write("Uzvārds: Viesitis2\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 45\n\n")

    guest_file.write("Vārds: Viesis3\n")
    guest_file.write("Uzvārds: Viesitis3\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 47\n\n")

    guest_file.write("Vārds: Viesis4\n")
    guest_file.write("Uzvārds: Viesitis4\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 15\n\n")

    guest_file.write("Vārds: Viesis5\n")
    guest_file.write("Uzvārds: Viesitis5\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 56\n\n")

    guest_file.write("Vārds: Viesis6\n")
    guest_file.write("Uzvārds: Viesitis6\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 32\n\n")

    guest_file.write("Vārds: Viesis7\n")
    guest_file.write("Uzvārds: Viesitis7\n")
    guest_file.write("Loma: Viesis\n")
    guest_file.write("Vecums: 68\n\n")

# nolasa datus no 'admin.txt' un 'guest.txt' failiem un apvieno tos vienā failā
combined_data = []
with open('admin.txt', 'r') as admin_file:
    admin_data = admin_file.readlines()
    combined_data.extend(admin_data)

with open('guest.txt', 'r') as guest_file:
    guest_data = guest_file.readlines()
    combined_data.extend(guest_data)

# Izveidojiet sarakstus, lai saglabātu administratoru un viesu vecumu
admin_ages = []

# Datu analīze un administratoru vecuma noteikšana
is_admin = False
for line in combined_data:
    if line.startswith("Loma: Admin"):
        is_admin = True
    elif line.startswith("Loma:"):
        is_admin = False
    if is_admin and line.startswith("Vecums:"):
        age = int(line.split(":")[1].strip())
        admin_ages.append(age)

# Apvienoto datu saglabāšana failā 'combined.txt'
with open('combined.txt', 'w') as combined_file:
    combined_file.writelines(combined_data)

# Apvienoto datu drukāšana
with open('combined.txt', 'r') as combined_file:
    print(combined_file.read())

# Aprēķina administratoru, vecākā un jaunākā administratora vidējo vecumu.
average_admin_age = sum(admin_ages) / len(admin_ages)
oldest_admin_age = max(admin_ages)
youngest_admin_age = min(admin_ages)

print(f"---------------------------")
print(f"|        Atbildes         |")
print(f"---------------------------\n")

print(f"Administratoru vidējais vecums: {average_admin_age}")
print(f"Vecākais administrators: {oldest_admin_age}")
print(f"Jaunākais administrators: {youngest_admin_age}")

# Administratoru un viesu skaita skaitīšana apvienotajā failā
admin_count = combined_data.count("Loma: Admin\n")
guest_count = combined_data.count("Loma: Viesis\n")

print(f"Administratoru skaits: {admin_count}")
print(f"Viesu skaits: {guest_count}")
