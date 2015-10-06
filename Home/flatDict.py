def flatten(data, res):
  '''for key in data:
    for element in data.get(key):
      # print data.get(key, {}).get(element, {})
      #print data.get(key).get(element)
      print data.key
  '''
  #print data.get('name',{}).get('first',{}).get('one')
  #if isinstance(data, dict):
  for key in data:
    #print data[key]
    if isinstance(data[key], dict):
      #print data[key]
      res.update({key: "" + data.get(key)})
      #flatten(data[key], res)
    #  print tmp 
      #res.update({key: tmp.get()})
    #else:
  print res
      
        
 
data = {
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

flatten(data, {})
