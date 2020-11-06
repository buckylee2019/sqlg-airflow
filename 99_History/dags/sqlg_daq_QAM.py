﻿
# -*- coding: utf-8 -*-
# Author        : Jesse Wei
# LastUpdate    : 2020/11/04
# Impact        : DAG generated by SQLG
# Message       : Humanity towards others, we live by sharing. Fear can hold you prisoner, only hope can set you free.

# from __future__ import print_function
import logging
import airflow
from datetime import datetime, timedelta
from airflow.operators.sensors import ExternalTaskSensor
from airflow.operators.python_operator import PythonOperator
from airflow import models
from airflow.models import Variable
# import sqlg_jobs 
import sqlg_jobs_
			

#from acme.operators.dwh_operators import PostgresOperatorWithTemplatedParams

def f_SYS_STS_STG():
    logging.info('Control flow: STAGE status ')

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),
    'provide_context': True
}

tmpl_search_path = Variable.get("sql_path")

my_taskid = 'SYS_STS_STG'
D_STG_INIT = airflow.DAG(
    'D_STG_INIT',
    schedule_interval=timedelta(1),
    default_args=args,
    template_searchpath=tmpl_search_path,    
    max_active_runs=1)

SYS_STS_STG = PythonOperator(task_id=my_taskid,
                    python_callable=f_SYS_STS_STG,
                    provide_context=False,
                    dag=D_STG_INIT)

my_taskid = 'D_STG_INITxSYS_STS_STG'                    
D_STG_INITxSYS_STS_STG = ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id='D_STG_INIT',
    external_task_id='SYS_STS_STG',
    execution_delta=None,  # Same day as today
    )

# Flow dag    
# DB_NAME = 'DWH'    
D_ODS_QAM = airflow.DAG(    "D_ODS_QAM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_DM_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs.HISTORYCARD.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.HISTORYCARD)

sqlg_jobs.PN_SPC.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.PN_SPC)

sqlg_jobs.SUB_SPC.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.SUB_SPC)

sqlg_jobs.RWK_GLOBAL_LOT_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.RWK_GLOBAL_LOT_WS1)

sqlg_jobs.RWK_GLOBAL_LOT_DETAIL_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.RWK_GLOBAL_LOT_DETAIL_WS1)

sqlg_jobs.INSTRUMENT_CORRECT_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.INSTRUMENT_CORRECT_NQJ)

sqlg_jobs.INSTRUMENT_INFO_CORRECT_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.INSTRUMENT_INFO_CORRECT_NQJ)

sqlg_jobs.MV_MTL_CROSS_REFERENCES_V.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_MTL_CROSS_REFERENCES_V)

sqlg_jobs.XX_ERP_ITEM.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.XX_ERP_ITEM)

sqlg_jobs.ERPIQC.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ERPIQC)

sqlg_jobs.ERFORM_DOC_MSG_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ERFORM_DOC_MSG_WS1)

sqlg_jobs.EF_QCEXCEPTION_MST_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.EF_QCEXCEPTION_MST_WS1)

sqlg_jobs.PN_MODULE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.PN_MODULE)

sqlg_jobs.PN_MODULE_MAINTAIN.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.PN_MODULE_MAINTAIN)

sqlg_jobs.SPC_ABNORMAL.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.SPC_ABNORMAL)

sqlg_jobs.COPQ_FCTACTUALCOST.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.COPQ_FCTACTUALCOST)

sqlg_jobs.MTL_MATERIAL_TRANSACTIONS.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MTL_MATERIAL_TRANSACTIONS)

sqlg_jobs.COPQ_DIMCATEGORY.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.COPQ_DIMCATEGORY)

sqlg_jobs.BI_DIMMULTIORG.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.BI_DIMMULTIORG)

sqlg_jobs.MV_ORG_ORGANIZATION_DEF.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_ORG_ORGANIZATION_DEF)

sqlg_jobs.ERDRLRR_INSPECTION_HEADER_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ERDRLRR_INSPECTION_HEADER_WS1)

sqlg_jobs.MV_GL_SETS_OF_BOOKS.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_GL_SETS_OF_BOOKS)

sqlg_jobs.MV_WSH_DELIVERABLES_V.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_WSH_DELIVERABLES_V)

sqlg_jobs.QKB_ITEM.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.QKB_ITEM)

