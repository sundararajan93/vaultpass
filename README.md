# vaultpass
Vaultpass is a simple command line utility to vault your password and store it as encrypted text and retrieve when you needed.

Storing the password in plain-text file is terrible practice. We might face this similar scenario, when we need to store FTP/DB Server password.
Instead of storing the Plain-Text password to a file, we can encrypt the password and store it safely.
When the password is required, we could decrypt the password from the same utility.

### prerequisite:
1. python3
2. cryptograpy module
`$sudo pip3 install cryptography`

### Setup
Setting up the tool is very simple, just clone the repo and make the script file executable.
```
$git clone https://github.com/sundararajan93/vaultpass.git 
$cd vaultpass
$chmod +x vaultpass.py
```

### Help command
Make use of the help (-h, --help) tags to view the available options

```
$./vaultpass -h
usage: vaultpass.py [-h] [-e EN_CRYPT] [-d] [-k]

optional arguments:
  -h, --help            show this help message and exit
  -e EN_CRYPT, --en_crypt EN_CRYPT
                        Pass the text to encrypt as an argument
  -d, --de_crypt        Pass the text to decrypt as an argument
  -k, --key             Generate the 'secret.key' file
```

### Generating Key file (Important Initial Step)
The important initial step is to generate the 'secret.key' file.
we can generate the secret key with -k, --key tags like below

```
$./vaultpass.py -k
Key Generated -> b'R4nfsFJv85t1kuz7zfwitfT0Fo1stqGdeq8G6IiMVH0='
```
##### Warning: This 'secret.key' file is very important. If you lose this you will not able to decrypt the password

### Encrypt the password
To encrypt the password you need use -e, --en_crypt tags like the below. pass the text in single quotes ('Text')

```
$./vaultpass.py -e 'p@$$w0rD'
b'gAAAAABfVOzHVIEJJQ-12OtOkIZqHxg0R5BZDLNluPlZ0XFMheLGVAuY3K6XGapb4qv0qZeErRlF1pxm9NmDitis-wQSDieAsw=='
```
This encrypted password stored in a text file on the same location(encrypted.txt).
Which can later be used to retrieve the password when required.

### Decrypt the password
When you require the password you can decrypt using -d, --de_crypt

```
$./vaultpass.py -d
p@$$w0rD
```
This same retrieval steps can be added to your own script as per the requirement.

