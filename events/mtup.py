import datetime
import meetup.api
# insert your secret key that you can find there https://secure.meetup.com/meetup_api/key/
client = meetup.api.Client('20_INSERT_YOUR_KEY_e318')
groups = client.GetFindGroups({'text':'Python'})
ids=[x['id'] for x in groups.items]
group_ids=",".join([str(x) for x in ids])
events=client.GetEvents({'group_id':group_ids})

def get_address(event):
  if 'event' in event:
    ven = event['venue']
    return str(ven['lat']) + ',' + str(ven['lon']) + ":" + ven['name'] + ', ' + ven['address_1'] + ',' + ven['city'] + ',' + ven['localized_country_name']
# lots of events only provide the location to the members :(
  return 'unknown'

for event in events.results:
  print('-------------')
  print(' * name of the event: ' + event['group']['name'] + '/' + event['name'])
  print(' * type of event: *** meetup')
  print(' * focus on Python: ' + event.get('description',''))
  print(' * approximate number of attendees: ' + str(event['yes_rsvp_count']))
  print(' * location (incl. country): ' + get_address(event))
  # TODO: add timezone
  print(' * dates/times/recurrence (incl. time zone): ' + datetime.datetime.utcfromtimestamp(int(event['time'])/1000).strftime('%Y-%m-%d %H:%M:%S'))
  print(' * link (in HTML format): <a href="' + event['event_url'] + '">' + event['name'] + '</a>')
  print('---------------')
