# /

DB=app.config['DB']

db_cont = get_db(DB)
return render_template(LAYOUT_URL, db_c = db_cont)

def get_db(data):
  """ key > THIS_COMPANY #str
      value['path'] > dv/data/db/this_company.db
      value['table_name'] > THIS_COMPANY
      item > 회사명, 프린트상호, 주소1 ...
      col[0] (주)두베스트, 직물 업체 ...
  """
  make_dict = {}
  temp_dict = {}
  temp_list = []
  for key, value in data.items():
    for item in value['column']:
      temp = query_db(value['path'], select_query(value['table_name'], item))
      for i, col in enumerate(temp): #tuple >> list
        temp_list.append(col[0])
      temp_dict[item] = temp_list
      temp_list=[]
    make_dict[key] = temp_dict
  
  return make_dict
  
  
#config

      
#checkoutPage
{% for key in db_c %}
{% for key,value in tt[key].items() %}
{{ value }}
{% endfor %}    
      
