from typing import NamedTuple

from plenum.common.constants import TXN_TYPE, TARGET_NYM, ORIGIN, DATA, RAW, ENC, HASH, NAME, VERSION, TYPE, \
    POOL_TXN_TYPES, ALIAS, \
    VERKEY
from sovrin_common.roles import Roles
from sovrin_common.transactions import SovrinTransactions

Environment = NamedTuple("Environment", [
    ("poolLedger", str),
    ("domainLedger", str)
])

ROLE = 'role'
NONCE = 'nonce'
ATTRIBUTES = "attributes"
ATTR_NAMES = "attr_names"
ACTION = 'action'
SCHEDULE = 'schedule'
TIMEOUT = 'timeout'
SHA256 = 'sha256'
START = 'start'
CANCEL = 'cancel'
COMPLETE = 'complete'
FAIL = 'fail'
JUSTIFICATION = 'justification'

NULL = 'null'
OWNER = '<owner>'

LAST_TXN = "lastTxn"
TXNS = "Txns"

ENC_TYPE = "encType"
SKEY = "secretKey"
REF = "ref"
PRIMARY = "primary"
REVOCATION = "revocation"

allOpKeys = (TXN_TYPE, TARGET_NYM, VERKEY, ORIGIN, ROLE, DATA, NONCE, REF, RAW,
             ENC, HASH, ALIAS, ACTION, SCHEDULE, TIMEOUT, SHA256, START, CANCEL,
             NAME, VERSION, JUSTIFICATION)

reqOpKeys = (TXN_TYPE,)

# Attribute Names
ENDPOINT = "endpoint"

# Roles
TRUST_ANCHOR = Roles.TRUST_ANCHOR.value
TGB = Roles.TGB.value

# client transaction types
NODE = SovrinTransactions.NODE.value
NYM = SovrinTransactions.NYM.value
ATTRIB = SovrinTransactions.ATTRIB.value
SCHEMA = SovrinTransactions.SCHEMA.value
ISSUER_KEY = SovrinTransactions.ISSUER_KEY.value
DISCLO = SovrinTransactions.DISCLO.value
GET_ATTR = SovrinTransactions.GET_ATTR.value
GET_NYM = SovrinTransactions.GET_NYM.value
GET_TXNS = SovrinTransactions.GET_TXNS.value
GET_SCHEMA = SovrinTransactions.GET_SCHEMA.value
GET_ISSUER_KEY = SovrinTransactions.GET_ISSUER_KEY.value

POOL_UPGRADE = SovrinTransactions.POOL_UPGRADE.value
NODE_UPGRADE = SovrinTransactions.NODE_UPGRADE.value

openTxns = (GET_NYM, GET_ATTR, GET_SCHEMA, GET_ISSUER_KEY)

# TXN_TYPE -> (requireds, optionals)
fields = {NYM: ([TARGET_NYM], [ROLE]),
          ATTRIB: ([], [RAW, ENC, HASH]),
          SCHEMA: ([NAME, VERSION, ATTR_NAMES], [TYPE, ]),
          GET_SCHEMA: ([], []),
          ISSUER_KEY: ([REF, DATA]),
          GET_ISSUER_KEY: ([REF, ORIGIN])
          }

CONFIG_TXN_TYPES = {POOL_UPGRADE, NODE_UPGRADE}
IDENTITY_TXN_TYPES = {NYM,
                      ATTRIB,
                      DISCLO,
                      GET_ATTR,
                      GET_NYM,
                      GET_TXNS,
                      SCHEMA,
                      GET_SCHEMA,
                      ISSUER_KEY,
                      GET_ISSUER_KEY}

validTxnTypes = set()
validTxnTypes.update(POOL_TXN_TYPES)
validTxnTypes.update(IDENTITY_TXN_TYPES)
validTxnTypes.update(CONFIG_TXN_TYPES)