sqlg_jobs.ERDRLRR_INSPECTION_STATUS_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ERDRLRR_INSPECTION_STATUS_WS1)

sqlg_jobs.ERDRLRR_INSPECTION_DETAIL_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ERDRLRR_INSPECTION_DETAIL_WS1)

sqlg_jobs.ERDRLRR_INSPECTION_RESULT_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ERDRLRR_INSPECTION_RESULT_WS1)

sqlg_jobs.PLANT.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.PLANT)

sqlg_jobs.SAP_MATERIALMASTER.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.SAP_MATERIALMASTER)

sqlg_jobs.MATERIALGROUP.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MATERIALGROUP)

sqlg_jobs.CONTROLTABLE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.CONTROLTABLE)

sqlg_jobs.EMS_LOOKUPVALUE_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.EMS_LOOKUPVALUE_NQJ)

sqlg_jobs.WO_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.WO_NQJ)

sqlg_jobs.SPN_TABL_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.SPN_TABL_NQJ)

sqlg_jobs.RESULTTYPE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.RESULTTYPE)

sqlg_jobs.MV_PDE_EXCEPTION_HEADER_V_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_PDE_EXCEPTION_HEADER_V_WS1)

sqlg_jobs.MV_PDE_EXCEPTION_EQUIP_V_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_PDE_EXCEPTION_EQUIP_V_WS1)

sqlg_jobs.MV_PDE_EXCEPTION_DETAIL_V_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_PDE_EXCEPTION_DETAIL_V_WS1)

sqlg_jobs.PDE_USER_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.PDE_USER_WS1)

sqlg_jobs.QCE_REASON_CODE_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.QCE_REASON_CODE_WS1)

sqlg_jobs.EMS_MANUFACTURER_WS1.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.EMS_MANUFACTURER_WS1)

sqlg_jobs.MODELTYPE.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MODELTYPE)

sqlg_jobs.EFLOW_ATLO_SCAR_CN.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.EFLOW_ATLO_SCAR_CN)

sqlg_jobs.ATLO_QUESTION_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ATLO_QUESTION_NQJ)

sqlg_jobs.EF_QCEXCEPTION_MST_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.EF_QCEXCEPTION_MST_NQJ)

sqlg_jobs.ATLO_SCAR_NQJ.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.ATLO_SCAR_NQJ)

sqlg_jobs.MV_XXCS_INCIDENTS_SFCS.dag=D_ODS_QAM
D_STG_INITxSYS_STS_STGxD_ODS_QAM.set_downstream(sqlg_jobs.MV_XXCS_INCIDENTS_SFCS)

D_SDM_QAM = airflow.DAG(    "D_SDM_QAM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_DM_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs.SDM_MATERIAL_CATEGORY_QA.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MATERIAL_CATEGORY_QA)

sqlg_jobs.SDM_PRODUCT_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_PRODUCT_TYPE)

sqlg_jobs.SDM_MODULE_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MODULE_TYPE)

sqlg_jobs.SDM_PRODUCT_DEVELOPMENT_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_PRODUCT_DEVELOPMENT_TYPE)

sqlg_jobs.SDM_MATERIAL_DEFECT_MODE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MATERIAL_DEFECT_MODE)

sqlg_jobs.SDM_CATEGORY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CATEGORY)

sqlg_jobs.SDM_QA_RESULT.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_QA_RESULT)

sqlg_jobs.SDM_C_FLOW_DEVELOPMENT_STAGE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_C_FLOW_DEVELOPMENT_STAGE)

sqlg_jobs.SDM_C_FLOW_DEVELOPMENT_DERI.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_C_FLOW_DEVELOPMENT_DERI)

sqlg_jobs.SDM_CONTROL_STATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CONTROL_STATION)

sqlg_jobs.SDM_CONTROL_THE_PROJECT.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CONTROL_THE_PROJECT)

sqlg_jobs.SDM_TURN_AROUND_TIME.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_TURN_AROUND_TIME)

sqlg_jobs.SDM_RMA_CASE_STATUS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_RMA_CASE_STATUS)

sqlg_jobs.SDM_PERSON_IN_CHARGE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_PERSON_IN_CHARGE)

sqlg_jobs.SDM_CLOSED_DAY_8D.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CLOSED_DAY_8D)

