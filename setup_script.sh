#!/bin/bash

# Foundational Tier
# 1. Create 3 directories: Development, Operations, Analytics
mkdir Development Operations Analytics

# 2. Add several blank dummy files to each directory
touch Development/file1.txt Development/file2.txt
touch Operations/file1.txt Operations/file2.txt
touch Analytics/file1.txt Analytics/file2.txt

# 3. Create 3 Groups in Linux: Developers, Operations, Data Analysts
sudo addgroup --force-badname Developers
sudo addgroup --force-badname Operations
sudo addgroup --force-badname "Data_Analysts"

# 4. Change ownership of directories to their respective groups
sudo chown :Developers Development
sudo chown :Operations Operations
sudo chown :"Data_Analysts" Analytics

# 5. Modify permissions to allow only group members to read, write, and execute
sudo chmod 770 Development
sudo chmod 770 Operations
sudo chmod 770 Analytics

# Copy directories to each user home directory
sudo cp -rp /home/ubuntu/Development /home/jewart
sudo cp -rp /home/ubuntu/Operations /home/jewart
sudo cp -rp /home/ubuntu/Analytics /home/jewart
sudo cp -rp /home/ubuntu/Development /home/bdorsey
sudo cp -rp /home/ubuntu/Operations /home/bdorsey
sudo cp -rp /home/ubuntu/Analytics /home/bdorsey
sudo cp -rp /home/ubuntu/Development /home/jwaller
sudo cp -rp /home/ubuntu/Operations /home/jwaller
sudo cp -rp /home/ubuntu/Analytics /home/jwaller

# Create users and add them to respective groups
sudo adduser jwaller --ingroup Developers --gecos "Jess Waller,,,jwaller@levelupbank.com"
sudo adduser bdorsey --ingroup Operations --gecos "Blake Dorsey,,,bdorsey@levelupbank.com"
sudo adduser jewart --ingroup "Data_Analysts" --gecos "Joey Ewart,,,jewart@levelupbank.com"

# Advanced Tier
# 1. Set permissions so that users can only view their own profile
sudo chmod 700 /home/jwaller
sudo chmod 700 /home/bdorsey
sudo chmod 700 /home/jewart

# Verification
# 2. Verify that each user can only view their own profile
echo "Verifying access to home directories:"
echo "-------------------------------------"
echo "For jwaller:"
su - jwaller -c 'ls ~'
su - jwaller -c 'ls ~bdorsey'
su - jwaller -c 'ls ~jewart'

echo "For bdorsey:"
su - bdorsey -c 'ls ~'
su - bdorsey -c 'ls ~jwaller'
su - bdorsey -c 'ls ~jewart'

echo "For jewart:"
su - jewart -c 'ls ~'
su - jewart -c 'ls ~jwaller'
su - jewart -c 'ls ~bdorsey'
