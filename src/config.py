{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'config'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-bdb79589f775>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#!/usr/bin/python\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mconfigparser\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mConfigParser\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;31m#from config import config\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpsycopg2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'config'"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/python\n",
    "from configparser import ConfigParser\n",
    "from config import config\n",
    "import psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def config(filename='database.ini', section='postgresql'):\n",
    "    # create a parser\n",
    "    parser = ConfigParser()\n",
    "    # read config file\n",
    "    parser.read(filename)\n",
    " \n",
    "    # get section, default to postgresql\n",
    "    db = {}\n",
    "    if parser.has_section(section):\n",
    "        params = parser.items(section)\n",
    "        for param in params:\n",
    "            db[param[0]] = param[1]\n",
    "    else:\n",
    "        raise Exception('Section {0} not found in the {1} file'.format(section, filename))\n",
    "    \n",
    "    return db"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def connect():\n",
    "    # Connect to PostgreSQL database server\n",
    "    conn = None\n",
    "    try:\n",
    "        # Read connection parameters\n",
    "        params = config()\n",
    "        \n",
    "        # Connect to the PostgreSQL server\n",
    "        print(\"Connecting to the PostgreSQL database...\")\n",
    "        conn = psycopg2.connect(**params)\n",
    "        \n",
    "        # Create a cursor\n",
    "        cur = conn.cursor()\n",
    "    \n",
    "    # Execute a statement\n",
    "        print(\"PostgreSQL database version:\")\n",
    "        cur.execute(\"SELECT version()\")\n",
    "        \n",
    "        # Display the PostgreSQL database server version\n",
    "        db_version = cur.fetchone()\n",
    "        print(db_version)\n",
    "        \n",
    "        # Close the communication with the PostreSQL\n",
    "        cur.close()\n",
    "    \n",
    "    except(Exception, psycopg2.DatabaseError) as error:\n",
    "        print(error)\n",
    "    finally:\n",
    "        if conn is not None:\n",
    "            conn.close()\n",
    "            print(\"Database connection closed.\")\n",
    "\n",
    "if __name_ == '__main__':\n",
    "    connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/michelle/pipelines/pipeline/bin/python3'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sys\n",
    "sys.executable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['/Users/michelle/pipelines',\n",
       " '/anaconda3/lib/python37.zip',\n",
       " '/anaconda3/lib/python3.7',\n",
       " '/anaconda3/lib/python3.7/lib-dynload',\n",
       " '',\n",
       " '/Users/michelle/pipelines/pipeline/lib/python3.7/site-packages',\n",
       " '/Users/michelle/pipelines/pipeline/lib/python3.7/site-packages/IPython/extensions',\n",
       " '/Users/michelle/.ipython']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/michelle/pipelines'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Please wait a moment while I gather a list of all available modules...\n",
      "\n",
      "IPython             _warnings           hmac                runpy\n",
      "__future__          _weakref            html                sched\n",
      "_abc                _weakrefset         http                secrets\n",
      "_ast                _xxtestfuzz         idlelib             select\n",
      "_asyncio            abc                 imaplib             selectors\n",
      "_bisect             aifc                imghdr              setuptools\n",
      "_blake2             antigravity         imp                 shelve\n",
      "_bootlocale         appnope             importlib           shlex\n",
      "_bz2                argparse            inspect             shutil\n",
      "_codecs             array               io                  signal\n",
      "_codecs_cn          ast                 ipaddress           site\n",
      "_codecs_hk          asynchat            ipykernel           six\n",
      "_codecs_iso2022     asyncio             ipykernel_launcher  smtpd\n",
      "_codecs_jp          asyncore            ipython_genutils    smtplib\n",
      "_codecs_kr          atexit              itertools           sndhdr\n",
      "_codecs_tw          audioop             jedi                socket\n",
      "_collections        autoreload          json                socketserver\n",
      "_collections_abc    backcall            jupyter             sqlite3\n",
      "_compat_pickle      base64              jupyter_client      sre_compile\n",
      "_compression        bdb                 jupyter_core        sre_constants\n",
      "_contextvars        binascii            keyword             sre_parse\n",
      "_crypt              binhex              lib2to3             ssl\n",
      "_csv                bisect              linecache           stat\n",
      "_ctypes             builtins            locale              statistics\n",
      "_ctypes_test        bz2                 logging             storemagic\n",
      "_curses             cProfile            lzma                string\n",
      "_curses_panel       calendar            macpath             stringprep\n",
      "_datetime           cgi                 mailbox             struct\n",
      "_dbm                cgitb               mailcap             subprocess\n",
      "_decimal            chunk               marshal             sunau\n",
      "_dummy_thread       cmath               math                symbol\n",
      "_elementtree        cmd                 mimetypes           sympyprinting\n",
      "_functools          code                mmap                symtable\n",
      "_hashlib            codecs              modulefinder        sys\n",
      "_heapq              codeop              multiprocessing     sysconfig\n",
      "_imp                collections         netrc               syslog\n",
      "_io                 colorsys            nis                 tabnanny\n",
      "_json               compileall          nntplib             tarfile\n",
      "_locale             concurrent          ntpath              telnetlib\n",
      "_lsprof             configparser        nturl2path          tempfile\n",
      "_lzma               contextlib          numbers             termios\n",
      "_markupbase         contextvars         opcode              test\n",
      "_md5                copy                operator            tests\n",
      "_multibytecodec     copyreg             optparse            textwrap\n",
      "_multiprocessing    crypt               os                  this\n",
      "_opcode             csv                 parser              threading\n",
      "_operator           ctypes              parso               time\n",
      "_osx_support        curses              pathlib             timeit\n",
      "_pickle             cythonmagic         pdb                 tkinter\n",
      "_posixsubprocess    dataclasses         pexpect             token\n",
      "_py_abc             datetime            pickle              tokenize\n",
      "_pydecimal          dateutil            pickleshare         tornado\n",
      "_pyio               dbm                 pickletools         trace\n",
      "_queue              decimal             pip                 traceback\n",
      "_random             decorator           pipes               tracemalloc\n",
      "_scproxy            difflib             pkg_resources       traitlets\n",
      "_sha1               dis                 pkgutil             tty\n",
      "_sha256             distutils           platform            turtle\n",
      "_sha3               doctest             plistlib            turtledemo\n",
      "_sha512             dummy_threading     poplib              types\n",
      "_signal             easy_install        posix               typing\n",
      "_sitebuiltins       email               posixpath           unicodedata\n",
      "_socket             encodings           pprint              unittest\n",
      "_sqlite3            ensurepip           profile             urllib\n",
      "_sre                enum                prompt_toolkit      uu\n",
      "_ssl                errno               pstats              uuid\n",
      "_stat               faulthandler        psycopg2            venv\n",
      "_string             fcntl               pty                 warnings\n",
      "_strptime           filecmp             ptyprocess          wave\n",
      "_struct             fileinput           pwd                 wcwidth\n",
      "_symtable           fnmatch             py_compile          weakref\n",
      "_sysconfigdata_i686_conda_cos6_linux_gnu formatter           pyclbr              webbrowser\n",
      "_sysconfigdata_m_darwin_darwin fractions           pydoc               wsgiref\n",
      "_sysconfigdata_powerpc64le_conda_cos7_linux_gnu ftplib              pydoc_data          xdrlib\n",
      "_sysconfigdata_x86_64_apple_darwin13_4_0 functools           pyexpat             xml\n",
      "_sysconfigdata_x86_64_conda_cos6_linux_gnu gc                  pygments            xmlrpc\n",
      "_testbuffer         genericpath         queue               xxlimited\n",
      "_testcapi           getopt              quopri              xxsubtype\n",
      "_testimportmultiple getpass             random              zipapp\n",
      "_testmultiphase     gettext             re                  zipfile\n",
      "_thread             glob                readline            zipimport\n",
      "_threading_local    grp                 reprlib             zlib\n",
      "_tkinter            gzip                resource            zmq\n",
      "_tracemalloc        hashlib             rlcompleter         \n",
      "_uuid               heapq               rmagic              \n",
      "\n",
      "Enter any module name to get more help.  Or, type \"modules spam\" to search\n",
      "for modules whose name or summary contain the string \"spam\".\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(\"modules\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "pipelines",
   "language": "python",
   "name": "pipelines"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
