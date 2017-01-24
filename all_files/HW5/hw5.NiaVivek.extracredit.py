
import urllib.request
import urllib 
import json
import oauth2
import operator
# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
TOKEN = ''
TOKEN_SECRET = ''

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API

def yelp_req(url):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
    try:
        oauth_request = oauth2.Request('GET', url, {})
        oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': TOKEN,
                'oauth_consumer_key': CONSUMER_KEY
            }
        )
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth2.Token(TOKEN, TOKEN_SECRET)
        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        signed_url = oauth_request.to_url()

        conn = urllib.request.urlopen(signed_url)
    except:
        print('Error with authentication. Enter authentication code.')
        return
    try:
        response = json.loads(conn.read().decode('utf8'))
    finally:
        conn.close()

    return response

#################################################################################
# Your code goes here
#Reference- http://matatat.org/yelp-timelines.html

def search(term, sort, location, limit=5, offset=0):
    """ Search Yelp with a term and location """
    url = 'http://api.yelp.com/v2/search'
    #adding search terms to the URL
    url_params = {'term':term.replace(' ','+'),
                  'location': location.replace(' ', '+'),
                  'offset':offset,
                  'sort_by': sort.replace(' ', '+'),
                  'limit': limit}
    try:
        params = urllib.parse.urlencode(url_params)
        response = yelp_req(url+'?'+params)
        bizs = response['businesses']
    except:
        print('Error opening URL')
        return
    return bizs

def get_business(id):
    """ Get business from Yelp """
    url = 'http://api.yelp.com/v2/business/{}'.format(id)
    response = yelp_req(url)
    return response

def get_restaurant():
    try:
        #search for restaurants in SFO
        bizs1 = search('restaurants','rating', 'San Francisco, CA',20)
        bizs2 = search('restaurants','rating', 'San Francisco, CA',20,20)
        #biz = get_business(bizs[0]['id'])
        #get the list from the 2 URL and make a dict using restaurant name and reviews
    
        dict_rest = dict()
        for biz in bizs1:
            dict_rest[biz['name']] = biz['review_count']
        for biz in bizs2:
            dict_rest[biz['name']] = biz['review_count']
    except:
        print('Error finding restaurants.')
        return
    #sort the dictionary
    sorted_rest = sorted(dict_rest.items(), key=operator.itemgetter(1), reverse = True)
    #write the dict to file
    write_file(sorted_rest)

def write_file(sorted_list):
    """Function to write the sorted list of restaurants"""
    try:
        with open('restaurants2.NiaVivek.txt','w') as write_file:
            for k,v in sorted_list:
                write_file.write(k + ", " + str(v) +"\n")
    except:
        print('Error writing to file')

def main():
    get_restaurant()

if __name__ == '__main__':
    main()



