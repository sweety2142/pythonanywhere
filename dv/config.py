#-*- coding:utf8 -*-
from datetime import datetime, timedelta

class Cfg(object):
	TITLE			= u'DEV'
	PORT = 3333
	HOME = '/var/www/flask/TT/dev'
	DB_URL = 'sqlite:///'
	DB_LOG_FLAG = 'True'
	USER_PATH = 'dv/data/db/user.db'
	LOG_FILE = 'dv/data/log/dev_users.log'
	LOGGER_FILE = 'dv/data/log/dev_log.log'
	SECRET_KEY = 'development key'
	DEBUG = True
	SIGNUP = True
	TEST_MODE = True
	ADMIN_USER = ['sh','test','i','김일호']
	NOW = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
	NOW_YMD = datetime.today().strftime('%Y-%m-%d')
	REMEMBERED_PERIOD = timedelta(hours=1)
	TEMPLATE={
		'main':'main.html',
		'layout':'layout.html',
		'signup':'signup.html',
		'login':'login.html',
		'cont_header':'contents/cont_header.html'
	}
	LOG_ACTIVITY = {
		'in':'IN',
		'do':'DO',
		'signup':'SIGNUP',
		'login':'LOGIN',
		'logout':'LOGOUT',
		'manual':'MANUAL'
	}
	
	DB ={
	    'THIS_COMPANY':{'path':'dv/data/db/this_company.db',
					    'table_name':'THIS_COMPANY',
					    'column':['코드','회사명','프린트상호','주소1','주소2','faxNo']
		},
	    'AGENT':{'path':'dv/data/db/Agent.db',
			     'table_name':'AGENT',
			     'column':['코드','Agent','AgentName','addr','TEL','FAX','DAM','JIK','EMAIL','MOBIL','LEVEL'],
			     'column_v':['코드','Agent','AgentName','addr','TEL','FAX','DAM','JIK','EMAIL','MOBIL','LEVEL','pk']
	    },
        'BANK':{'path':'dv/data/db/bank.db',
                    'table_name':'BANK',
                    'column':['코드','은행','영문명'],
                    'column_v':['코드','은행','영문명','pk']
            },
        'BUYER':{'path':'dv/data/db/buyer.db',
                     'table_name':'BUYER',
                     'column':['코드','Buyer','프린트Buyer','주소1','주소2','TEL','FAX','DAM','JIK','EMAIL','MOBIL','LEVEL','바이어코드','등급발행일','pk']
            },
		'BUYERBANK':{'path':'dv/data/db/BUYERBANK.db',
					 'table_name':'BUYERBANK',
					 'column':['Code','BankName','Address'],
					 'column_v':['Code','BankName','Address','pk']
		},
		'COMPANY':{'path':'dv/data/db/company.db',
				   'table_name':'COMPANY',
				   'column':['코드','업체','MAKER','ADDR','TEL','FAX','DAM','JIK','EMAIL','MOBIL','LBL'],
				   'column_v':['코드','업체','MAKER','ADDR','TEL','FAX','DAM','JIK','EMAIL','MOBIL','LBL','pk']
		},
			'CONTAINERYARD':{'path':'dv/data/db/CONTAINERYARD.db',
						 'table_name':'CONTAINERYARD',
						 'column':['CODE','Container','TEL','담당자'],
						 'column_v':['CODE','Container','TEL','담당자','pk']
		},
		'CONTRACT_CONDITION':{'path':'dv/data/db/contract_condition.db',
							  'table_name':'CONTRACT_CONDITION',
							  'column':['CODE','계약조건'],
							  'column_v':['CODE','계약조건','pk']
		},
		'CURRENCY_UNIT':{'path':'dv/data/db/currency_unit.db',
						 'table_name':'CURRENCY_UNIT',
						 'column':['코드','화폐단위'],
						 'column_v':['코드','화폐단위','pk']
		},
	    'DELIVERYPLACE':{'path':'dv/data/db/DELIVERYPLACE.db',
						 'table_name': 'DELIVERYPLACE',
						 'column':['CODE','Delivery_Place'],
						 'column_v':['CODE','Delivery_Place','pk']
		},
		'DEPARTMENT':{'path':'dv/data/db/department.db',
					  'table_name': 'DEPARTMENT',
					  'column':['Code','부서명'],
					  'column_v':['Code','부서명','pk']
		},
		'DESTINATION':{'path':'dv/data/db/destination.db',
					   'table_name': 'DESTINATION',
					   'column':['코드','도착지','프린트도착지1','프린트도착지2'],
					   'column_v':['코드','도착지','프린트도착지1','프린트도착지2','pk']
		},
		'EXCHANGE_RATE':{'path':'dv/data/db/exchange_rate.db',
						 'table_name': 'EXCHANGE_RATE',
						 'column':['기준일자','화폐단위','환율'],
						 'column_v':['기준일자','화폐단위','환율','pk']
		},
		'FAIRWAY':{'path':'dv/data/db/fairway.db',
				   'table_name':'FAIRWAY',
				   'column':['코드','항로'],
				   'column_v':['코드','항로','pk']
		},
		'FORWARDING':{'path':'dv/data/db/FORWARDING.db',
					  'table_name':'FORWARDING',
					  'column':['CODE','FORWARDING'],
					  'column_v':['CODE','FORWARDING','pk']
		},
		'FTA_CONVENTION':{'path':'dv/data/db/FTA_convention.db',
						  'table_name':'FTA_CONVENTION',
						  'column':['CODE','협정명칭'],
						  'column_v':['CODE','협정명칭','pk']
		},
		'FTA_ITEM_NUMBER':{'path':'dv/data/db/FTA_item_number.db',
						   'table_name':'FTA_ITEM_NUMBER',
						   'column':['CODE','품목번호'],
						   'column_v':['CODE','품목번호','pk']
		},
		'FTA_ORIGIN':{'path':'dv/data/db/FTA_origin.db',
					  'table_name':'FTA_ORIGIN',
					  'column':['CODE','원산지'],
					  'column_v':['CODE','원산지','pk']
		},
		'ITEM':{'path':'dv/data/db/ITEM.db',
				'table_name': 'ITEM',
				'column':['코드','Item','프린트_Item'],
				'column_v':['코드','Item','프린트_Item','pk']
		},
		'LOCALTRUCKING':{'path':'dv/data/db/LOCALTRUCKING.db',
						 'table_name':'LOCALTRUCKING',
						 'column':['CODE','Local_trucking'],
						 'column_v':['CODE','Local_trucking','pk']
		},
		'LUSTER':{'path':'dv/data/db/LUSTER.db',
				  'table_name':'LUSTER',
				  'column':['코드','Luster','프린트Luster'],
				  'column_v':['코드','Luster','프린트Luster','pk']
		},
		'PAYMENT':{'path':'dv/data/db/PAYMENT.db',
				   'table_name':'PAYMENT',
				   'column':['코드','Payment'],
				   'column_v':['코드','Payment','pk']
		},
		'PURCHASE_METHOD':{'path':'dv/data/db/purchase_method.db',
						   'table_name':'PURCHASE_METHOD',
						   'column':['Code','매입방식'],
						   'column_v':['Code','매입방식','pk']
		},
		'QUANTITY':{'path':'dv/data/db/quantity.db',
					'table_name':'QUANTITY',
					'column':['코드','수량단위'],
					'column_v':['코드','수량단위','pk']
		},
		'SEA':{'path':'dv/data/db/SEA.db',
			   'table_name':'SEA',
			   'column':['Code','선적방법'],
			   'column_v':['Code','선적방법','pk']
		},
		'SHIPPING_COMPANY':{'path':'dv/data/db/shipping_company.db',
							'table_name':'SHIPPING_COMPANY',
							'column':['코드','선박회사'],
							'column_v':['코드','선박회사','pk']
		},
		'TERM':{'path':'dv/data/db/TERM.db',
				'table_name':'TERM',
				'column':['코드','Term'],
				'column_v':['코드','Term','pk']
		}
		,
		'orderno':{
			'path': 'dv/data/db/orderno.db',
			'table_name': 'orderno',
			'column': ['OrderNo', 'OrderGubun','Buyer','Agent','Item','DN','LF','LS','Remark','QTY','수량단위','U_PRX','AMOUNT','FOB_단가','Fob_Amt','DELI','OrderTerm','도착지','OrderPayMent','DAYS','COM1','COM2','LCNo','SD','ED','MARGIN','OrderCommTotal','계약일자','ORDER화폐단위','외화','PONUMBER']
		}
		,
		'nego':{
			'path':'dv/data/db/nego.db',
			'table_name':'nego',
			'view_db':['InvNo','LF','DueDate','LS'],
			'column':['InvNo','DueDate','Buyer','Agent','LCNo','Item','DN','LF','LS','Remark','Maker','Nego수량','Nego달러','Nego원화','FOBAmount달러','FOBAmount원화','선명','서류일자','선적일자','선임달러','선임원화','적화보험료달러','적화보험료원화','수출보험료달러','수출보험료원화','우편료달러','우편료원화','기타달러','기타원화','Margin달러','Margin원화','면장번호','면장신고일자','면장FOB달러','면장FOB원화','Nego일자','RefNo','화폐단위','Nego기타통화','인수일자','인수확정일자','PAYMENTDATE','면장번호_1','OrderPayment','LoteNo','ConNo','BLNo','결제일자','화폐단위_1','NEGO단가','FOB단가','Term','Bank','InvoiceNo','InvoiceDate','도착지','도착지_1','BuyerBankName','잔액외화','잔액달러','TT','Com1','Amount1','Agent_1','Com2','Amount2','Agent_2','Com3','Amount3','Agent_3','Com4','Amount4','Agent_4','환가요율','old_orderno','LessDeley달러','LessDeley원화','Less달러','Less원화','인수지연달러','인수지연원화','계산서일자1','계산서수량1','계산서금액1','계산서금액달러1','계산서일자2','계산서수량2','계산서금액2','계산서금액달러2','계산서일자3','계산서수량3','계산서금액3','계산서금액달러3','계산서일자4','계산서수량4','계산서금액4','계산서금액달러4','출고일','입금일자1','입금액1','입금일자2','입금액2','입금일자3','입금액3','입금일자4','입금액4','입금일자5','입금액5','환가료환출달러','환가료환출원화','PONUMBER','Order예상선임','Demurrage달러','Demurrage원화','UnderValue']
		},
		'alldata_ship':{
			'path':'dv/data/db/alldata_ship.db',
			'table_name':'alldata_ship',
			'column':['order_title','gubun','doc_1','date_doc_1','doc_2',
					  'date_doc_2','doc_3','doc_4','doc_5','doc_6',
					  'doc_7','doc_8','doc_10','doc_11','doc_12',
					  'date_doc_13','doc_14','doc_15','doc_16','doc_17',
					  'date_request','shipcompany','date_sailing','date_job','factory',
					  'movement','date_sailday','date_BLsailday','sunim','damdang',
					  'THC','remark','tel','fax']
			
		},
		'alldata_user':{
			'path':'dv/data/db/alldata_user.db',
			'table_name':'alldata_user',
			'column':['order_title','user_name']
		},
		'alldata_deliveryorder':{
			'path':'dv/data/db/alldata_deliveryorder.db',
			'table_name':'alldata_deliveryorder',
			'column':['orderno','gubun','to1','from1','date_order',
			          'buyer','destination','item1','item2','item3',
					  'item4','date_container','shipping','packing','company',
					  'forwarding','booking','vessel','cont_sel','tel',
					  'damdang','customer','closing_doc_date','closing_doc','closing_cont_date',
					  'closing_cont','etd','eta','place','localtrucking']
		},
		'inst_nego_bank':{
			'path':'dv/data/db/inst_nego_bank.db',
			'table_name':'INST_NEGO_BANK',
			'column':['name','english','address','swift','account',
			          'benefit','account2','benefit2']
		},
		'alldata_contract2':{
			'path':'dv/data/db/alldata_contract2.db',
			'table_name':'alldata_contract2',
			'column':[
				"ordercon"	, 	"gubun"	,	"messrs"	,	"shipment"	,	"packing"	,
	   	        "insurance"	,	"remark"	,	"contractdate"	,	"contractno"	,	"buyersref"	,
	            "portodfdischarging"	,	"transshipment"	,	"partialshipment"	,	"payment"	,	"inspection"	,
	            "commodity1"	,	"quantity1"	,	"unitprice1",	"about1"	,	"commodity2"	,
	            "quantity2"	,	"unitprice2"	,	"about2"	,	"commodity3" ,	"quantity3"	,
	            "unitprice3"	,	"about3"	,	"totalquantity"	,	"totalabout"	,	"term"	, 
				"port"
			]
		},
		'alldata':{
			'path': 'dv/data/db/alldata.db',
			'table_name': 'ALLDATA',
			'column': ['Index', 'buyer_order', 'OrderNo', 'OrderGubun', 'agent_order', 
			           'datepicker', 'date_stand', 'date_delivery', 'term_order', 'arrive_order',
					   'payment_order','order_term', 'method_order', 'document_order','order_com1',
					   'order_com1_amount','order_com1_to','order_com2','order_com2_amount','order_com2_to',
					   'order_com3','order_com3_amount','order_com3_to','order_com4','order_com4_amount',
					   'order_com4_to','order_com_total','item_order','order_DN','order_LF',
					   'LS_order','order_remark','order_suip','order_ponum','order_quantity',
					   'QTY_order','PRC_order','order_prc','order_cross_rate','order_dollor',
					   'order_LC','order_receive_LC','date_SD','date_ED','table_supply',
					   'order_expect_price','order_etc_per','order_etc_amount','order_expect_margin','order_supplyremark',
					   'order_special','buyerbank_order','order_before_order','inv_ship','actual_ship',
					   'ship_BL','ETA_ship','ship_size','tableSPL_ship','bank_nego',
					   'day_nego','nego_ref','nego_InvNo','nego_quantity','unit_nego',
					   'nego_TT','nego_underV','unit_nego_table','nego_etc','nego_etc_dollor',
					   'neto_etc_exchange','nego_won','nego_cross','nego_cross_amount','nego_com1_rate',
					   'nego_com1_amount','nego_hwanga','nego_com2_rate','nego_com2_amount','nego_com_total',
					   'nego_uwon','nextnego_nego','nego_m1','radio','nego_m3',
					   'buymethod_nego','nego_m4','DueDate_nego','report_nego','get_nego',
					   'table_nego','nego_incomplete_value','nego_comment','table_local','paydate1_local',
					   'paydate2_local','paydate3_local','paydate4_local','BillInvoice1','BillInvoice2',
					   'BillInvoice3','BillInvoice4','BillMoneyInvoice1','BillMoneyInvoice2','BillMoneyInvoice3',
					   'BillMoneyInvoice4','BillDollorInvoice1','BillDollorInvoice2','BillDollorInvoice3','BillDollorInvoice4',
					   'BillRate1','BillRate2','BillRate3','BillRate4','local_sunim',
					   'local_sunim2','local_demur','local_demur2','local_su','local_su2',
					   'local_jukwha','local_jukwha2','local_transport','local_transport2','local_comm',
					   'local_comm2','paycomm_local','clean_local','local_lc_open','local_lc_open2',
					   'local_receive_LC','local_receive_LC_won','local_u','local_u2','local_hwanhwan','local_hwanhwan2','local_delay','local_delay2','local_less','local_less2','local_insudelay','local_insudelay2','local_actual',
					   'local_actual2','local_special','out_fta','item_fta','place_fta','cont_fta','pk','port'],
					   
			'view_db': ['buyer_order', 'OrderNo', 'OrderGubun', 'agent_order', 'datepicker', 'date_stand', 'date_delivery', 'term_order', 'arrive_order', 'payment_order',
					   'order_term', 'method_order', 'document_order','order_com1','order_com1_amount','order_com1_to','order_com2','order_com2_amount','order_com2_to','order_com3',
					   'order_com3_amount','order_com3_to','order_com4','order_com4_amount','order_com4_to','order_com_total','item_order','order_DN','order_LF',
					   'LS_order','order_remark','order_suip','order_ponum','order_quantity','QTY_order','PRC_order','order_prc','order_cross_rate','order_dollor','order_LC',
					   'order_receive_LC','date_SD','date_ED','table_supply','order_expect_price','order_etc_per','order_etc_amount','order_expect_margin','order_supplyremark',
					   'order_special','buyerbank_order','order_before_order','inv_ship','actual_ship','ship_BL','ETA_ship','ship_size','tableSPL_ship','bank_nego','day_nego',
					   'nego_ref','nego_InvNo','nego_quantity','unit_nego','nego_TT','nego_underV','unit_nego_table','nego_etc','nego_etc_dollor','neto_etc_exchange',
					   'nego_won','nego_cross','nego_cross_amount','nego_com1_rate','nego_com1_amount','nego_hwanga','nego_com2_rate','nego_com2_amount','nego_com_total',
					   'nego_uwon','nextnego_nego','nego_m1','radio','nego_m3','buymethod_nego','nego_m4','DueDate_nego','report_nego','get_nego','table_nego','nego_incomplete_value',
					   'nego_comment','table_local','paydate1_local','paydate2_local','paydate3_local','paydate4_local','BillInvoice1','BillInvoice2','BillInvoice3','BillInvoice4',
					   'BillMoneyInvoice1','BillMoneyInvoice2','BillMoneyInvoice3','BillMoneyInvoice4','BillDollorInvoice1','BillDollorInvoice2','BillDollorInvoice3','BillDollorInvoice4',
					   'BillRate1','BillRate2','BillRate3','BillRate4','local_sunim','local_sunim2','local_demur','local_demur2','local_su','local_su2','local_jukwha','local_jukwha2',
					   'local_transport','local_transport2','local_comm','local_comm2','paycomm_local','clean_local','local_lc_open','local_lc_open2','local_receive_LC','local_receive_LC_won',
					   'local_u','local_u2','local_hwanhwan','local_hwanhwan2','local_delay','local_delay2','local_less','local_less2','local_insudelay','local_insudelay2','local_actual',
					   'local_actual2','local_special','out_fta','item_fta','place_fta','cont_fta','port','pk']
		
		}
	
	
	
	
  #'THIS_COMPANY':{'path':'dv/data/this_company.db',
  #                'table_name':'THIS_COMPANY',
  #                'column':['코드','회사명','프린트상호','주소1','주소2','faxNo']
  #                },      
  }

