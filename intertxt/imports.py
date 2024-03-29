ARANGO_UN='root'
ARANGO_PW='passwd'

#print(__file__,'imported')
import os,sys
from pathlib import Path

TMP_CORPUS='tmp'
PATH_USER_HOME = str(Path.home())
PATH_HOME = os.path.join(PATH_USER_HOME,'intertxt')
PATH_DATA = os.path.join(PATH_HOME,'data')
PATH_CONFIG = os.path.join(PATH_HOME,'config')
PATH_CORPORA = os.path.join(PATH_HOME,'corpora')
TO_SCREEN = False
TO_FILE = True
RELSPACE_DEFAULT='is_also'
FROM_DEFAULT=['text']
TO_DEFAULT=['text']
MINHASH_KEYPREF=b'trWOR'



CORPUS_SOURCE_RANKS={
	'chadwyck':1,
	'hathi':4,
	'wikidata':7,
	'chicago':3,
	'markmark':2,
}


SERVERS=[
    # 'http://128.232.229.63:8529'
	# 'http://185.143.45.10:8529'
	'http://127.0.0.1:8529'
	# 'http://0.0.0.0:8529'
]
TEXT_COLLECTION_NAME='text'
FULL_TEXT_KEYS={'author','title'}

DATABASE='intertxt'
_ADB_ = None
_ADB_CLIENT = None
_ADB_SYSDB = None
VNUM='2023_01_28'
GRAPHNAME='_intertxt_'

COL_ID='id'
COL_ADDR='_addr'
COL_CORPUS='_corpus'
IDSEP_START='_'
IDSEP='/'
IDSEP_DB=')('
MATCHRELNAME='rdf:type'
DEFAULT_COMPAREBY=dict(author=0.9, title=0.9)#, year=1.0)

INIT_DB_WITH_CORPORA = {
	# 'bpo',
	'chadwyck',
	'chicago',
	'markmark',
	'txtlab',
	'tedjdh',
	'gildedage',
	# 'canon_fiction',
	'clmet',
	'dta',
	'dialnarr',
	'estc',
	'eebo_tcp',
	'ecco_tcp',
	'ecco',
	'evans_tcp',
	'litlab',
	# 'ravengarside',
	'semantic_cohort',
	'spectator'
}

OK_META_KEYS={
'_id',
'_key',
'_addr',
'_corpus',
'_au',
'_ti',
'_yr',
'id',
}




TEXT_CACHE={}
TMP_CORPUS='tmp'
CORPUS_CACHE={}
HASH_NUMPERM=128*2


### stdlib
from collections import Counter,defaultdict,UserList
import tempfile
from zipfile import BadZipFile
import shutil
import tempfile,sys,shutil,os,random


## external
import pandas as pd
import numpy as np
import networkx as nx
import humanize



## me
from intertxt.utils.logs import *
with Log('booting'):
	from intertxt.utils import *
	from intertxt.database import *
	from intertxt.texts import *
	from intertxt.corpora import *
	from intertxt.models import *

