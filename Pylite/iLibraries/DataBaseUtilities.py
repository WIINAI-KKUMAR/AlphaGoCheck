
import cx_Oracle as cx
import pandas as pd

def connect_db_fetch(user_name,password,host_name,port,db_name,sql):
    db_export_excel = r"C:\Users\vinaykumar_puppala\Desktop\TEST_1_FILE.xlsx"
    sheetname="sheet1"

    CONN_STR = "".join([user_name + '/' + password + '@' + host_name + ':' + port + '/' + db_name])
    Connection = cx.connect(CONN_STR)
    cursor    = Connection.cursor()
    #listVal=[]
    cursor.execute(sql)
    clumn = []
    for FieldName in cursor.description:
        clumn.append(FieldName[0])
        #print(FieldName[0])
    #print(clumn)
    df =pd.DataFrame(cursor.fetchall(),columns=clumn)
    cursor.close()
    Connection.close()
    #print(df.index)
    #print(df.dtypes)
    df.to_excel(db_export_excel,sheet_name=sheetname)
    return df