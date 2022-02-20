"""Main file for Nextpass runtime"""

from dotenv import load_dotenv
from getpass import getpass
from internal import Internal
import os

load_dotenv()
internal = Internal(getpass('Enter your master password: '), os.getenv('TOKEN'), os.getenv('SERVER'))
# Clear passwords in database.
# internal.clear()
# Delete specific website password
# internal.delete('a', 'a')
# Add a website password
# internal.add_item('a', 'a', 'a', 'b', 'c', 'd')
print(internal.search('a', 'website', False))
internal.close()