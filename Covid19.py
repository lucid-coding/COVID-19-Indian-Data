import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def caps(name : str) -> str :
    """
    A function that modifies name
    ---
    name : str
    """
    if len(name.split())==1:
        return name.capitalize()
    else:
        sep=[word.capitalize() for word in name.split()]
        final=sep[0]+' '+sep[1]
        return final

def State():
    """
    A function that finds a place/state
    ---
    Arguments -> None
    """
    
    url='https://api.covid19india.org/data.json'
    print('Retrieving  data...wait a moment')
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    js=json.loads(data)

    place = [i for i in js["statewise"]]
    print('\n'.join(place))
    
    def inputs():
      n=input('\n\nEnter the states from above list to get the results:')
      n=caps(n)
      state_index=place.index(n)
      return state_index,n

    try:
      state_index,n=inputs();
    except ValueError:
      print("Please check the spelling of states from above list")
      state_index,n=inputs()

    confirmed=js['statewise'][state_index]['confirmed']
    active=js['statewise'][state_index]['active']
    recovered=js['statewise'][state_index]['recovered']
    deaths=js['statewise'][state_index]['deaths']
    update=js['statewise'][state_index]['lastupdatedtime']
    
    return n, confirmed, active, recovered, deaths, update

def district(n):
    url='https://api.covid19india.org/state_district_wise.json'
    print('Retrieving  data...wait a moment')
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    js=json.loads(data)

    districts=[]
    for i in js[n]['districtData']:
        print(i)
        districts.append(i)

    def dist_inputs_and_result() -> None:
      """
      A first class function that shows the stats of the api call.
      ---
      Arguments -> None
      """
      m=input('\n\nEnter the Districts from above list to get the results:')
      m=caps(m)
      print('Confirmed cases:', js[n]['districtData'][m]['confirmed'])
      print('Active cases:', js[n]['districtData'][m]['active'])
      print('Recovered:', js[n]['districtData'][m]['recovered'])
      print('Death:', js[n]['districtData'][m]['deceased'])
      print('\n\n\t Refresh the page to check for another state and district \n\t\t\t\t\t THANK YOU')
      return None
    
    try:
      dist_inputs_and_result()
    except KeyError:
      print("Please check the spelling of Districts from the above list")
      dist_inputs_and_result()

    return None

input("Press enter to get COVID 19 results") 
n, confirmed, active, recovered, deaths, update=State()
print('Confirmed Cases:', confirmed)
print('active Cases:', active)
print('Recovered:', recovered)
print('Deaths:', deaths)
print('Last Updated time:', update)


confirmation=input("\n\nDo you want to Check the district Wise results of "+n+" state  [y/n]:\n")

    

if confirmation=='y':
    district(n)
else:
    print("\t\t THANK YOU")
