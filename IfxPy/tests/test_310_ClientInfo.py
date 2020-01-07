# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_310_ClientInfo(self):
    obj = IfxPyTestFunctions()
    obj.assert_expectf(self.run_test_310)

  def run_test_310(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    client = IfxPy.client_info(conn)
    
    if client:
      print("DRIVER_NAME: string(%d) \"%s\"" % (len(client.DRIVER_NAME), client.DRIVER_NAME))
      print("DRIVER_VER: string(%d) \"%s\"" % (len(client.DRIVER_VER), client.DRIVER_VER))
      print("DATA_SOURCE_NAME: string(%d) \"%s\"" % (len(client.DATA_SOURCE_NAME), client.DATA_SOURCE_NAME))
      print("DRIVER_ODBC_VER: string(%d) \"%s\"" % (len(client.DRIVER_ODBC_VER), client.DRIVER_ODBC_VER))
      print("ODBC_VER: string(%d) \"%s\"" % (len(client.ODBC_VER), client.ODBC_VER))
      print("ODBC_SQL_CONFORMANCE: string(%d) \"%s\"" % (len(client.ODBC_SQL_CONFORMANCE), client.ODBC_SQL_CONFORMANCE))
    
      IfxPy.close(conn)
    else:
      print("Error.")

#__END__
#__LUW_EXPECTED__
#DRIVER_NAME: string(%d) %s
#DRIVER_VER: string(%d) %s
#DATA_SOURCE_NAME: string(%d) %s
#DRIVER_ODBC_VER: string(%d) %s
#ODBC_VER: string(%d) %s
#ODBC_SQL_CONFORMANCE: string(%d) %s
#APPL_CODEPAGE: int(%d)
#CONN_CODEPAGE: int(%d)
#__ZOS_EXPECTED__
#DRIVER_NAME: string(%d) %s
#DRIVER_VER: string(%d) %s
#DATA_SOURCE_NAME: string(%d) %s
#DRIVER_ODBC_VER: string(%d) %s
#ODBC_VER: string(%d) %s
#ODBC_SQL_CONFORMANCE: string(%d) %s
#APPL_CODEPAGE: int(%d)
#CONN_CODEPAGE: int(%d)
#__SYSTEMI_EXPECTED__
#DRIVER_NAME: string(%d) %s
#DRIVER_VER: string(%d) %s
#DATA_SOURCE_NAME: string(%d) %s
#DRIVER_ODBC_VER: string(%d) %s
#ODBC_VER: string(%d) %s
#ODBC_SQL_CONFORMANCE: string(%d) %s
#APPL_CODEPAGE: int(%d)
#CONN_CODEPAGE: int(%d)
#__IDS_EXPECTED__
#DRIVER_NAME: string(%d) %s
#DRIVER_VER: string(%d) %s
#DATA_SOURCE_NAME: string(%d) %s
#DRIVER_ODBC_VER: string(%d) %s
#ODBC_VER: string(%d) %s
#ODBC_SQL_CONFORMANCE: string(%d) %s