sqlg_jobs.SDM_TIER1.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_TIER1)

sqlg_jobs.SDM_SHIPPING_DATE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_SHIPPING_DATE)

sqlg_jobs.SDM_RETURN_SOURCE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_RETURN_SOURCE)

sqlg_jobs.SDM_WARRANTY_STATUS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_WARRANTY_STATUS)

sqlg_jobs.SDM_INVENTORY_OWNER.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_INVENTORY_OWNER)

sqlg_jobs.SDM_MANUFACTURER.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MANUFACTURER)

sqlg_jobs.SDM_CAVITY_NO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CAVITY_NO)

sqlg_jobs.SDM_CASE_CLOSE_STATUS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CASE_CLOSE_STATUS)

sqlg_jobs.SDM_STATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_STATION)

sqlg_jobs.SDM_MO_NO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MO_NO)

sqlg_jobs.SDM_MO_START_MONTH.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MO_START_MONTH)

sqlg_jobs.SDM_MO_PART_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MO_PART_TYPE)

sqlg_jobs.SDM_MP_APPROVE_DATE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MP_APPROVE_DATE)

sqlg_jobs.SDM_SR_NUMBER.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_SR_NUMBER)

sqlg_jobs.SDM_ATLO_FOR_MP.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_ATLO_FOR_MP)

sqlg_jobs.SDM_MP_FLAG.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MP_FLAG)

sqlg_jobs.SDM_PM.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_PM)

sqlg_jobs.SDM_CSD_REASON_PAY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CSD_REASON_PAY)

sqlg_jobs.SDM_CSD_MATERIAL_SCRAP_COS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CSD_MATERIAL_SCRAP_COS)

sqlg_jobs.SDM_CSD_CUSTOMER_PAID_SERV.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CSD_CUSTOMER_PAID_SERV)

sqlg_jobs.SDM_IQC_DAILY_INPUT_MANP_A.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_IQC_DAILY_INPUT_MANP_A)

sqlg_jobs.SDM_IQC_DAILY_INPUT_MANP.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_IQC_DAILY_INPUT_MANP)

sqlg_jobs.SDM_IQC_DAILY_TOTAL_INSP.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_IQC_DAILY_TOTAL_INSP)

sqlg_jobs.SDM_IQC_AVERAGE_INSPECTION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_IQC_AVERAGE_INSPECTION)

sqlg_jobs.SDM_INCOMING_MATERIAL_REJECT_LOTS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_INCOMING_MATERIAL_REJECT_LOTS)

sqlg_jobs.SDM_SUPPLIER_MATERIAL_PRODUC.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_SUPPLIER_MATERIAL_PRODUC)

sqlg_jobs.SDM_CUSTOMER_INSPECTION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CUSTOMER_INSPECTION)

sqlg_jobs.SDM_CUSTOMER_COMPLAIN_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CUSTOMER_COMPLAIN_CASES)

sqlg_jobs.SDM_IN_PROCESS_QUALITY_CONTROL.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_IN_PROCESS_QUALITY_CONTROL)

sqlg_jobs.SDM_QUALITY_ALERT_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_QUALITY_ALERT_CASES)

sqlg_jobs.SDM_EQUIPMENT_ANOMALY_CASE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_EQUIPMENT_ANOMALY_CASE)

sqlg_jobs.SDM_FIXTURE_ANOMALY_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_FIXTURE_ANOMALY_CASES)

sqlg_jobs.SDM_EQUIPMENT_FIXTURE_ANOM.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_EQUIPMENT_FIXTURE_ANOM)

sqlg_jobs.SDM_FAULT_INJECTION_DR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_FAULT_INJECTION_DR)

sqlg_jobs.SDM_Q_SCAN_DEFECT_RATE_DR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_Q_SCAN_DEFECT_RATE_DR)

sqlg_jobs.SDM_FINAL_QUALITY_INSPECTI.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_FINAL_QUALITY_INSPECTI)

sqlg_jobs.SDM_FQC_LRR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_FQC_LRR)

sqlg_jobs.SDM_QUALITY_HOLD_CASES.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_QUALITY_HOLD_CASES)

sqlg_jobs.SDM_CLOSE_WITHIN_SIPULATED.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CLOSE_WITHIN_SIPULATED)

