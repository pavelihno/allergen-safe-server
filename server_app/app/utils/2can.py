import hashlib

public_key = '126dab4b35a30663b103cc072761c92b'
private_key = 'b47d9572d55b8fae97335aae4584499a'

url = f'https://my2can.com/api/v1_ticket.json/{public_key}'

'''
Request to url. Receiving:
{
    "status": "success",
    "data": {
        "ticket": "65c87f4d62adc"
    }
}
'''

ticket = '65cc6717b78f3'

token = hashlib.md5((private_key + ticket).encode()).hexdigest()

print(token)