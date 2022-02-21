import sqlite3
import bcrypt
from FileAES import FileAES
import pyscrypt
import requests
import hashlib
import socket
import os
import secrets
import shutil
import pwnedpasswords
import json

class Internal():
    """Internal manage for nextpass. Basically handles the database and encrypted backups for Nextpass."""
    sqlite_connection = None
    sqlite_cursor = None
    loaded_pwds = []
    pwdHash = None
    pwd = None
    salt = b''
    fileaes = FileAES()
    token = None
    server_url = ''
    def __init__(self, password: str, token: str, server: str) -> None:
        self.server_url = server
        self.token = token
        self.fileaes.set_key(pyscrypt.hash(password.encode(), self.load_salt(), 16, 8, 1, 32))
        if (os.path.exists('pwd.db') and os.path.exists('PWD_DB_HASH.DBHASH') and os.path.exists('SALT_PWD.HASH')):
            if (self.internet()):
                if (not (self.validate())):
                    raise ValueError('Not a valid token.')
                else:
                    pass
            else:
                pass
            self.decrypt_db()
        else:
            if (self.internet()):
                if (self.validate()):
                    topassHeaders = { 'Authorization': json.dumps({ 'token': self.token }) }
                    if (Internal.is_downloadable(f'{self.server_url}/api/nextpass/db', headers=topassHeaders) and Internal.is_downloadable(f'{self.server_url}/api/nextpass/db/hash', headers=topassHeaders) and Internal.is_downloadable(f'{self.server_url}/api/nextpass/pwd/salt', headers=topassHeaders)):
                        self.download(f'{self.server_url}/api/nextpass/db', topassHeaders, 'pwd.db')
                        self.download(f'{self.server_url}/api/nextpass/db/hash', topassHeaders, 'PWD_DB_HASH.DBHASH')
                        self.download(f'{self.server_url}/api/nextpass/pwd/salt', topassHeaders, 'SALT_PWD.HASH')
                    else:
                        pass
                else:
                    raise ValueError('Not a valid token.')
            else:
                pass
        self.sqlite_connection = sqlite3.connect('pwd.db')
        self.sqlite_cursor = self.sqlite_connection.cursor()
        self.pwdHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
        self.sqlite_cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (
            website text,
            name text,
            idHash text,
            emailHash text,
            idEncrypted text,
            emailEncrypted text,
            passwordEncrypted text,
            secret2faEncrypted text,
            notes text
            )""")
        
        self.sqlite_cursor.execute("""CREATE TABLE IF NOT EXISTS salts (
            salt blob
        )""")

        if (self.sqlite_cursor.execute("SELECT * FROM salts").fetchone()):
            self.salt = self.sqlite_cursor.execute("SELECT * FROM salts").fetchone()[0]
        else:
            self.salt = bcrypt.gensalt(12)
            self.sqlite_cursor.execute("INSERT INTO salts VALUES (?)", (self.salt,))
    
    def internet(self, host="8.8.8.8", port=53, timeout=3) -> bool:
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
        except socket.error as ex:
            s.close()
            return False
        
        s.close()
        return True

    def id(self):
        charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        gened_id = ''
        for i in range(4):
            for j in range(4):
                gened_id += secrets.choice(charset)
            gened_id += '-'
        
        gened_id = list(gened_id)
        gened_id.pop()
        gened_id = "".join(gened_id)
        return gened_id

    def add_item(self, website: str, name: str, email: str, password: str, secret2fa = "", notes = "") -> int:
        hashedEmail = bcrypt.hashpw(email.encode(), self.salt)
        ida = self.id()
        hashedId = bcrypt.hashpw(ida.encode(), self.salt)
        encryptedId = self.fileaes.encrypt_text(ida)
        querysql2 = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE website LIKE ? AND emailHash LIKE ?", (website, hashedEmail,)).fetchone()
        if (querysql2):
            self.close()
            raise ValueError('Value already exists.')
        encryptedEmail = self.fileaes.encrypt_text(email)
        encryptedPassword = self.fileaes.encrypt_text(password)
        encrypted2fasecret = self.fileaes.encrypt_text(secret2fa)
        encryptedNotes = self.fileaes.encrypt_text(notes)
        # self.loaded_pwds.append({
        #     'website': website,
        #     'name': name,
        #     'idHash': hashedId,
        #     'emailHash': hashedEmail,
        #     'emailEncryted': encryptedEmail,
        #     'passwordEncrypted': encryptedPassword,
        #     'secret2faEncrypted': encrypted2fasecret,
        #     'notes': encryptedNotes
        # })

        querysql = self.sqlite_cursor.execute("INSERT INTO passwords VALUES (?,?,?,?,?,?,?,?,?)", (website, name, hashedId, hashedEmail, encryptedId, encryptedEmail, encryptedPassword, encrypted2fasecret, encryptedNotes,))
        return 0
    
    def generatePassword(self, length: int, punctuation = True, digits = True) -> str:
        return self.fileaes.generatePassword(length, punctuation, digits)
    
    def passwordStrength(self, password: str) -> str:
        return self.fileaes.password_strength(password)

    def passwordCheck(self, website: str, email: str) -> str:
        return self.passwordStrength(self.fileaes.decrypt_text(self.search_email(website, email, plural=False)[5]))

    def search_email(self, website: str, email: str, plural=True, limit=100) -> list or tuple:
        querysql = None
        if plural:
            querysql = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE emailHash LIKE ? AND website LIKE ?", (bcrypt.hashpw(email.encode(), self.salt), website,))
            return self.decrypt_data(querysql.fetchmany(limit))
        else:
            querysql = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE emailHash LIKE ? AND website LIKE ?", (bcrypt.hashpw(email.encode(), self.salt), website,))
            return self.decrypt_datum(querysql.fetchone()) or []

    def search_name(self, website: str, name: str, plural=True, limit=100) -> list or tuple:
        querysql = None
        if plural:
            querysql = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE name LIKE ? AND website LIKE ?", (name, website,))
            return self.decrypt_data(querysql.fetchmany(limit))
        else:
            querysql = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE name LIKE ? AND website LIKE ?", (name, website,))
            return self.decrypt_datum(querysql.fetchone()) or []

    def delete(self, website: str, email: str) -> None:
        querysql = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE website LIKE ? AND emailHash LIKE ?", (website, bcrypt.hashpw(email.encode(), self.salt),)).fetchone()
        if (querysql):
            self.sqlite_cursor.execute("DELETE FROM passwords WHERE website LIKE ? AND emailHash LIKE ?", (website, bcrypt.hashpw(email.encode(), self.salt),))
        else:
            self.close()
            raise ValueError('Can\'t delete a non-existant item.')

    def search(self, website: str, value: str, type: str, plural=True, limit=100) -> list or tuple:
        formated = {
            'name': self.search_name,
            'email': self.search_email
        }

        if (formated.get(type)):
            return formated.get(type)(website, value, plural, limit)
        else:
            self.close()
            raise ValueError('Not a valid search query type. Please select either email, name, or website.')

    def fetch_all(self) -> list
        return self.decrypt_data(self.sqlite_cursor.execute("SELECT * FROM passwords").fetchall()) or []

    def clear_mem(self) -> None:
        self.loaded_pwds.clear()

    def clear(self) -> None:
        self.clear_mem()
        self.sqlite_cursor.execute("DELETE FROM passwords;")

    def encrypt_db(self) -> None:
        self.fileaes.encrypt_file('pwd.db')
        os.rename('pwd.db.encrypted', 'pwd.db')

    def decrypt_db(self) -> None:
        try:
            shutil.copyfile('pwd.db', '$3pwd.db.tmp')
            os.rename('pwd.db', 'pwd.db.encrypted')
            self.fileaes.decrypt_file('pwd.db')
        except:
            raise ValueError('Not the correct password.')
        res = False
        with open(f'pwd.db', 'rb') as f:
            with open(f'PWD_DB_HASH.DBHASH', 'rb') as f1:
                res = hashlib.sha512(f.read()).digest() == f1.read()
                f1.close()
            f.close()
        
        if res:
            os.remove('$3pwd.db.tmp')
        else:
            shutil.copyfile('$3pwd.db.tmp', 'pwd.db')
            os.remove('$3pwd.db.tmp')
            raise ValueError('Not the correct password.')

    def edit(self, id: str, **toset) -> None:
        querysql = self.sqlite_cursor.execute("SELECT * FROM passwords WHERE idHash LIKE ?", (bcrypt.hashpw(id.encode(), self.salt).decode(),)).fetchone()
        # do not modify that
        if (querysql):
            sql_pre = "UPDATE passwords SET "
            tostr = ''
            how_much = []
            sql_vars = []
            allowed_to_modify = ['website', 'name', 'id', 'email', 'password', 'secret2fa', 'notes']
            toset_items = list(toset.items())
            for i in range(len(toset_items)):
                if (not (isinstance(toset_items[i][1], str))):
                    pass
                else:
                    if (toset_items[i][0].lower() == 'email'):
                        if (len(how_much) > 0):
                            tostr += ', '
                        how_much.append('email')
                        how_much.append('emailHash')
                        
                        tostr += 'emailHash = '
                        sql_vars.append(bcrypt.hashpw(toset_items[i][1].encode(), self.salt).decode())
                        sql_vars.append(self.fileaes.encrypt_text(toset_items[i][1]))
                        tostr += '?'
                        tostr += ', '
                        tostr += 'emailEncrypted = '
                        tostr += '?'
                    elif (toset_items[i][0].lower() == 'password'):
                        if (len(how_much) > 0):
                            tostr += ', '
                        how_much.append('passwordEncrypted')

                        tostr += 'passwordEncrypted = '
                        sql_vars.append(self.fileaes.encrypt_text(toset_items[i][1]))
                        tostr += '?'
                    elif (toset_items[i][0].lower() == 'secret2fa'):
                        if (len(how_much) > 0):
                            tostr += ', '
                        how_much.append('secret2faEncrypted')

                        tostr += 'secret2faEncrypted = '
                        sql_vars.append(self.fileaes.encrypt_text(toset_items[i][1]))
                        tostr += '?'
                    elif (toset_items[i][0].lower() == 'notes'):
                        if (len(how_much) > 0):
                            tostr += ', '
                        how_much.append('notes')

                        tostr += 'notes = '
                        sql_vars.append(self.fileaes.encrypt_text(toset_items[i][1]))
                        tostr += '?'
                    elif (toset_items[i][0].lower() == 'website'):
                        if (len(how_much) > 0):
                            tostr += ', '
                        how_much.append('website')

                        tostr += 'website = '
                        sql_vars.append(toset_items[i][1])
                        tostr += '?'
                    elif (toset_items[i][0].lower() == 'name'):
                        if (len(how_much) > 0):
                            tostr += ', '
                        how_much.append('name')

                        tostr += 'name = '
                        sql_vars.append(toset_items[i][1])
                        tostr += '?'
            sql_pre += tostr
            sql_vars.append(bcrypt.hashpw(id.encode(), self.salt))
            sql_pre += ' WHERE idHash = ' + '?'
            querysql2 = self.sqlite_cursor.execute(sql_pre, tuple(sql_vars))
        else:
            self.close()
            raise ValueError('Not a valid id to edit.')

    def load_salt(self) -> bytes:
        if (os.path.exists('SALT_PWD.HASH')):
            data = b''
            with open(f'SALT_PWD.HASH', 'rb') as f:
                data = f.read()
                f.close()
            return data
        else:
            return self.generate_salt()

    def generate_salt(self) -> bytes:
        randomg = os.urandom(32)
        with open(f'SALT_PWD.HASH', 'wb') as f:
            f.write(randomg)
            f.close()
        return randomg

    def validate(self) -> bool:
        res = requests.post(f'{self.server_url}/api/validate', data={ 'token': self.token })
        if (res.ok):
            return True
        else:
            return False

    def decrypt_data(self, data: list) -> list:
        try:
            new_list = []
            for i in range(len(data)):
                new_list.append(self.decrypt_datum(data[i]))
        except:
            return []
        
        return new_list

    def decrypt_datum(self, data_tuple: tuple) -> tuple:
        try:
            if len(data_tuple) != 9:
                self.close()
                raise ValueError('Not a valid tuple')
            data = list(data_tuple)[4:]
            new_data = list(data_tuple)[:2]
            new_data.append(list(data_tuple)[2])
            new_data.append(list(data_tuple)[3])
            for i in range(len(data)):
                new_data.append(self.fileaes.decrypt_text(data[i]))
        except:
            return []
        
        return new_data

    def download(self, url, headers, local_filename: str) -> str:
        with requests.get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename

    def upload(self, server, headers, fileobj: dict) -> int:
        res = requests.patch(server, headers=headers, files=fileobj)
        if (res.ok):
            return res.status_code
        else:
            return res.status_code

    @staticmethod
    def is_downloadable(url, headers) -> bool:
        h = requests.head(url, allow_redirects=True, headers=headers)
        header = h.headers
        content_type = header.get('content-type')
        if 'text' in content_type.lower():
            return False
        if 'html' in content_type.lower():
            return False
        return True

    def getHash(self) -> None:
        with open(f'pwd.db', 'rb') as f:
            with open(f'PWD_DB_HASH.DBHASH', 'wb') as f1:
                f1.write(hashlib.sha512(f.read()).digest())
                f1.close()
            f.close()

    def close(self) -> None:
        self.sqlite_connection.commit()
        self.sqlite_connection.close()
        self.getHash()
        self.encrypt_db()
        if (self.internet()):
            if (self.validate()):
                self.upload(f'{self.server_url}/api/nextpass/db', { 'Authorization': json.dumps({ 'token': self.token }) }, { 'pwd': open(f'pwd.db', 'rb') })
                self.upload(f'{self.server_url}/api/nextpass/db/hash', { 'Authorization': json.dumps({ 'token': self.token }) }, { 'pwdhash': open(f'PWD_DB_HASH.DBHASH', 'rb') })
                self.upload(f'{self.server_url}/api/nextpass/pwd/salt', { 'Authorization': json.dumps({ 'token': self.token }) }, { 'hash': open(f'SALT_PWD.HASH', 'rb') })
            else:
                raise ValueError('Not a valid token.')
        else:
            pass