sqlg_jobs.SDM_CUSTOMER_COMPLAIN_FOR.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CUSTOMER_COMPLAIN_FOR)

sqlg_jobs.SDM_ON_TIME_CLOSE_RATIO_FOR_WN.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_ON_TIME_CLOSE_RATIO_FOR_WN)

sqlg_jobs.SDM_CLOSE_WITHIN_14_DAYS_FO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CLOSE_WITHIN_14_DAYS_FO)

sqlg_jobs.SDM_CUSTOMER_COMPLAIN_FOR_S.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CUSTOMER_COMPLAIN_FOR_S)

sqlg_jobs.SDM_CLOSE_WITHIN_14_DAYS_RATIO.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CLOSE_WITHIN_14_DAYS_RATIO)

sqlg_jobs.SDM_FIELD_DEFECT_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_FIELD_DEFECT_QUANTITY)

sqlg_jobs.SDM_ON_SITE_REWORK_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_ON_SITE_REWORK_QUANTITY)

sqlg_jobs.SDM_IN_WARRANTY_RETURN_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_IN_WARRANTY_RETURN_QUANTITY)

sqlg_jobs.SDM_QUALITY_REJECT_QUANTITY.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_QUALITY_REJECT_QUANTITY)

sqlg_jobs.SDM_MODELS_WITH_MO_RECORDS.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_MODELS_WITH_MO_RECORDS)

sqlg_jobs.SDM_CSD_PLANNED_SHIPPING.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CSD_PLANNED_SHIPPING)

sqlg_jobs.SDM_ACTUAL_CALIBRATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_ACTUAL_CALIBRATION)

sqlg_jobs.SDM_PLANNED_CALIBRATION.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_PLANNED_CALIBRATION)

sqlg_jobs.SDM_CALIBRATION_COMPLETED_RATE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_CALIBRATION_COMPLETED_RATE)

sqlg_jobs.SDM_TICKET_TYPE.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_TICKET_TYPE)

sqlg_jobs.SDM_FINAL_QUALITY_INSPECT.dag=D_SDM_QAM
D_STG_INITxSYS_STS_STGxD_SDM_QAM.set_downstream(sqlg_jobs.SDM_FINAL_QUALITY_INSPECT)

D_DM_QAM = airflow.DAG(    "D_DM_QAM",
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    template_searchpath=tmpl_search_path,
    default_args=args,
    start_date=airflow.utils.dates.days_ago(1),    
    max_active_runs=1)

### D_STG_INITxSYS_STS_STGxD_ODS_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_ODS_QAM"
D_STG_INITxSYS_STS_STGxD_ODS_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_SDM_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_SDM_QAM"
D_STG_INITxSYS_STS_STGxD_SDM_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
### D_STG_INITxSYS_STS_STGxD_DM_QAM

my_taskid = "D_STG_INITxSYS_STS_STGxD_DM_QAM"
D_STG_INITxSYS_STS_STGxD_DM_QAM= ExternalTaskSensor(
    task_id=my_taskid,
    external_dag_id="D_STG_INIT",
    external_task_id="SYS_STS_STG",
    execution_delta=None,  # Same day as today
)
sqlg_jobs.DIM_MATERIAL_CATEGORY_QA.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MATERIAL_CATEGORY_QA)

sqlg_jobs.DIM_PRODUCT_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_PRODUCT_TYPE)

sqlg_jobs.DIM_MODULE_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MODULE_TYPE)

sqlg_jobs.DIM_PRODUCT_DEVELOPMENT_TYPE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_PRODUCT_DEVELOPMENT_TYPE)

sqlg_jobs.DIM_MATERIAL_DEFECT_MODE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MATERIAL_DEFECT_MODE)

sqlg_jobs.DIM_CATEGORY.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_CATEGORY)

sqlg_jobs.DIM_QA_RESULT.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_QA_RESULT)

sqlg_jobs.DIM_CONTROL_STATION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_CONTROL_STATION)

sqlg_jobs.DIM_CONTROL_THE_PROJECT.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_CONTROL_THE_PROJECT)

sqlg_jobs.DIM_TURN_AROUND_TIME.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_TURN_AROUND_TIME)

sqlg_jobs.DIM_RMA_CASE_STATUS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_RMA_CASE_STATUS)

sqlg_jobs.DIM_PERSON_IN_CHARGE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_PERSON_IN_CHARGE)

sqlg_jobs.DIM_CLOSED_DAY_8D.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_CLOSED_DAY_8D)

sqlg_jobs.DIM_TIER1.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_TIER1)

sqlg_jobs.DIM_SHIPPING_DATE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_SHIPPING_DATE)

sqlg_jobs.DIM_RETURN_SOURCE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_RETURN_SOURCE)

sqlg_jobs.DIM_WARRANTY_STATUS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_WARRANTY_STATUS)

sqlg_jobs.DIM_INVENTORY_OWNER.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_INVENTORY_OWNER)

sqlg_jobs.DIM_CAVITY_NO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_CAVITY_NO)

sqlg_jobs.DIM_CASE_CLOSE_STATUS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_CASE_CLOSE_STATUS)

sqlg_jobs.DIM_STATION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_STATION)

sqlg_jobs.DIM_C_FLOW_DEVELOPMENT_STAGE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_C_FLOW_DEVELOPMENT_STAGE)

sqlg_jobs.DIM_C_FLOW_DEVELOPMENT_DERI.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_C_FLOW_DEVELOPMENT_DERI)

sqlg_jobs.DIM_ATLO_FOR_MP.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_ATLO_FOR_MP)

sqlg_jobs.DIM_MP_FLAG.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MP_FLAG)

sqlg_jobs.DIM_PM.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_PM)

sqlg_jobs.DIM_MO_NO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MO_NO)

sqlg_jobs.DIM_MO_START_MONTH.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MO_START_MONTH)

sqlg_jobs.DIM_MP_APPROVE_DATE.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_MP_APPROVE_DATE)

sqlg_jobs.DIM_SR_NUMBER.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.DIM_SR_NUMBER)

sqlg_jobs.FCT_CSD_MATERIAL_SCRAP_COS.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CSD_MATERIAL_SCRAP_COS)

sqlg_jobs.FCT_CSD_CUSTOMER_PAID_SERV.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CSD_CUSTOMER_PAID_SERV)

sqlg_jobs.FCT_IQC_DAILY_INPUT_MANP.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_IQC_DAILY_INPUT_MANP)

sqlg_jobs.FCT_IQC_DAILY_TOTAL_INSP.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_IQC_DAILY_TOTAL_INSP)

sqlg_jobs.FCT_IQC_AVERAGE_INSPECTION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_IQC_AVERAGE_INSPECTION)

sqlg_jobs.FCT_SUPPLIER_MATERIAL_PRODUC.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_SUPPLIER_MATERIAL_PRODUC)

sqlg_jobs.FCT_CUSTOMER_INSPECTION.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CUSTOMER_INSPECTION)

sqlg_jobs.FCT_CUSTOMER_COMPLAIN_CASES.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CUSTOMER_COMPLAIN_CASES)

sqlg_jobs.FCT_FAULT_INJECTION_DR.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_FAULT_INJECTION_DR)

sqlg_jobs.FCT_Q_SCAN_DEFECT_RATE_DR.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_Q_SCAN_DEFECT_RATE_DR)

sqlg_jobs.FCT_QUALITY_HOLD_CASES.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_QUALITY_HOLD_CASES)

sqlg_jobs.FCT_CLOSE_WITHIN_SIPULATED.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CLOSE_WITHIN_SIPULATED)

sqlg_jobs.FCT_CUSTOMER_COMPLAIN_FOR.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CUSTOMER_COMPLAIN_FOR)

sqlg_jobs.FCT_ON_TIME_CLOSE_RATIO_FOR_WN.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_ON_TIME_CLOSE_RATIO_FOR_WN)

sqlg_jobs.FCT_CLOSE_WITHIN_14_DAYS_FO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CLOSE_WITHIN_14_DAYS_FO)

sqlg_jobs.FCT_CUSTOMER_COMPLAIN_FOR_S.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CUSTOMER_COMPLAIN_FOR_S)

sqlg_jobs.FCT_CLOSE_WITHIN_14_DAYS_RATIO.dag=D_DM_QAM
D_STG_INITxSYS_STS_STGxD_DM_QAM.set_downstream(sqlg_jobs.FCT_CLOSE_WITHIN_14_DAYS_RATIO)

